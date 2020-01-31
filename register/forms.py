from django.contrib.auth.forms import (
    AuthenticationForm
)
from django import forms

class LoginForm(AuthenticationForm):

    error_messages = {'invalid_login':'入力された情報ではログインできませんでした。もう一度入力内容をお確かめください。'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = forms.EmailField(label='e-mailアドレス')

    def clean_password(self):
        password = self.cleaned_data['password']
        for letter in password:
            if letter.islower() or letter.isdigit():
                return password
        print('heres error')
        raise forms.ValidationError('Caps Lockキーがオンになっていませんか？ ')
