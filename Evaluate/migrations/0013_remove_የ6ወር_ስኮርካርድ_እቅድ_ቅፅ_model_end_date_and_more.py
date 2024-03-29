# Generated by Django 4.2 on 2024-02-07 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Evaluate', '0012_alter_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_model_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='start_date',
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='d1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='d2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='m1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='m2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='y1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='y2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='መማርና_እድገት_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='መማርና_እድገት_10',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='መማርና_እድገት_11',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='መማርና_እድገት_12',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='መማርና_እድገት_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='መማርና_እድገት_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='መማርና_እድገት_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='መማርና_እድገት_5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='መማርና_እድገት_6',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='መማርና_እድገት_7',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='መማርና_እድገት_8',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='መማርና_እድገት_9',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='ተገልጋይ_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='ተገልጋይ_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='ተገልጋይ_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='የውስጥ_አሰራር_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='የውስጥ_አሰራር_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='የውስጥ_አሰራር_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='የውስጥ_አሰራር_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='የውስጥ_አሰራር_5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='የውስጥ_አሰራር_6',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='የውስጥ_አሰራር_7',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='ፋይናንስ_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='ፋይናንስ_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='ፋይናንስ_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='ፋይናንስ_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='ፋይናንስ_5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='ፋይናንስ_6',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='የሰራተኛው_ሙሉ_ስም',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='የስራ_መደቡ_መጠሪያ',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='የቅርብ_ኃላፊው_ሙሉ_ስም',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model',
            name='ደረጃ',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='demoModel',
        ),
    ]
