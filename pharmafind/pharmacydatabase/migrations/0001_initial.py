# Generated by Django 4.0.6 on 2022-07-24 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('milligrams', models.FloatField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacydatabase.brand')),
            ],
        ),
        migrations.CreateModel(
            name='DrugType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('contactemail', models.EmailField(blank=True, max_length=50, null=True)),
                ('website', models.CharField(blank=True, max_length=50, null=True)),
                ('delivery', models.BooleanField()),
                ('canimport', models.BooleanField()),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DrugSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacydatabase.drug')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacydatabase.pharmacy')),
            ],
        ),
        migrations.AddField(
            model_name='drug',
            name='drugtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacydatabase.drugtype'),
        ),
    ]
