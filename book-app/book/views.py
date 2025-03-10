from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db import models
from django.contrib import messages

from .models import Category, Book
from .forms import BookForm
from .forms import BookForm2

################################################################
#一覧表示用のDjango標準ビュー(ListView)を承継して一覧表示用のクラスを定義
class BookListView(ListView):
    #利用するモデルを指定
    model = Book
    #データを渡すテンプレートファイルを指定
    template_name = 'book/book_list.html'

    #家計簿テーブルの全データを取得するメソッドを定義
    def queryset(self):
        return Book.objects.all().order_by('rental').reverse()

################################################################
class BookCreateView(CreateView):
    #利用するモデルを指定
    model = Book
    #データを渡すテンプレートファイルを指定
    template_name = 'book/book_form.html'

    #利用するフォームクラス名を指定
    form_class = BookForm
    #登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('book:book_list')

################################################################
class BookUpdateView(UpdateView):
    #利用するモデルを指定
    model = Book
    #データを渡すテンプレートファイルを指定
    template_name = 'book/book_form2.html'

    #利用するフォームクラス名を指定
    form_class = BookForm2
    #登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('book:book_list')

################################################################
class BookDeleteView(DeleteView):
    #利用するモデルを指定
    model = Book
    #削除処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('book:book_list')

################################################################
class BookDetailView(DetailView):
    #利用するモデルを指定
    model = Book
    #データを渡すテンプレートファイルを指定
    template_name = 'book/book_detail.html'
################################################################
