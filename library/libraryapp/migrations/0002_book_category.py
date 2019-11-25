# Generated by Django 2.2.7 on 2019-11-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(help_text='enter name of book', max_length=100)),
                ('book_price', models.CharField(help_text='enter price of book', max_length=100)),
                ('book_isbn_Num', models.CharField(help_text='enter isbn number', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(help_text='enter Book category', max_length=100)),
            ],
        ),
    ]