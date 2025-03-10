from django.db import models
from datetime import datetime    #追加する


class Category(models.Model):
    class Meta:
       #テーブル名の指定
       db_table ="category"
       verbose_name ="カテゴリ"         #追加
       verbose_name_plural ="カテゴリ"  #追加

    #カラム名の定義
    category_name = models.CharField(max_length=255,unique=True)

    def __str__(self):
       return self.category_name


class Book(models.Model):
    class Meta:
       #テーブル名
       db_table ="book"
       verbose_name ="本の登録"          #追加
       verbose_name_plural ="本の登録"   #追加

    # カラムの定義
    title = models.CharField(verbose_name="本のタイトル", max_length=255, help_text="※入力必須項目")
    author = models.CharField(verbose_name="本の著者名", max_length=30, blank=True)
    publisher = models.CharField(verbose_name="本の出版社", max_length=30, blank=True)
    buydate = models.DateField(verbose_name="購入日",default=datetime.now, null=True, blank=True)

    # category = models.ForeignKey(Category, on_delete = models.PROTECT, verbose_name="カテゴリ")
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, verbose_name="カテゴリ", null=True, blank=True)
    url = models.URLField(verbose_name="本のURL（楽天ブックスのURLを入力ください）", max_length=255, help_text="※入力必須項目<br>※重複書籍の登録防止になります", unique=True)

    rental = models.IntegerField(verbose_name="本の貸し出し回数（お手数ですが、貸し出し時に数値をインクリメントください）", blank=True, default=0, help_text="※要望あれば、自動インクリメント機能を実装します")
    email = models.EmailField(verbose_name="本の貸出先E-Mail（本のレンタル時は、E-Mailを入力ください）", max_length=255, blank=True, help_text="※本を返却するときは、E-Mailを削除ください")
    memo = models.TextField(verbose_name="メモ", max_length=255, blank=True)
    comment = models.TextField(verbose_name="本のコメント（書評）", max_length=255, blank=True)

    ########################################################################
    created_at = models.DateTimeField(verbose_name='登録日時',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    ########################################################################


    def __str__(self):
           return self.title
