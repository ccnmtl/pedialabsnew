# Generated by Django 3.2.23 on 2023-12-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionplanresponse',
            name='action_plan',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='actionplanresponse',
            name='assessment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='lab',
            name='correct_actionplan',
            field=models.CharField(choices=[('Situation urgent. Call or admit patient immediately', 'Situation urgent. Call or admit patient immediately'), ('Situation needs follow-up. Call patient within a week', 'Situation needs follow-up. Call patient within a week'), ('Flag for review at following visit', 'Flag for review at following visit'), ("Call patient's mother to say the results were normal", "Call patient's mother to say the results were normal"), ('Prescribe treatment', 'Prescribe treatment'), ('Refer for further tests', 'Refer for further tests'), ('Reassure and send home', 'Reassure and send home')], default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='test',
            name='abnormality',
            field=models.CharField(default='none', max_length=256),
        ),
        migrations.AlterField(
            model_name='test',
            name='result_level',
            field=models.CharField(choices=[('unselected', 'Please select:'), ('low', 'Low'), ('normal', 'Normal'), ('high', 'High')], default='normal', max_length=256),
        ),
        migrations.AlterField(
            model_name='testresponse',
            name='abnormality',
            field=models.CharField(default='none', max_length=256),
        ),
        migrations.AlterField(
            model_name='testresponse',
            name='result_level',
            field=models.CharField(choices=[('unselected', 'Please select:'), ('low', 'Low'), ('normal', 'Normal'), ('high', 'High')], max_length=256),
        ),
    ]