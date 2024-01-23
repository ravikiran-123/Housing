# Generated by Django 4.2.7 on 2023-12-13 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('housingapp', '0068_remove_plotlikedproject_plotproject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housingexperts',
            name='Agent',
        ),
        migrations.RemoveField(
            model_name='housingexperts',
            name='expert_type',
        ),
        migrations.RemoveField(
            model_name='projectdetail',
            name='Experts',
        ),
        migrations.AddField(
            model_name='housingexperts',
            name='project_details',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='housingapp.projectdetail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='featuredcollections',
            name='feature_type',
            field=models.CharField(choices=[('Commercial', 'Commercial'), ('Rent', 'Rent'), ('Buy', 'Buy'), ('Plots', 'Plots'), ('Flatmate', 'Flatmate')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='flatmatechoice',
            name='flatmate_choices',
            field=models.CharField(choices=[('Girls', 'Girls'), ('Food Available', 'Food Available'), ('Private Room', 'Private Room'), ('Boys', 'Boys')], default='Boys', max_length=20),
        ),
        migrations.AlterField(
            model_name='floorplan',
            name='Configuration',
            field=models.CharField(choices=[('2BHK', '2BHK'), ('3BHK', '3BHK'), ('1BHK', '1BHK'), ('4BHK', '4BHK')], default='1BHK', max_length=20),
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