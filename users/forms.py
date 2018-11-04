from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from snowpenguin.django.recaptcha2.widgets import ReCaptchaHiddenInput
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # firstname = forms.CharField()
    # lastname = forms.CharField()
    email = forms.EmailField()
    # captcha = ReCaptchaField(widget=ReCaptchaHiddenInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # add  `captcha, firstname, lastname`  fields


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
