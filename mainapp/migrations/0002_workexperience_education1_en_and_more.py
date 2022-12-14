# Generated by Django 4.0.4 on 2022-05-07 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='Education1_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='Education1_hy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='Education1_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='Education2_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='Education2_hy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='Education2_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='country_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='country_hy',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='country_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='ken2_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ken_2', to='mainapp.ken'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='ken2_hy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ken_2', to='mainapp.ken'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='ken2_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ken_2', to='mainapp.ken'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='ken3_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ken_3', to='mainapp.ken'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='ken3_hy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ken_3', to='mainapp.ken'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='ken3_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ken_3', to='mainapp.ken'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='ken_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.ken'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='ken_hy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.ken'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='ken_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.ken'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='lang2_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lang_2', to='mainapp.lang'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='lang2_hy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lang_2', to='mainapp.lang'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='lang2_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lang_2', to='mainapp.lang'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='lang3_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lang_3', to='mainapp.lang'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='lang3_hy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lang_3', to='mainapp.lang'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='lang3_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lang_3', to='mainapp.lang'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='lang_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.lang'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='lang_hy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.lang'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='lang_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.lang'),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='profession_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='profession_hy',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='profession_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='skills1_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='skills1_hy',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='skills1_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='skills2_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='skills2_hy',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='skills2_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='skills3_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='skills3_hy',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='skills3_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='title_hy',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='work1_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='work1_hy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='work1_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='work2_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='work2_hy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='work2_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='work3_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='work3_hy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='work3_ru',
            field=models.TextField(blank=True, null=True),
        ),
    ]
