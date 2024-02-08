# Generated by Django 4.2 on 2024-02-08 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Evaluate', '0014_remove_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_model_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='የድርጊት_መርሃ_ግብር_ቅፅ_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('የሰራተኛው_ሙሉ_ስም', models.CharField(blank=True, max_length=100, null=True)),
                ('የቅርብ_ኃላፊው_ሙሉ_ስም', models.CharField(blank=True, max_length=100, null=True)),
                ('የስራ_መደቡ_መጠሪያ', models.CharField(blank=True, max_length=100, null=True)),
                ('ደረጃ', models.CharField(blank=True, max_length=100, null=True)),
                ('d1', models.IntegerField(null=True)),
                ('d2', models.IntegerField(null=True)),
                ('m1', models.IntegerField(null=True)),
                ('m2', models.IntegerField(null=True)),
                ('y1', models.IntegerField(null=True)),
                ('y2', models.IntegerField(null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='start_date',
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='d1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='d2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='m1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='m2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='value1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='value10',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='value2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='value3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='value4',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='value5',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='value6',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='value7',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='value8',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='value9',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='y1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model',
            name='y2',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
