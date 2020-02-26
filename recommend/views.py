from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from register.models import User
from recommend.models import Excellent_Man
from django.urls import reverse
from django.shortcuts import redirect
from .forms import ManForm, AddInformationForm
from django.core.mail import BadHeaderError, send_mail
from post_mail.forms import UserForm
# Create your views here.

def information(request):
    if request.method == 'POST':
        form = ManForm(request.POST)
        if form.is_valid():
            excellent_Man = form.save(commit=False)
            excellent_Man.who_recommend = request.user
            excellent_Man.save()
            message = 'ご紹介ありがとうございました'
            form = ManForm
            return render(request, 'recommend/guest_page.html', {'message':message, 'form':form})
        else:
            return render(request, 'recommend/guest_page.html', {'form':form})

    form = ManForm
    recommended_man = Excellent_Man.objects.all()
    context = {
    'form':form,
    'addform':AddInformationForm,
    'recommended_man':recommended_man
    }
    return render(request, 'recommend/guest_page.html', context)



@login_required
def add_user(request, id):
    man = Excellent_Man.objects.get(id=id)
    message = make_mail(request, man)

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()
            mail(password, user.email, message)
            return redirect('/')

    form = UserForm
    context = {'man':man, 'message':message, 'form':form}
    return render(request, "recommend/man_information.html", context)


def add_more_information(request, id):
    man = Excellent_Man.objects.get(id=id)
    form = AddInformationForm(request.POST)
    if form.is_valid():
        man.more_information += ' '+ form.cleaned_data.get("more_information")
        man.save()
        return redirect('/')


def make_mail(request, man):
    return f'{man.who_recommend.division} {man.who_recommend.first_name}さんから、{man.company} {man.name}さんを紹介いただきました。そこで、システムにログインいただき、{man.who_recommend.first_name}さんの情報に、ご存知な情報を追加いただけないでしょうか？どうぞよろしくお願いします'

def mail(password, to, message):
    """題名"""
    subject = "情報提供のお願い"
    """本文"""

    m = message + ' パスワード ' + password + ' ログインＵＲＬ' + 'http://127.0.0.1:8000/'
    """送信元メールアドレス"""
    from_email = ''
    """宛先メールアドレス"""
    recipient_list = [
        to
    ]

    send_mail(subject, m, from_email, recipient_list)
