# Generated by Django 3.0.6 on 2020-05-18 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketDictionary', '0004_auto_20200518_1608'),
        ('dailyAnalysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_analysis', models.DateField()),
                ('header', models.TextField()),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=250, unique_for_date='date_analysis')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('analysis_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dailyAnalysis.AnalysisType')),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketDictionary.Ticker')),
            ],
        ),
        migrations.DeleteModel(
            name='Paragraph',
        ),
    ]
