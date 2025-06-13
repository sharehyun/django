from django.db import models

# class Product(models.model):
#     id = models.IntegerField(default=0,primary_key=True)
#     name = models.CharField(max_length=100)
#     category1 = models.CharField(max_length=50)
#     category2 = models.CharField(max_length=50)
#     brand = models.CharField(max_length=50)
#     madein = models.CharField(max_length=50)
#     weight = models.IntegerField(default=0)
#     cPice = models.IntegerField(default=0)
#     dPrice = models.IntegerField(default=0)
#     inventory = models.IntegerField(default=0)
#     img1 = models.ImageField()
#     img2 = models.ImageField(null=True,blank=True)
#     img3 = models.ImageField(null=True,blank=True)
#     regiDate = models.DateTimeField(auto_now_add=True)
#     fixDate = models.DateTimeField(auto_now=True)
#     available = models.IntegerField(default=0)
#     exposure = models.IntegerField(default=0)

#     그외 원산지(char), 중량(int), 소비자가격(int), 할인가(int), 재고(int), 메인이미지(img), 서브이미지(img), 서브이미지2(img), 등록일자(datetime),
#     수정일자(datetime), 판매여부-판매중/품절/판매중지(char/int), 상위노출(notice와 같은 방식-int)
#     숫자 쪽이 검색이 빠르기 때문에 되도록이면 숫자를 활용하는 쪽이 좋다??
    