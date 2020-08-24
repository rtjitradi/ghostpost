# Generated by Django 3.1 on 2020-08-24 02:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoastsRoastsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_boast', models.BooleanField()),
                ('post_content', models.CharField(max_length=280)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('post_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('privatesecret_key', models.CharField(max_length=50)),
            ],
        ),
    ]
