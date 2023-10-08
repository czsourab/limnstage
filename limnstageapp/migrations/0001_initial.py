# Generated by Django 2.1.5 on 2019-02-03 08:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('images', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='limn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=500)),
                ('body', models.TextField()),
                ('limntype', models.CharField(max_length=30)),
                ('subjects', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='limnanswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=500)),
                ('answer', models.TextField()),
                ('limnid', models.IntegerField()),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='userform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('fullname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=200)),
                ('profilepic', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
