# -*- cording: urf-8 -*-
from django.forms import ModelForm
from cms.models import Book, Impression

class BookForm(ModelForm):
    '''書籍のフォーム'''
    class Meta:
        model = Book
        fields = ('name', 'publisher', 'page',)

class  ImpressionForm(ModelForm):
    '''感想フォーム'''
    class Meta:
        model = Impression
        fields =('comment', )
