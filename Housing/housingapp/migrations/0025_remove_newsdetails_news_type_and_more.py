# Generated by Django 4.2.7 on 2023-11-10 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingapp', '0024_rename_banner_image_banner_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsdetails',
            name='news_type',
        ),
        migrations.AlterField(
            model_name='developerdetails',
            name='developer_type',
            field=models.CharField(choices=[('Plots', 'Plots'), ('Buy', 'Buy')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='featuredcollections',
            name='feature_type',
            field=models.CharField(choices=[('Flatmate', 'Flatmate'), ('Commercial', 'Commercial'), ('Buy', 'Buy'), ('Plots', 'Plots'), ('Rent', 'Rent')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='flatmatechoice',
            name='flatmate_choices',
            field=models.CharField(choices=[('Private Room', 'Private Room'), ('Food Available', 'Food Available'), ('Boys', 'Boys'), ('Girls', 'Girls')], default='Boys', max_length=20),
        ),
        migrations.AlterField(
            model_name='housingexperts',
            name='expert_type',
            field=models.CharField(choices=[('Flatmate', 'Flatmate'), ('Commercial', 'Commercial'), ('Buy', 'Buy'), ('Plots', 'Plots'), ('Rent', 'Rent')], default='Buy', max_length=20),
        ),
    ]