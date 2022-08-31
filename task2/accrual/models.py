from django.db import models
from datetime import datetime
from manage import init_django

init_django()

MONTH_CHOICES = (
    (1, "January"), (2, "February"),
    (3, "March"), (4, "April"),
    (5, "May"), (6, "June"),
    (7, "July"), (8, "August"),
    (9, "September"), (10, "October"),
    (11, "November"), (12, "Decemberry")
    )

class Accrual(models.Model):
    date = models.DateTimeField()
    month = models.PositiveSmallIntegerField(null=True, choices=MONTH_CHOICES)
    
    def save(self, *args, **kwargs):
        # достали месяц из даты
        self.month = datetime.strptime(self.date, "%Y-%m-%d").month
        super(Accrual, self).save(*args, **kwargs)
    

class Payment(models.Model):
    # связь один к одному из условий задачи
    accrual = models.OneToOneField(Accrual, null=True, on_delete=models.SET_NULL, related_name='payment')

    date = models.DateTimeField()
    month = models.PositiveSmallIntegerField(null=True, choices=MONTH_CHOICES)

    def save(self, *args, **kwargs):
        # месяц из даты
        self.month = datetime.strptime(self.date, "%Y-%m-%d").month

        try:

            # опущено условие про месяц, 
            # потому что условий про самый старый включает месяц
            # 1 - фильтруем по неоплаченным счетам
            # 2 - фильтруем по прошедшей дате
            # 3 - сортируем по дате
            # 4 - берём первое
            self.accrual = Accrual.objects.filter(payment=None, date__lte = self.date).order_by('date').last()
            super(Payment, self).save()
        
        except Exception as e:
            # если возникло исключение оставляем пустым
            self.accrual = None
        super(Payment, self).save()
 
