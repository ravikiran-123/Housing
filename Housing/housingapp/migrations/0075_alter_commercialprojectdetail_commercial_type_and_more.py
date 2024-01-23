# Generated by Django 4.2.7 on 2023-12-14 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingapp', '0074_projectdetail_experts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercialprojectdetail',
            name='commercial_type',
            field=models.CharField(choices=[('Recently Added properties for sale', 'Recently Added properties for sale'), ('Recently Added properties for Rent', 'Recently Added properties for Rent')], default='Recently Added properties for sale', max_length=40),
        ),
        migrations.AlterField(
            model_name='featuredcollections',
            name='feature_type',
            field=models.CharField(choices=[('Plots', 'Plots'), ('Rent', 'Rent'), ('Commercial', 'Commercial'), ('Buy', 'Buy')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='flatmatechoice',
            name='flatmate_choices',
            field=models.CharField(choices=[('Food Available', 'Food Available'), ('Girls', 'Girls'), ('Boys', 'Boys'), ('Private Room', 'Private Room')], default='Boys', max_length=20),
        ),
        migrations.AlterField(
            model_name='floorplan',
            name='Configuration',
            field=models.CharField(choices=[('3BHK', '3BHK'), ('1BHK', '1BHK'), ('2BHK', '2BHK'), ('4BHK', '4BHK')], default='1BHK', max_length=20),
        ),
        migrations.AlterField(
            model_name='plotsprojectdetail',
            name='possession_status',
            field=models.CharField(choices=[('Beyond 3 years', 'Beyond 3 years'), ('Ready to move', 'Ready to move'), ('In 3 years', 'In 3 years')], default='Ready to move', max_length=20),
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='possession_status',
            field=models.CharField(choices=[('Beyond 3 years', 'Beyond 3 years'), ('Ready to move', 'Ready to move'), ('In 3 years', 'In 3 years')], default='Ready to move', max_length=20),
        ),
    ]
