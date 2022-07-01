from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
UserAdmin.fieldsets[2][1]['fields'] = (
                                        "is_active",
                                        "is_staff",
                                        'wallet',
                                        "job",
                                        "card_number",
                                        "avatar",
                                        "is_superuser",
                                        'groups',
                                        'user_permissions'
                                    )
admin.site.register(User, UserAdmin)


