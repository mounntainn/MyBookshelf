from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Category, Kakeibo
 
class KakeiboListView(ListView):
   model = Kakeibo
   template_name = 'kakeibo_list.html'
 
   #家計簿テーブルの全データを取得するメソッドを定義
   def queryset(self):
       return Kakeibo.objects.all()