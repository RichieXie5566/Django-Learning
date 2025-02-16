from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'輸入您的電子郵件'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'您的名'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'您的姓'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = '輸入帳號'
		self.fields['username'].label = '' #指定的視窗中顯示的文字和圖像
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>必填。150個字符或更少。僅限字母、數字和@/./+/-/_。</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = '輸入密碼'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>您的密碼不能與其他個人信息過於相似。</li><li>您的密碼必須包含至少8個字符。</li><li>您的密碼不能是常用的密碼。</li><li>您的密碼不能完全是數字。</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = '確認密碼'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>再輸入一次密碼</small></span>'

class UpdateUserForm(UserChangeForm):
	password = None # 隱藏密碼的區域
	
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'電子郵件'}), required=False)
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'您的名'}), required=False)
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'您的姓'}), required=False)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def __init__(self, *args, **kwargs):
		super(UpdateUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = '輸入帳號'
		self.fields['username'].label = '' #指定的視窗中顯示的文字和圖像
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>必填。150個字符或更少。僅限字母、數字和@/./+/-/_。</small></span>'

class ChangePasswordForm(SetPasswordForm):
	class META:
		model = User
		fields = ['new_password1', 'new_password2']
	
	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = '輸入密碼'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>您的密碼不能與其他個人信息過於相似。</li><li>您的密碼必須包含至少8個字符。</li><li>您的密碼不能是常用的密碼。</li><li>您的密碼不能完全是數字。</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = '確認密碼'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>再輸入一次密碼</small></span>'

class UserInfoForm(forms.ModelForm):

    phone = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'電話號碼'}), required=False)
    address1 = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'地址第一行'}), required=True)
    address2 = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'地址第二行'}), required=False)
    city = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'城市'}), required=True)
    zipcode = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'郵遞區號'}), required=True)
    country = forms.CharField(label = "", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'國家'}), required=True)

    class Meta:
        model = Profile
        fields = ('phone', 'address1', 'address2', 'city', 'zipcode', 'country')
