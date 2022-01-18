# Generated by Django 3.2.4 on 2022-01-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[['MALE', 'Male'], ['FEMALE', 'Female']], max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.BigIntegerField(unique=True)),
                ('address', models.CharField(max_length=120, null=True)),
                ('ssc', models.IntegerField()),
                ('puc', models.IntegerField()),
                ('btech', models.IntegerField()),
                ('yop', models.IntegerField()),
                ('course', models.CharField(default='python full stack', max_length=50)),
                ('mock', models.IntegerField(default=2)),
            ],
        ),
    ]