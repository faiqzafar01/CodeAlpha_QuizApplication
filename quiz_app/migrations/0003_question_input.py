# Generated by Django 4.2.5 on 2023-09-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_alter_question_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='input',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
