from typing import Tuple

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField('Когда создано объявление',
                                      default=timezone.now,
                                      db_index=True)

    description = models.TextField('Текст объявления',
                                   blank=True)
    price = models.IntegerField('Цена квартиры',
                                db_index=True)

    town = models.CharField('Город',
                            max_length=50,
                            db_index=True)
    town_district = models.CharField('Район города',
                                     max_length=50,
                                     blank=True,
                                     help_text='Чертаново Южное')
    address = models.TextField('Адрес квартиры',
                               help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField('Этаж',
                             max_length=3,
                             help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField('Количество комнат',
                                       db_index=True)
    living_area = models.IntegerField('жилая площадь (кв.м)',
                                      null=True,
                                      blank=True,
                                      db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона',
                                          db_index=True)
    active = models.BooleanField('Объявление активно',
                                 db_index=True)
    construction_year = models.IntegerField('Год постройки здания',
                                            null=True,
                                            blank=True,
                                            db_index=True)
    new_building = models.BooleanField('Новостройка',
                                       null=True,
                                       blank=True,
                                       db_index=True)
    like = models.ManyToManyField(User,
                                  verbose_name='Кто лайкнул',
                                  related_name='flat_likes',
                                  blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    complainterator = models.ForeignKey(User,
                                        verbose_name='Кто жаловался',
                                        on_delete=models.CASCADE,
                                        related_name='users')
    address = models.ForeignKey(Flat,
                                verbose_name='Квартира, на которую пожаловались',
                                on_delete=models.CASCADE,
                                related_name='addresses')
    contents = models.TextField('Текст обращения')


    def __str__(self):
        return f'{self.complainterator}, {self.address}'


class Owner(models.Model):
    owner = models.CharField('ФИО владельца',
                             max_length=250,
                             db_index=True)
    phonenumber = models.CharField('Телефон',
                                   max_length=20,
                                   db_index=True)
    pure_phone = PhoneNumberField('Телефон (нормализованный)',
                                  region='RU',
                                  max_length=20,
                                  blank=True,
                                  null=True,
                                  db_index=True)
    flats = models.ManyToManyField(Flat,
                                   verbose_name='Квартиры',
                                   related_name='owned_by')

    def __str__(self):
        return self.owner
