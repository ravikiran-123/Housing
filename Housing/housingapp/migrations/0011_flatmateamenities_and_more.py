# Generated by Django 4.1 on 2023-10-27 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('housingapp', '0010_flatmateassistance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatmateAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Amenities_images')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('flatmate_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housingapp.flatmateprojectdetail')),
            ],
        ),
        migrations.AlterField(
            model_name='flatmatechoice',
            name='flatmate_choices',
            field=models.CharField(choices=[('Girls', 'Girls'), ('Boys', 'Boys'), ('Food Available', 'Food Available'), ('Private Room', 'Private Room')], default='Boys', max_length=20),
        ),
        migrations.DeleteModel(
            name='FlatmateAssistance',
        ),
    ]