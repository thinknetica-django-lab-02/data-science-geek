from django.db import models
from django.urls import reverse
from uuslug import uuslug


class Goods(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to='goods', blank=True)
    price = models.DecimalField('Цена', max_digits=12, decimal_places=2)
    quantity = models.IntegerField('Количество', default=1)
    category = models.ForeignKey('GoodsCategory', on_delete=models.CASCADE,
                                 verbose_name='Категория')
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE, related_name="goods",
                               verbose_name='Продавец')
    tags = models.ManyToManyField('GoodsTag', related_name="goods",
                                  verbose_name='Тэги')
    draft = models.BooleanField('Черновик', default=False)

    slug = models.SlugField(max_length=200, editable=False)
    article = models.CharField('Артикул', max_length=10, editable=False)

    def save(self, *args, **kwargs):
        self.article = str(self.id).zfill(6)
        self.slug = uuslug(self.name, instance=self)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['draft', 'name', 'price']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('goods-detail', args=[self.slug])

    @property
    def stock_status(self):
        return 'в наличии' if self.quantity > 0 else 'нет в наличии'


class GoodsCategory(models.Model):
    name = models.CharField('Название', max_length=30, unique=True)
    slug = models.SlugField('Ссылка', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='categories', blank=True)
    draft = models.BooleanField('Черновик', default=False)

    class Meta:
        ordering = ['draft', 'name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('goods-by-category', args=[self.slug])


class GoodsTag(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Seller(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    birth_date = models.DateField('Дата рождения', blank=True, null=True)
    email = models.EmailField('E-mail', max_length=100)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'

    def __str__(self):
        return self.full_name
