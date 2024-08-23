from django.contrib import admin

from quot_app.models import Company


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyName', 'contact', 'pincode', 'gstIn')