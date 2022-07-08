from django.shortcuts import render, get_object_or_404
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
from django.http import HttpResponse, Http404
from donate.models import donate
from account.models import User

def go_to_gateway_view(request,donate_to,amount):

    get_object_or_404(User, username=donate_to)
    # خواندن مبلغ از هر جایی که مد نظر است
    #amount = 50000
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    #user_mobile_number = '+989112221234'  # اختیاری

    factory = bankfactories.BankFactory()
    try:
        bank = factory.create() # or factory.auto_create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url(f'/callback-gateway/{donate_to}/{amount}/')
        #bank.set_mobile_number(user_mobile_number)  # اختیاری
    
        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید. 
        bank_record = bank.ready()
        
        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        
        # TODO: redirect to failed page.
        raise e

def callback_gateway_view(request,donate_to,amount):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        try:
            d = donate(donate_to=donate_to,amount=amount,payment_status=True,tracking_code=tracking_code)
            d.save()
            U = get_object_or_404(User, username=donate_to)
            U.wallet += amount
            U.save()
            # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
            # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
            return render(request, 'peyment/success.html')
        except:
            raise Http404
    try:
        d = donate(donate_to=donate_to,amount=amount,payment_status=False,tracking_code=tracking_code)
        d.save()
    
        # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
        return render(request, 'peyment/failed.html')
    except:
        raise Http404
