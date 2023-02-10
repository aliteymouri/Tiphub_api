from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import ValidationError
from .models import User
from django import forms


def validate_phone(value):
    if value[:2] != "09" or len(value) < 11:
        raise forms.ValidationError('یک شماره تماس معتبر وارد کنید', code='start_with_09')
    try:
        int(value)
    except:
        raise forms.ValidationError('یک شماره تماس معتبر وارد کنید', code='start_with_09')


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='گذرواژه ',
                               widget=forms.PasswordInput({"placeholder": "گذرواژه"}))
    confirm_password = forms.CharField(label='تایید گذرواژه ',
                                       widget=forms.PasswordInput(
                                           {"placeholder": "تایید گذرواژه", }))
    phone = forms.CharField(
        widget=forms.TextInput({'maxlength': 11}),
        validators=[validate_phone]
    )

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
    phone = forms.CharField(
        widget=forms.TextInput({'maxlength': 11}),
        validators=[validate_phone]
    )

    class Meta:
        model = User
        fields = ('email', 'fullname', 'phone', 'password', 'bio', 'image', 'is_active', 'is_admin')
