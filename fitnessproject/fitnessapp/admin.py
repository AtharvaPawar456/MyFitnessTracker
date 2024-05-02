from django.contrib import admin

# Register your models here.


from .models import UserAccountDetails, DailyTracking, PaymentsTracking

# Register your models here.

admin.site.register(UserAccountDetails)
admin.site.register(DailyTracking)
admin.site.register(PaymentsTracking)