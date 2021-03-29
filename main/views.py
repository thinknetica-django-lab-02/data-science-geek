from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from main.models import Goods, GoodsCategory


def index(request):
    template_name = 'main/index.html'
    context = {'turn_on_block': True}
    return HttpResponse(render(request, template_name, context=context))


class GoodsListView(ListView):
    model = Goods
    template_name = 'main/goods_grid.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все товары'
        return context


class GoodsListByCategoryView(ListView):
    model = Goods
    template_name = 'main/goods_grid.html'

    def get_queryset(self):
        self.category = get_object_or_404(GoodsCategory, slug=self.kwargs['slug'])
        return Goods.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Категория: {self.category}'
        return context


class GoodsDetailView(DetailView):
    model = Goods
    template_name = 'main/goods_detail.html'

    def get_object(self, **kwargs):
        self.goods = get_object_or_404(Goods, slug=self.kwargs['slug'])
        return self.goods

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Категория: {self.goods.category}'
        return context
