from django.db import models

class Person(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Полное имя'
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    photo = models.ImageField(
        upload_to='photos/',
        null=True,
        blank=True,
        verbose_name='Фото'
    )
        # Новые опциональные поля:
    is_alive = models.BooleanField(
        default=True,
        verbose_name='Живой?',
        help_text='Снимите галочку, если человек скончался'
    )
    contact_info = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Контакты',
        help_text='Телефон, e-mail или ссылки на соцсети'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание / биография',
        help_text='Любые заметки, истории, даты событий'
    )

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    def __str__(self):
        return self.name


class Relation(models.Model):
    parent = models.ForeignKey(
        Person,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name='Родитель'
    )
    child = models.ForeignKey(
        Person,
        related_name='parents',
        on_delete=models.CASCADE,
        verbose_name='Ребёнок'
    )

    class Meta:
        verbose_name = 'Связь родитель – ребёнок'
        verbose_name_plural = 'Связи родитель – ребёнок'
        # чтобы одна и та же пара parent–child не дублировалась
        unique_together = ('parent', 'child')

    def __str__(self):
        return f"{self.parent.name} → {self.child.name}"
