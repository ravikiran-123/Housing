# Generated by Django 4.2.7 on 2023-11-14 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('housingapp', '0026_projectdetail_possession_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='commercialprojectdetail',
            name='commercial_type',
            field=models.CharField(choices=[('Recently Added properties for Rent', 'Recently Added properties for Rent'), ('Recently Added properties for sale', 'Recently Added properties for sale')], default='Recently Added properties for sale', max_length=40),
        ),
        migrations.AlterField(
            model_name='featuredcollections',
            name='feature_type',
            field=models.CharField(choices=[('Flatmate', 'Flatmate'), ('Rent', 'Rent'), ('Plots', 'Plots'), ('Buy', 'Buy'), ('Commercial', 'Commercial')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='flatmatechoice',
            name='flatmate_choices',
            field=models.CharField(choices=[('Private Room', 'Private Room'), ('Food Available', 'Food Available'), ('Girls', 'Girls'), ('Boys', 'Boys')], default='Boys', max_length=20),
        ),
        migrations.AlterField(
            model_name='housingexperts',
            name='expert_type',
            field=models.CharField(choices=[('Flatmate', 'Flatmate'), ('Rent', 'Rent'), ('Plots', 'Plots'), ('Buy', 'Buy'), ('Commercial', 'Commercial')], default='Buy', max_length=20),
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='possession_status',
            field=models.CharField(choices=[('In 3 years', 'In 3 years'), ('Beyond 3 years', 'Beyond 3 years'), ('Ready to move', 'Ready to move')], default='Ready to move', max_length=20),
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
        migrations.AddField(
            model_name='faq',
            name='project_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housingapp.projectdetail'),
        ),
    ]