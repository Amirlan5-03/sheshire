from django.contrib import admin
from .models import Person, Relation

class RelationInline(admin.TabularInline):
    model = Relation
    fk_name = 'parent'
    extra = 1
    verbose_name = 'Ребёнок'
    verbose_name_plural = 'Дети'

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # какие поля показывать в списке
    list_display = ('name', 'birth_date', 'is_alive')
    # поля, доступные для фильтрации и поиска
    list_filter = ('is_alive',)
    search_fields = ('name', 'contact_info', 'description')
    # как сгруппировать поля в форме
    fieldsets = (
        ('Основные данные', {
            'fields': ('name', 'birth_date', 'is_alive', 'photo'),
        }),
        ('Контакты и описание', {
            'fields': ('contact_info', 'description'),
            'classes': ('collapse',),  # по желанию можно свернуть секцию
        }),
    )
    inlines = [RelationInline]