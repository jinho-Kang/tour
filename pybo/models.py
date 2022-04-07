from django.db import models
import pymysql

class Question(models.Model):
    subject=models.CharField(max_length=200)
    content=models.TextField()
    create_date=models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()

class Restaurant(models.Model):
    가게이름=models.CharField(max_length=100)
    주소=models.CharField(max_length=100)
    위도=models.FloatField(default=0.0)
    경도=models.FloatField(default=0.0)
    class Meta:
        db_table = "restaurant"
class TourInfo(models.Model):
    관광안내소명 = models.CharField(max_length=100)
    소재지도로명주소 = models.CharField(max_length=100)
    위도 = models.FloatField()
    경도 = models.FloatField()
    class Meta:
        db_table = "tour_info"
class TourMotel(models.Model):
    지번주소 = models.CharField(max_length=100)
    사업장명 = models.CharField(max_length=100)
    위도 = models.FloatField()
    경도 = models.FloatField()
    class Meta:
        db_table = "tour_motel"
class TourStreet(models.Model):
    검색키워드 = models.CharField(max_length=100)
    지번주소 = models.CharField(max_length=100)
    경도 = models.FloatField()
    위도 = models.FloatField()
    class Meta:
        db_table = "tour_street"
