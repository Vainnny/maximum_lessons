from django.db import models


class Adverts(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    content = models.TextField('Текст объявления')
    photo = models.CharField('Изображение', max_length=100)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    category = models.SmallIntegerField('Категория товара')
    phone_number = models.CharField('Номер телефона', max_length=15)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг будет уместен')
    isActual = models.BooleanField('Актуально')

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'Adverts(id={self.id}, title={self.title}, price={self.price})'
