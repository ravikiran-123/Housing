# Generated by Django 4.2.7 on 2023-12-13 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('housingapp', '0067_rename_project_plotlikedproject_plotproject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plotlikedproject',
            name='plotproject',
        ),
        migrations.AddField(
            model_name='plotlikedproject',
            name='project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='housingapp.plotsprojectdetail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commerciallikedproject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housingapp.commercialprojectdetail'),
        ),
        migrations.AlterField(
            model_name='commercialprojectdetail',
            name='commercial_type',
            field=models.CharField(choices=[('Recently Added properties for sale', 'Recently Added properties for sale'), ('Recently Added properties for Rent', 'Recently Added properties for Rent')], default='Recently Added properties for sale', max_length=40),
        ),
        migrations.AlterField(
            model_name='featuredcollections',
            name='feature_type',
            field=models.CharField(choices=[('Plots', 'Plots'), ('Buy', 'Buy'), ('Flatmate', 'Flatmate'), ('Rent', 'Rent'), ('Commercial', 'Commercial')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='flatmatechoice',
            name='flatmate_choices',
            field=models.CharField(choices=[('Boys', 'Boys'), ('Food Available', 'Food Available'), ('Private Room', 'Private Room'), ('Girls', 'Girls')], default='Boys', max_length=20),
        ),
        migrations.AlterField(
            model_name='floorplan',
            name='Configuration',
            field=models.CharField(choices=[('3BHK', '3BHK'), ('4BHK', '4BHK'), ('1BHK', '1BHK'), ('2BHK', '2BHK')], default='1BHK', max_length=20),
        ),
        migrations.AlterField(
            model_name='housingexperts',
            name='expert_type',
            field=models.CharField(choices=[('Plots', 'Plots'), ('Buy', 'Buy'), ('Flatmate', 'Flatmate'), ('Rent', 'Rent'), ('Commercial', 'Commercial')], default='Buy', max_length=20),
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
