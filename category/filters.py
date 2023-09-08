from django.db.models import Q
from dataclasses import fields
import django_filters
from django import forms
from category.models import *
from django_filters import CharFilter
from django.forms.widgets import TextInput, Textarea



class Bookfilter(django_filters.FilterSet):
    q=CharFilter(method='my_custom_filter',label="",widget=TextInput(attrs={'placeholder': 'Search here..','class': 'form-control col-8','size': 500,}))
    class Meta:
        model = Book
        fields=['q']
    def my_custom_filter(self, queryset, name, value):
        print(name)
        print(value)
        return queryset.filter(
                Q(title__icontains=value) | Q(author__icontains=value)
            )