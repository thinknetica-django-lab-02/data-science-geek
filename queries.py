import datetime

from django.db.models import Count, Q

from main.models import Goods, GoodsCategory, GoodsTag
from main.models import Seller

# Добавляем новые категории
cat1 = GoodsCategory.objects.create(name='food')
cat2 = GoodsCategory.objects.create(name='tech')
cat3 = GoodsCategory.objects.create(name='other')

# Добавляем новые теги
tag1 = GoodsTag.objects.create(name='Дешевый товар')
tag2 = GoodsTag.objects.create(name='Дорогой товар')
tag3 = GoodsTag.objects.create(name='Хочу купить')

# Добавляем покупателей
today = datetime.date.today()

seller1 = Seller(first_name='Иван', last_name='Иванов', email='ivanov@gmail.com', birth_date=today)
seller1.save()

seller2 = Seller(first_name='Петр', last_name='Петров', email='petrov@gmail.com')
seller2.save()

# Добавляем товары
goods1 = Goods(name='Молоко', price=56.60, quantity=20, dt=today, category=cat1, seller=seller1)
goods1.save()
goods1.tags.add(tag1, tag3)

goods2 = Goods(name='Ноутбук', price=56600, quantity=3, dt=today, category=cat2, seller=seller2,
               article='23123')
goods2.save()
goods2.tags.add(tag2)

# Выводим все теги
GoodsTag.objects.all()
# Тэги, у которых название начинается с "Хочу"
GoodsTag.objects.filter(name__startswith="Хочу")

# Все категории
GoodsCategory.objects.all()
# Категории, в которых еще нет товаров
GoodsCategory.objects.filter(goods=None)
# Категории, в которых ровно 1 товар
GoodsCategory.objects.annotate(count_goods=Count('goods')).filter(count_goods=1)

# Все покупатели
Seller.objects.all()

# Покупатели, которые купили молоко ИЛИ их зовут Петр
Seller.objects.filter(Q(goods__name='Молоко') | Q(first_name='Петр'))

# Покупатели, которые купили молоко И их зовут Иван
Seller.objects.filter(Q(goods__name='Молоко') & Q(first_name='Иван'))

# Товар с id = 1
Goods.objects.get(id=1)
