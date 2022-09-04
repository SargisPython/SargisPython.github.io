from django.db import models
from django.contrib import admin




class WorkExperience(models.Model):
    image = models.ImageField(upload_to="image", null=True, blank=True)
    title = models.CharField(max_length=100, null=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True)
    skills1 = models.CharField(max_length=100, null=True, blank=True)
    percent = models.ForeignKey('Percents', on_delete=models.CASCADE, blank=True)
    skills2 = models.CharField(max_length=100, null=True, blank=True)
    percent1 = models.ForeignKey('Percents', on_delete=models.CASCADE, blank=True, related_name='percent_1')
    skills3 = models.CharField(max_length=100, null=True, blank=True)
    percent2 = models.ForeignKey('Percents', on_delete=models.CASCADE, blank=True, related_name='percent_2')
    #skills4 = models.CharField(max_length=100, null=True, blank=True)
    #percent3 = models.ForeignKey('Percents', on_delete=models.CASCADE, blank=True, related_name='percent_3')
    lang = models.ForeignKey('Lang', on_delete=models.CASCADE, blank=True, )
    ken = models.ForeignKey('Ken', on_delete=models.CASCADE, blank=True,null=True)
    lang2 = models.ForeignKey('Lang', on_delete=models.CASCADE, blank=True, related_name='lang_2')
    ken2 = models.ForeignKey('Ken', on_delete=models.CASCADE, blank=True, related_name='ken_2')
    lang3 = models.ForeignKey('Lang', on_delete=models.CASCADE, blank=True, related_name='lang_3')
    ken3 = models.ForeignKey('Ken', on_delete=models.CASCADE, blank=True, related_name='ken_3')
    work1 = models.TextField(blank=True)
    created1 = models.DateField(null=True, blank=True, max_length=100)
    work2 = models.TextField(blank=True)
    created2 = models.DateField(null=True, blank=True, max_length=100)
    work3 = models.TextField(blank=True)
    created3 = models.DateField(null=True, blank=True, max_length=100)
    Education1 = models.TextField(blank=True)
    created4 = models.DateField(null=True, blank=True, max_length=100)
    Education2 = models.TextField(blank=True)
    created5 = models.DateField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.title






class Lang(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'lang'
        verbose_name_plural = 'langes'
        ordering = ['id']


class Ken(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ken'
        verbose_name_plural = 'kens'
        ordering = ['id']


class Percents(models.Model):
    title = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title



class Social(models.Model):
    title=models.CharField(max_length=50)
    url=models.CharField(max_length=255)
    icon=models.ImageField(upload_to="icons")

    def __str__(self):
        return self.title








