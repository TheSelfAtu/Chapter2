from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from register.models import User
from recommend.models import Excellent_Man
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .forms import UserFormSet
from django.core.mail import BadHeaderError, send_mail


@login_required
def show_mypage(request):
    if request.user.is_staff :
        users = User.objects.exclude(is_staff=True)
        recommended = Excellent_Man.objects.all()
        context = {
        'users':users,
        'recommended':recommended
        }
        return render(request, 'post_mail/staff_page.html', context)

    url = reverse_lazy('recommend:information')
    return redirect(url)

@login_required
def add_guest(request):
    if request.method == 'POST':
        formset = UserFormSet(request.POST)
        for form in formset:
            if form.is_valid :
                user = form.save(commit=False)
                if user.email:
                    password = User.objects.make_random_password()
                    mail(request, user.email, password)
                    user.set_password(password)
                    user.save()
        return redirect('/')

    formset = UserFormSet(queryset=User.objects.none())
    return render(request, 'post_mail/send_mail.html', {'formset':formset})



def mail(request, to, password):
    """題名"""
    subject = "紹介のお願い"
    """本文"""
    message = 'いつも優秀な人材を紹介してくれてありがとうございます。これからも、我が社に入ってくれそうな人材をぜひともご紹介ください。 List of Excellent Young-man は、みなさんから人事部に紹介してもいいと思った人たちを登録いただくシステムです。もし人事部から連絡してもよい優秀な方がいらっしゃいましたら、ぜひご登録をお願いします。' +' パスワード'+password + ' ログインURL' + ' http://127.0.0.1:8000/'

    """送信元メールアドレス"""
    from_email = ""
    """宛先メールアドレス"""
    recipient_list = [
        to
    ]

    send_mail(subject, message, from_email, recipient_list)
