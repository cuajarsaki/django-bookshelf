from django import forms
from .models import Book

from django.core.mail import EmailMessage

trans_zen_han = str.maketrans('a', 'b')


class BookForm(forms.ModelForm):
    """
    新規データ登録画面用のフォーム定義
    """
    class Meta:
        model = Book
        fields =['title', 'author','publisher','buydate', 'category', 'url', 'rental', 'email', 'memo', 'comment']
        widgets = {
                'memo': forms.Textarea(attrs={'rows':2, 'cols':15}),
            }

class BookForm2(forms.ModelForm):
    """
    編集データ登録画面用のフォーム定義
    """
    class Meta:
        model = Book
        fields =['title', 'author','publisher','buydate', 'category', 'url', 'rental', 'email', 'memo', 'comment']
        widgets = {
                'memo': forms.Textarea(attrs={'rows':2, 'cols':15}),
            }
