# Generated by Django 4.1 on 2023-10-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingapp', '0003_alter_flatmatechoice_flatmate_choices'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FlatmateAmenities',
            new_name='FlatmateServices',
        ),
        migrations.AlterField(
            model_name='featuredcollections',
            name='feature_type',
            field=models.CharField(choices=[('Buy', 'Buy'), ('Plots', 'Plots'), ('Commercial', 'Commercial'), ('Rent', 'Rent')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='flatmatechoice',
            name='flatmate_choices',
            field=models.CharField(choices=[('Food Available', 'Food Available'), ('Girls', 'Girls'), ('Private Room', 'Private Room'), ('Boys', 'Boys')], default='Boys', max_length=20),
        ),
        migrations.AlterField(
            model_name='housingexperts',
            name='expert_type',
            field=models.CharField(choices=[('Buy', 'Buy'), ('Plots', 'Plots'), ('Commercial', 'Commercial'), ('Rent', 'Rent')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='newsdetails',
            name='news_type',
            field=models.CharField(choices=[('Buy', 'Buy'), ('Plots', 'Plots'), ('Commercial', 'Commercial'), ('Rent', 'Rent')], default='Buy', max_length=20),
        ),
    ]
