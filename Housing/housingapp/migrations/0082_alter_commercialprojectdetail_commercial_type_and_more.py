# Generated by Django 5.0 on 2023-12-14 09:51

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingapp', '0081_alter_featuredcollections_feature_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercialprojectdetail',
            name='commercial_type',
            field=models.CharField(choices=[('Recently Added properties for sale', 'Recently Added properties for sale'), ('Recently Added properties for Rent', 'Recently Added properties for Rent')], default='Recently Added properties for sale', max_length=40),
        ),
        migrations.AlterField(
            model_name='developerdetails',
            name='developer_type',
            field=models.CharField(choices=[('Buy', 'Buy'), ('Plots', 'Plots')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='featuredcollections',
            name='feature_type',
            field=models.CharField(choices=[('Buy', 'Buy'), ('Rent', 'Rent'), ('Plots', 'Plots'), ('Commercial', 'Commercial')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='flatmatechoice',
            name='flatmate_choices',
            field=models.CharField(choices=[('Private Room', 'Private Room'), ('Boys', 'Boys'), ('Girls', 'Girls'), ('Food Available', 'Food Available')], default='Boys', max_length=20),
        ),
        migrations.AlterField(
            model_name='floorplan',
            name='Configuration',
            field=models.CharField(choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('4BHK', '4BHK'), ('3BHK', '3BHK')], default='1BHK', max_length=20),
        ),
        migrations.AlterField(
            model_name='housingexperts',
            name='expert_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Buy', 'Buy'), ('Rent', 'Rent'), ('Plots', 'Plots'), ('Commercial', 'Commercial')], default=[], max_length=2048),
        ),
        migrations.AlterField(
            model_name='plotsprojectdetail',
            name='possession_status',
            field=models.CharField(choices=[('Ready to move', 'Ready to move'), ('In 3 years', 'In 3 years'), ('Beyond 3 years', 'Beyond 3 years')], default='Ready to move', max_length=20),
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='possession_status',
            field=models.CharField(choices=[('Ready to move', 'Ready to move'), ('In 3 years', 'In 3 years'), ('Beyond 3 years', 'Beyond 3 years')], default='Ready to move', max_length=20),
        ),
    ]
