from django.db import models
from datetime import datetime
 
class BaseModel(models.Model):
 
    class Meta:
        verbose_name ="ベースモデル"
        verbose_name_plural ="ベースモデル"
      
    #columns
    updated_by = models.BigIntegerField("更新者")
    updated_at = models.DateField("更新日", default=datetime.now)
    created_by = models.BigIntegerField("登録者")
    created_at = models.DateField("登録日", default=datetime.now)
    deleted_by = models.DateField("削除日", default=datetime.now)
 
    def __str__(self):
        return self.deleted_by

class UserMaster(BaseModel):
 
    class Meta:
        verbose_name ="ユーザーマスタ"
        verbose_name_plural ="ユーザーマスタ"
      
    #columns
    user_name = models.SlugField("ユーザー名", default="NO NAME")
 
    def __str__(self):
        return self.user_id 

class Category(models.Model):
 
    class Meta:
        verbose_name ="カテゴリ"
        verbose_name_plural ="カテゴリ"

    #カラム名の定義
    category_name = models.CharField(max_length=255,unique=True)
 
    def __str__(self):
        return self.category_name
 
 
class Kakeibo(models.Model):
 
    class Meta:
        verbose_name ="家計簿"
        verbose_name_plural ="家計簿"
 
    #カラムの定義
    date = models.DateField("日付",default=datetime.now)
    category = models.ForeignKey(Category, on_delete = models.PROTECT, verbose_name="カテゴリ")
    money = models.IntegerField("金額", help_text="単位は日本円")
    quantity = models.IntegerField(verbose_name="数量",default=0)
    memo = models.CharField(verbose_name="メモ", max_length=500)
 
    def __str__(self):
        return self.memo