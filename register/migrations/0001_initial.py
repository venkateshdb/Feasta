# Generated by Django 3.0.4 on 2020-03-30 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='authapp.CustomUser')),
                ('location', models.CharField(blank=True, help_text='Location of User.', max_length=100, verbose_name='location')),
                ('address', models.CharField(blank=True, help_text='Address of User.', max_length=150, verbose_name='address')),
                ('profile_pic', models.ImageField(blank=True, help_text='Profile pictures of Users', upload_to='profile pics', verbose_name='profile image')),
            ],
            options={
                'abstract': False,
            },
            bases=('authapp.customuser',),
        ),
    ]
