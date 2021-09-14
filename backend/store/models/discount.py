from django.db import models


class Discount(models.Model):
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, related_name='book_discounts',
                                  verbose_name='Книга')
    start_date = models.DateTimeField(verbose_name='Дата начала')
    end_date = models.DateTimeField(verbose_name='Дата окончания')
    amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Скидка в д.е')
    is_active = models.BooleanField(default=False, verbose_name='Активна')


    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"

