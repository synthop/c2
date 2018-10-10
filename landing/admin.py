from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']         # какие поля будут выводиться в админку
# либо    list_display = [field.name for field in Subscriber._meta.fields] # возвращает все поля модели
    # exclude = ['email'] # исключает указанное поле
    # fields = ['email']  # указываем, какое поле будет отображаться
    list_filter = ['name'] # добавляет в админку фильтр поля, по которому будем фильтровать
    search_fields = ['name', 'email'] # добавляется поле поиска, по которому можно выбрать записи
    class Meta:
        model = Subscriber       # на основании какой модели переопределяется класс Admin

admin.site.register(Subscriber, SubscriberAdmin)
