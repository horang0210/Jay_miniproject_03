# Generated by Django 5.1.4 on 2024-12-19 07:28

import django.contrib.auth.password_validation
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0006_alter_userinfo_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="password",
            field=models.CharField(
                error_messages={"password": "양식에 맞는 비밀번호로 다시 만들어주세요."},
                help_text="최소 8자 이상으로 만들어주세요",
                max_length=150,
                validators=[
                    django.contrib.auth.password_validation.MinimumLengthValidator
                ],
            ),
        ),
    ]