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
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все товары'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_slug = self.request.GET.get('tag')
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)
        return queryset


class GoodsListByCategoryView(ListView):
    model = Goods
    template_name = 'main/goods_grid.html'
    paginate_by = 2

    def get_queryset(self):
        self.category = get_object_or_404(GoodsCategory, slug=self.kwargs['slug'])
        queryset = Goods.objects.filter(category=self.category)

        tag_slug = self.request.GET.get('tag')
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)
        return queryset

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
