from django import forms
from register.models import User



class IntroduceForm(forms.Form):
    name = forms.CharField(
        label='名前',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )


    company = forms.CharField(
        label='勤め先',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )

    phone_number = forms.CharField(
        label='電話番号',
        required=False,
    )

    email = forms.EmailField(
    label = 'emailアドレス',
    required= False,
    )

    reason = forms.fields.ChoiceField(
        label = '推薦理由',
        choices = (
            ('転職を検討していたから（給料の不満）', '転職を検討していたから（給料の不満）'),
            ('転職を検討していたから（昇進への不満）', '転職を検討していたから（昇進への不満）'),
            ('転職を検討していたから（会社方針の不満）', '転職を検討していたから（会社方針の不満）'),

        ),
        required=True,
        widget=forms.widgets.Select
    )

    more_information = forms.CharField(
    label = '人事部へ提供できる情報',
    required = False,
    widget = forms.Textarea()
    )

    def clean(self):
        email = self.cleaned_data.get('email')
        phone_number = self.cleaned_data.get('phone_number')

        if not (email or phone_number):
            raise forms.ValidationError('emailアドレスか電話番号のどちらかの入力が必要です。')

class AddInformationForm(forms.Form):
    more_information = forms.CharField(
    label = '人事部へ提供できる情報',
    required = False,
    widget = forms.Textarea()
    )
