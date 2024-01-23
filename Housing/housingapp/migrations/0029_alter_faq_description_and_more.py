# Generated by Django 4.2.7 on 2023-11-14 09:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housingapp', '0028_alter_commercialprojectdetail_commercial_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='Description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='featuredcollections',
            name='feature_type',
            field=models.CharField(choices=[('Commercial', 'Commercial'), ('Buy', 'Buy'), ('Plots', 'Plots'), ('Flatmate', 'Flatmate'), ('Rent', 'Rent')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='flatmatechoice',
            name='flatmate_choices',
            field=models.CharField(choices=[('Food Available', 'Food Available'), ('Boys', 'Boys'), ('Private Room', 'Private Room'), ('Girls', 'Girls')], default='Boys', max_length=20),
        ),
        migrations.AlterField(
            model_name='housingexperts',
            name='expert_type',
            field=models.CharField(choices=[('Commercial', 'Commercial'), ('Buy', 'Buy'), ('Plots', 'Plots'), ('Flatmate', 'Flatmate'), ('Rent', 'Rent')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='possession_status',
            field=models.CharField(choices=[('Ready to move', 'Ready to move'), ('In 3 years', 'In 3 years'), ('Beyond 3 years', 'Beyond 3 years')], default='Ready to move', max_length=20),
        ),
    ]
