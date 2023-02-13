from datetime import timedelta

from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class CardStatus(models.Model):
    name = models.CharField(
        max_length=24,
        unique=True,
        null=False,
        blank=False,
        verbose_name='name',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'


class CardSeria(models.Model):
    name = models.CharField(
        max_length=6,
        unique=True,
        null=False,
        blank=False,
        verbose_name='name',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'seria'
        verbose_name_plural = 'seria'


class Card(models.Model):
    status = models.ForeignKey(CardStatus, on_delete=models.CASCADE, null=False, blank=False)
    seria = models.ForeignKey(CardSeria, on_delete=models.CASCADE, null=False, blank=False)
    date_created = models.DateField(default=now)
    expire_date = models.DateField(default=now() + timedelta(days=365))
    last_used_date = models.DateTimeField(null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def get_absolute_url(self):
        return reverse('main_card_detail', kwargs={'card_id': self.id})


class Product(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)


class Order(models.Model):
    date_created = models.DateTimeField(default=now)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=False, blank=False)


class OrderProduct(models.Model):
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=False, blank=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False)
