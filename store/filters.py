from django import forms
from .models import *
import django_filters
from django_filters import RangeFilter
from django_filters.widgets import RangeWidget

#price_lte = django_filters.RangeFilter()

class ProductFilter(django_filters.FilterSet):

    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))
    #start_price = django_filters.RangeFilter(label='max',field_name='price',lookup_expr=('gte'),widget=RangeWidget(attrs={'type': 'range','class':'form-control-range'}))
    #end_price = django_filters.RangeFilter(label='min',field_name='price',lookup_expr=('lte'),widget=RangeWidget(attrs={'type': 'range','class':'form-control-range'}))
    #price = django_filters.RangeFilter(field_name='price',widget=RangeWidget(attrs={'type': 'range','class':'form-control-range'}))
    class Meta:
        model = Item
        fields = ['category',]
