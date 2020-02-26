from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class Excellent_Man(models.Model):
    who_recommend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='名前', max_length=20)
    company = models.CharField(verbose_name='勤務先', max_length=20)
   
    REASON_CHOICES = [
          ('転職を検討していたから（給料の不満)', '転職を検討していたから（給料の不満）'),
          ('転職を検討していたから（昇進への不満)', '転職を検討していたから（昇進への不満）'),
          ('転職を検討していたから（会社方針の不満)', '転職を検討していたから（会社方針の不満）'),

    ]
    reason = models.CharField(
        verbose_name='推薦理由',
        max_length=100,
        choices=REASON_CHOICES,
        default="転職を検討していたから（給料の不満",
    )
    phone_number = models.CharField(verbose_name='電話番号', max_length=11, blank=True)
    email = models.EmailField(verbose_name='emailアドレス', blank=True)
    more_information = models.TextField(verbose_name='詳細',)
    created_date = models.DateTimeField(verbose_name='登録日', default=timezone.now)
