from datetime import datetime
from accrual.models import Payment, Accrual
from django.db import transaction, DatabaseError

# bulk_create не работает ожидаемым образом
# метод не вызывает save()
# Accrual.objects.bulk_create([
#                 Accrual(**{'date' : datetime.fromisoformat('2019-12-10')}),
#                 Accrual(**{'date' : datetime.fromisoformat('2010-12-04')}),
#                 ...........................................................
#                 Accrual(**{'date' : datetime.fromisoformat('2019-05-04')})])

Accrual.objects.all().delete()
Payment.objects.all().delete()
try:
    with transaction.atomic():
        # accruals
        Accrual.objects.create(**{'date' : '2019-12-10'})
        Accrual.objects.create(**{'date' : '2010-12-04'})
        Accrual.objects.create(**{'date' : '2019-12-04'})
        Accrual.objects.create(**{'date' : '2022-05-01'})
        Accrual.objects.create(**{'date' : '1999-01-01'})
        Accrual.objects.create(**{'date' : '2023-06-04'})
        Accrual.objects.create(**{'date' : '2019-05-04'})
        # payments 
        Payment.objects.create(**{'date' : '2019-03-10'})
        Payment.objects.create(**{'date' : '2010-12-04'})
        Payment.objects.create(**{'date' : '2019-12-04'})
        Payment.objects.create(**{'date' : '2022-04-01'})
        Payment.objects.create(**{'date' : '2022-04-01'})
        Payment.objects.create(**{'date' : '2022-04-01'})
        Payment.objects.create(**{'date' : '2022-04-01'})
        Payment.objects.create(**{'date' : '2022-04-01'})
except DatabaseError as e:
    print(e)


accruals = Accrual.objects.all()
payments = Payment.objects.all()

# данный тест проверяет корректность присвоения
# задолжности при создании объекта класса Payment
# в данной выборке создано задолжностей (7) - платежей (8)
# два долга начисляются в будущем                           - 2
# один платеж сверху не находит себе задолжности для оплаты - 1
# соответственно 3 платяжа останутся None
assert len(list(filter(lambda x: x == None, payments.values_list('accrual', flat=True)))) == 3, \
                           "неверное число оплаченных задолжностей"

# проверка корректности создаваемого количества объектов класса Accrual
assert len(accruals) == 7, "неверное число созданных объектов Accrual"

# проверка корректности создаваемого количества объектов класса Payment
assert len(payments) == 8, "неверное число созданных объектов Payment"

# проверка корректности присвоения ForeignKey первому созданному объекту
# первый объект выбирает вторую по счету задолженность
# раньше был только 1999 год
# Платеж:         'date' : '2019-03-10'
# Задолженность:  'date' : '2010-12-04'

assert (payments.first().date, payments.first().accrual.date) == (datetime.fromisoformat("2019-03-10"), datetime.fromisoformat("2010-12-04")), \
                                                            "оплата произошло в неправильном порядке"

