# Generated by Django 4.2.9 on 2024-02-06 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Evaluate', '0008_remove_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_model_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_model',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
