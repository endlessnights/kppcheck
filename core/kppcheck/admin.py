from django.contrib import admin

# Register your models here.
from .models import Kpps, Reports


@admin.register(Kpps)
class PublishCities(admin.ModelAdmin):
    list_display = [
        'name',
        'address',
    ]


@admin.register(Reports)
class PublishCompanies(admin.ModelAdmin):
    list_display = [
        'kpp',
        'created_date',
        'ttw',
        'carcount',
        'pcount',
    ]