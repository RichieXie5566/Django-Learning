from django import forms
from .models import ShippingAddress
from store.models import Product

class ShippingForm(forms.ModelForm):

    shipping_full_name = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'姓名'}), required=True)
    shipping_email  = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'電子信箱'}), required=False)
    shipping_phone = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'電話'}), required=True)
    shipping_address1 = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'地址第一行'}), required=True)
    shipping_address2 = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'地址第二行'}), required=False)
    shipping_city = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'城市'}), required=True)
    shipping_zipcode = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'郵遞區號'}), required=True)
    shipping_country = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'國家'}), required=True)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_phone', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_zipcode', 'shipping_country']
        exclude = ['user']

class PaymentForm(forms.Form):
    card_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '持卡人姓名'}), required=True)
    card_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '卡號'}), required=True)
    card_exp_date = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '有效期限'}), required=True)
    card_cvv_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '安全碼'}), required=True)
    card_address_1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '地址一'}), required=True)
    card_address_2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '地址二'}), required=False)
    card_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '卡片帳單城市'}), required=True)
    card_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '卡片帳單郵遞區號'}), required=True)
    card_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '卡片帳單國家'}), required=True)
