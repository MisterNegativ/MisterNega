# Generated by Django 4.2 on 2023-04-16 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('syllabuses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='literature',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='literature_set', to='syllabuses.course', verbose_name='Дисциплина'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='agreed_with',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='syllabuses.director', verbose_name='Согласовывает: '),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='syllabuses.course', verbose_name='Дисциплина'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='format_of_training',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='syllabuses.format', verbose_name='Формат обучения'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='instructor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='syllabuses.customuser', verbose_name='Инструктор/Преподаватель'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='language_of_education',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='syllabuses.language', verbose_name='Язык обучения'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='proficiency_level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='syllabuses.proficiency', verbose_name='Уровень владения языком'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='training_level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='syllabuses.edulevel', verbose_name='Уровень обучения'),
        ),
    ]
