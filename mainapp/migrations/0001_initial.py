# Generated by Django 4.0.4 on 2022-05-05 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'ken',
                'verbose_name_plural': 'kens',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'lang',
                'verbose_name_plural': 'langes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Percents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='icons')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('title', models.CharField(max_length=100, null=True)),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('skills1', models.CharField(blank=True, max_length=100, null=True)),
                ('skills2', models.CharField(blank=True, max_length=100, null=True)),
                ('skills3', models.CharField(blank=True, max_length=100, null=True)),
                ('work1', models.TextField(blank=True)),
                ('created1', models.DateField(blank=True, max_length=100, null=True)),
                ('work2', models.TextField(blank=True)),
                ('created2', models.DateField(blank=True, max_length=100, null=True)),
                ('work3', models.TextField(blank=True)),
                ('created3', models.DateField(blank=True, max_length=100, null=True)),
                ('Education1', models.TextField(blank=True)),
                ('created4', models.DateField(blank=True, max_length=100, null=True)),
                ('Education2', models.TextField(blank=True)),
                ('created5', models.DateField(blank=True, max_length=100, null=True)),
                ('ken', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.ken')),
                ('ken2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ken_2', to='mainapp.ken')),
                ('ken3', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ken_3', to='mainapp.ken')),
                ('lang', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.lang')),
                ('lang2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lang_2', to='mainapp.lang')),
                ('lang3', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lang_3', to='mainapp.lang')),
                ('percent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.percents')),
                ('percent1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='percent_1', to='mainapp.percents')),
                ('percent2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='percent_2', to='mainapp.percents')),
            ],
        ),
    ]
