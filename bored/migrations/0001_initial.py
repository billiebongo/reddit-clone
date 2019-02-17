# Generated by Django 2.0.10 on 2019-02-17 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('username', models.EmailField(max_length=254, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('password_recently_reset', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActivationToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=40, verbose_name='Activation Token')),
                ('status', models.CharField(choices=[('A', 'ACTIVE'), ('E', 'EXPIRED')], default='A', max_length=1)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokenuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=20)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=40, verbose_name='Activation Token')),
                ('text', models.CharField(max_length=40, verbose_name='Activation Token')),
                ('tags', models.CharField(max_length=40, verbose_name='Activation Token')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=40, verbose_name='Activation Token')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bored.Location'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]