from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

UserAdmin.list_display += ('sms_code', 'sms_status')
UserAdmin.fieldsets += (
    (None, {'fields': ('sms_code', 'sms_status')}),
)
