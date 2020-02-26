# Generated by Django 2.2.10 on 2020-02-25 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(blank=True, max_length=10, verbose_name='last name')),
                ('division_name', models.CharField(blank=True, max_length=30, verbose_name='department')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(choices=[('営業', '営業部'), ('経理', '経理部'), ('人事', '人事部'), ('IT', 'IT部')], default='営業部', max_length=5),
        ),
    ]