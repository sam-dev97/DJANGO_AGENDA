from django.contrib import admin
from contact import models
# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'show'
    ordering = '-id',
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'email',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name', 'show'
    list_display_links = 'id',


# Registro da categoria
@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
