from django import forms
from register.models import User

class UserForm(forms.ModelForm):

    field_order = ['department','division','first_name','last_name']
    division = forms.CharField(label='課', widget=forms.TextInput(attrs={
        'placeholder':'例　営業一　経理二'
    }))
    class Meta:
        model = User
    
        fields = {'first_name','last_name','department','division', 'email'}
        labels = {'first_name':'苗字','last_name':'名前','department':'部署','division':'課'}

UserFormSet = forms.modelformset_factory(model=User, form=UserForm, extra=10, max_num=10)
