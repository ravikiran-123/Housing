# Generated by Django 4.2.7 on 2023-11-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingapp', '0025_remove_newsdetails_news_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetail',
            name='possession_status',
            field=models.CharField(choices=[('Ready to move', 'Ready to move'), ('In 3 years', 'In 3 years'), ('Beyond 3 years', 'Beyond 3 years')], default='Ready to move', max_length=20),
        ),
        migrations.AlterField(
            model_name='commercialprojectdetail',
            name='commercial_type',
            field=models.CharField(choices=[('Recently Added properties for sale', 'Recently Added properties for sale'), ('Recently Added properties for Rent', 'Recently Added properties for Rent')], default='Recently Added properties for sale', max_length=40),
        ),
        migrations.AlterField(
            model_name='featuredcollections',
            name='feature_type',
            field=models.CharField(choices=[('Flatmate', 'Flatmate'), ('Plots', 'Plots'), ('Buy', 'Buy'), ('Commercial', 'Commercial'), ('Rent', 'Rent')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='housingexperts',
            name='expert_type',
            field=models.CharField(choices=[('Flatmate', 'Flatmate'), ('Plots', 'Plots'), ('Buy', 'Buy'), ('Commercial', 'Commercial'), ('Rent', 'Rent')], default='Buy', max_length=20),
        ),
    ]