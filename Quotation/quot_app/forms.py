from django import forms
from .models import Customer, Company


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'




class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'companyName',
            'printCompanyName',
            'address1',
            'address2',
            'pincode',
            'contact',
            'gstIn',

        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['companyName'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Company Name'})
        self.fields['printCompanyName'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Print Company Name'})
        self.fields['address1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Address 1'})
        self.fields['address2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Address 2'})
        self.fields['pincode'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Pincode'})
        self.fields['contact'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Contact'})
        self.fields['gst'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter GST'})
        self.fields['state'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter State'})

    def clean_companyName(self):
        company_name = self.cleaned_data.get('companyName')
        if Company.objects.filter(companyName=company_name).exists():
            raise forms.ValidationError('A company with this name already exists.')
        return company_name