from django.db import models


class Student(models.Model):
    full_name = models.CharField('ФИО', max_length=250)
    birth_date = models.DateField()
    performance = models.CharField('Успеваемость', max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
