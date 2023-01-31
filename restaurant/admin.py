from django.contrib import admin
from .models import Booking, Menu
# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'guest_number')
    search_fields = ('first_name', 'last_name')
    list_per_page: 20


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_per_page = 10


admin.site.register(Booking, BookingAdmin)
admin.site.register(Menu, MenuAdmin)
