# Generated by Django 3.2.4 on 2021-07-20 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_petstagramuser_date_joined'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('image_url', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.petstagramuser')),
            ],
        ),
    ]