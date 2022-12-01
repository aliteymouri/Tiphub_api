from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import PasswordChangeForm
from django.forms import ValidationError
from .models import User
from django import forms


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='گذرواژه ',
                               widget=forms.PasswordInput({"placeholder": "گذرواژه", "id": "pass"}))
    confirm_password = forms.CharField(label='تایید گذرواژه ',
                                       widget=forms.PasswordInput(
                                           {"placeholder": "تایید گذرواژه", "id": "confirm_pass"}))

    class Meta:
        model = User
        fields = ('email', 'fullname', 'phone', 'password')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError("رمزعبور مشابه نیست")
        elif len(password and confirm_password) < 8:
            raise ValidationError("رمز عبور وارد شده کمتر از 8 کاراکتر میباشد")
        return confirm_password

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 11:
            raise ValidationError("یک شماره تماس معتبر وارد کنید")
        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="برای تغییر گذرواژه <a href=\"../password/\">کلیک کنید</a>"
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 11:
            raise ValidationError("یک شماره تماس معتبر وارد کنید")
        return phone

    class Meta:
        model = User
        fields = ('email', 'fullname', 'phone', 'password', 'bio', 'image', 'is_active', 'is_admin')
