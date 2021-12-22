# Generated by Django 3.2.9 on 2021-12-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField()),
                ('attachment', models.FileField(upload_to='file_data/')),
            ],
            options={
                'db_table': 'faqs',
            },
        ),
    ]