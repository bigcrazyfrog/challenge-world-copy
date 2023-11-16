# Generated by Django 4.2.4 on 2023-08-24 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenges', '0002_achievement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='groups',
        ),
        migrations.AddField(
            model_name='challengegroup',
            name='challenges',
            field=models.ManyToManyField(blank=True, related_name='groups', to='challenges.challenge', verbose_name='Challenges'),
        ),
        migrations.AlterField(
            model_name='challengegroup',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='challenge_groups', to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
    ]
