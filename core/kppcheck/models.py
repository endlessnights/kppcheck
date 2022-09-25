from django.db import models
from django.shortcuts import render
import datetime
from django_admin_geomap import GeoItem
from django.db.models import Avg
# Create your models here.


class Kpps(models.Model, GeoItem):
    name = models.CharField(verbose_name='Название', max_length=150, blank=False)
    address = models.CharField(verbose_name='Адрес', max_length=300, blank=False)
    border = models.CharField(verbose_name='Граница', max_length=150, blank=True)
    lon = models.FloatField(default='71.430557', null=False)  # longitude
    lat = models.FloatField(default='51.128239', null=False)  # latitude

    @property
    def geomap_longitude(self):
        return '' if self.lon is None else str(self.lon)

    @property
    def geomap_latitude(self):
        return '' if self.lon is None else str(self.lat)

    @property
    def geomap_popup_common(self):
        return "<a href='kpp/{}' target='iframe1'>{}</a>".format(self.id, self.name)

    def __str__(self):
        return self.name

    def publish(self):
        self.save()

    class Meta:
        verbose_name = 'кпп'
        verbose_name_plural = 'кпп'


class Reports(models.Model):
    kpp = models.ForeignKey(Kpps, on_delete=models.PROTECT, verbose_name='КПП')
    created_date = models.DateTimeField(
        verbose_name='Дата обновления',
        null=False
    )
    ttw = models.FloatField(
        verbose_name='Время ожидания',
        null=False
    )
    carcount = models.IntegerField(
        verbose_name='Кол-во авто',
        null=True
    )
    pcount = models.IntegerField(
        verbose_name='Кол-во людей',
        null=True
    )

    def publish(self):
        self.created_date = datetime.datetime.now()
        self.save()

    class Meta:
        verbose_name = 'отчет'
        verbose_name_plural = 'отчеты'
