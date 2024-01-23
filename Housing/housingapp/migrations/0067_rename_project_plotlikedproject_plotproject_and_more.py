# Generated by Django 4.2.7 on 2023-12-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingapp', '0066_rename_plotproject_plotlikedproject_project_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plotlikedproject',
            old_name='project',
            new_name='plotproject',
        ),
        migrations.AlterField(
            model_name='commercialprojectdetail',
            name='commercial_type',
            field=models.CharField(choices=[('Recently Added properties for Rent', 'Recently Added properties for Rent'), ('Recently Added properties for sale', 'Recently Added properties for sale')], default='Recently Added properties for sale', max_length=40),
        ),
        migrations.AlterField(
            model_name='developerdetails',
            name='developer_type',
            field=models.CharField(choices=[('Plots', 'Plots'), ('Buy', 'Buy')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='featuredcollections',
            name='feature_type',
            field=models.CharField(choices=[('Rent', 'Rent'), ('Commercial', 'Commercial'), ('Flatmate', 'Flatmate'), ('Buy', 'Buy'), ('Plots', 'Plots')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='flatmatechoice',
            name='flatmate_choices',
            field=models.CharField(choices=[('Food Available', 'Food Available'), ('Boys', 'Boys'), ('Private Room', 'Private Room'), ('Girls', 'Girls')], default='Boys', max_length=20),
        ),
        migrations.AlterField(
            model_name='floorplan',
            name='Configuration',
            field=models.CharField(choices=[('2BHK', '2BHK'), ('4BHK', '4BHK'), ('1BHK', '1BHK'), ('3BHK', '3BHK')], default='1BHK', max_length=20),
        ),
        migrations.AlterField(
            model_name='housingexperts',
            name='expert_type',
            field=models.CharField(choices=[('Rent', 'Rent'), ('Commercial', 'Commercial'), ('Flatmate', 'Flatmate'), ('Buy', 'Buy'), ('Plots', 'Plots')], default='Buy', max_length=20),
        ),
    ]