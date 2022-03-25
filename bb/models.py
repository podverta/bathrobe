from django.db import models

class Item(models.Model):
    """items for embroidery"""
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        """return name"""
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Sample(models.Model):
    size_choices = [
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
    ]
    type_choices = [
        ('Terry', 'Махровый'),
        ('Fleece', 'Флисовый'),
    ]
    toys_choices = [
        ('Mi', 'Зайка МИ'),
        ('JL', 'Jack&Lin'),
        ('Podariy', 'Подария'),
    ]
    color_choices = [
        ('Синий', 'Синий'),
        ('Зеленый', 'Зеленый'),
        ('Морская волна', 'Морская волна'),
        ('Розовый', 'Розовый'),
        ('Темно-сини', 'Темно-сини'),
        ('Белый', 'Белый'),
        ('Черный', 'Черный'),
        ('Бордовый', 'Бордовый'),
        ('Серый', 'Серый'),
        ('Темно-серый', 'Темно-серый'),
        ('Кремовый', 'Кремовый'),
        ('Фиолетовый', 'Фиолетовый'),
        ('Пыльно-зеленый', 'Пыльно-зеленый'),
        ('Темно-коричневый', 'Темно-коричневый'),
        ('Светло-коричневый', 'Светло-коричневый'),
        ('Антрацит', 'Антрацит'),
        ('Джинс', 'Джинс'),
    ]
    type_name = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='products', verbose_name='Тип товара')
    name = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
    type = models.CharField(max_length=20, choices=type_choices, verbose_name='Материал')
    color = models.CharField(max_length=20, choices=color_choices, verbose_name='Цвет')
    size = models.CharField(max_length=20, choices=size_choices, verbose_name='Размер')
    toys = models.CharField(max_length=20, choices=toys_choices, blank=True, verbose_name='Тип игрушки')
    quantity = models.IntegerField()
    comments = models.TextField(max_length=500, blank=True,)

    class Meta:
        verbose_name = 'Пример'
        verbose_name_plural = 'Примеры'


    def __str__(self):
        return self.name