# Generated by Django 5.2.3 on 2025-06-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiProj', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='characterstats',
            old_name='ATK',
            new_name='base_ATK',
        ),
        migrations.RenameField(
            model_name='characterstats',
            old_name='DEF',
            new_name='base_DEF',
        ),
        migrations.RenameField(
            model_name='characterstats',
            old_name='HP',
            new_name='base_HP',
        ),
        migrations.RenameField(
            model_name='characterstats',
            old_name='critRate',
            new_name='rarity',
        ),
        migrations.RemoveField(
            model_name='characterstats',
            name='ER',
        ),
        migrations.RemoveField(
            model_name='characterstats',
            name='critDMG',
        ),
        migrations.AddField(
            model_name='characterstats',
            name='bATKDMG',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='base_ER',
            field=models.FloatField(default=100.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='base_critDMG',
            field=models.FloatField(default=150.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='base_critRate',
            field=models.FloatField(default=5.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='elemDMG',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='element',
            field=models.CharField(default='Temp', max_length=100),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='hATKDMG',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='healBONUS',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='rLibDMG',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='rSkillDMG',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='trace_ATK',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='trace_DEF',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='trace_HP',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='trace_critDMG',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='trace_critRate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='trace_elemDMG',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='trace_healBONUS',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='weapon',
            field=models.CharField(default='Temp', max_length=100),
        ),
    ]
