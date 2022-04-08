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

class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        abstract = True

    type_name = models.ForeignKey(Item, on_delete=models.CASCADE,
                                  verbose_name='Тип товара')
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True,
                              verbose_name='Изображение')
    quantity = models.IntegerField(verbose_name='Количество')


    def __str__(self):
        return self.type_name

class Toys(Category):
    toys_choices = [
        ('Зайка Ми', 'Зайка Ми'),
        ('Jack&Lin', 'Jack&Lin'),
        ('Подария', 'Подария'),
        ('Other', 'Другие'),
    ]
    toys = models.CharField(max_length=20, choices=toys_choices,
                            verbose_name='Тип игрушки')
    price = models.DecimalField(max_digits=12, decimal_places=2,
                                verbose_name='Стоимость')

    comments = models.TextField(max_length=500, blank=True,
                                verbose_name='Комментарий')

    price_quantity = models.DecimalField(max_digits=12, blank=True,
                                         decimal_places=2, default=0,
                                         verbose_name='Общая стоимость')

    def save(self, *args, **kwargs):
        self.price_quantity = self.price * self.quantity
        super(Toys, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Игрушка'
        verbose_name_plural = 'Игрушки'

    def __str__(self):
        return "{} : {} : {} шт.".format(self.type_name,
                                         self.toys, self.quantity,)

class Bathrobes(Category):
    size_choices = [
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
    ]
    type_choices = [
        ('Махровый', 'Махровый'),
        ('Флисовый', 'Флисовый'),
        ('Другие', 'Другие'),
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
    type = models.CharField(max_length=20, choices=type_choices,
                            verbose_name='Материал')
    color = models.CharField(max_length=20, choices=color_choices,
                             verbose_name='Цвет')
    size = models.CharField(max_length=20, choices=size_choices,
                            verbose_name='Размер')
    price = models.DecimalField(max_digits=12, decimal_places=2,
                                verbose_name='Стоимость', default=3300)
    comments = models.TextField(max_length=500, blank=True,
                                verbose_name='Комментарий')
    price_quantity = models.DecimalField(max_digits=12, blank=True,
                                         decimal_places=2, default=0,
                                         verbose_name='Общая стоимость')

    def save(self, *args, **kwargs):
        self.price_quantity = self.price * self.quantity
        super(Bathrobes, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'Халат'
        verbose_name_plural = 'Халаты'


    def __str__(self):
        return "{} : {} : {} : {} : {} шт.".format(self.type_name, self.type,
                                          self.color, self.size, self.quantity)
class Towels(Category):
    towel_size_choices = [
        ('50*90', '50*90'),
        ('70*130', '70*130'),
    ]
    towel_color_choices = [
        ('Синий', 'Синий'),
        ('Зеленый', 'Зеленый'),
        ('Морская волна', 'Морская волна'),
        ('Розовый', 'Розовый'),
        ('Темно-сини', 'Темно-сини'),
        ('Голубой', 'Голубой'),
        ('Белый', 'Белый'),
        ('Малиновый', 'Малиновый'),
        ('Сиреневый', 'Сиреневый'),
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
    color = models.CharField(max_length=20, choices=towel_color_choices,
                             verbose_name='Цвет')
    size = models.CharField(max_length=20, choices=towel_size_choices,
                            verbose_name='Размер')
    price = models.DecimalField(max_digits=12, decimal_places=2,
                                verbose_name='Стоимость')
    comments = models.TextField(max_length=500, blank=True,
                                verbose_name='Комментарий')
    price_quantity = models.DecimalField(max_digits=12, blank=True,
                                         decimal_places=2, default=0,
                                         verbose_name='Общая стоимость')

    def save(self, *args, **kwargs):
        self.price_quantity = self.price * self.quantity
        super(Towels, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Полотенце'
        verbose_name_plural = 'Полотенца'

    def __str__(self):
        return "{} : {} : {} : {} шт.".format(self.type_name, self.size,
                                self.color, self.quantity)

