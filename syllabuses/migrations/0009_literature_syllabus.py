# Generated by Django 4.2.2 on 2023-06-10 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('syllabuses', '0008_alter_syllabus_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='literature',
            name='syllabus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='literature_set', to='syllabuses.syllabus', verbose_name='Силлабус'),
        ),
    ]