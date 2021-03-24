from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=100)
    article = models.CharField(max_length=20, null=True, blank=True, unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField(default=1)
    dt = models.DateField()
    is_sale = models.BooleanField(default=False)
    category = models.ForeignKey('GoodsCategory', on_delete=models.CASCADE)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE, related_name="goods")
    tags = models.ManyToManyField('GoodsTag', related_name="goods")

    class Meta:
        ordering = ['is_sale', 'name', 'price']
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name

    @property
    def in_stock(self):
        return 'в наличии' if self.quantity > 0 else 'нет в наличии'

    @property
    def description(self):
        return f'{self.name}: {self.price}, {self.article}, {self.in_stock}'


class GoodsCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    is_visible = models.BooleanField(default=False)

    class Meta:
        ordering = ['is_visible', 'name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class GoodsTag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    not_empty_filed = models.DateField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Seller(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'

    def __str__(self):
        return self.full_name
