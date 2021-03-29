from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOriginal
from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.flatpages.models import FlatPage

from main.models import Goods, GoodsCategory, GoodsTag, Seller


class CKEditorFlatpageForm(FlatpageForm):
    content = forms.CharField(widget=CKEditorWidget())


class FlatPageAdmin(FlatPageAdminOriginal):
    form = CKEditorFlatpageForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(Goods)
admin.site.register(GoodsCategory)
admin.site.register(GoodsTag)
admin.site.register(Seller)
