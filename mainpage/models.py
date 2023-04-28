from django.db import models

class Form(models.Model):
    fullname = models.CharField("ФИО", max_length = 100)
    phone = models.CharField("Телефон", max_length = 15)
    time = models.TimeField("Время")
    date = models.DateField("Дата")
    location = models.CharField("Локация", max_length = 20)
    rate = models.CharField("Тариф", max_length = 20)

    def __str__(self):
        return self.fullname
