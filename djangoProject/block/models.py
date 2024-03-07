from django.db import models
from jsonfield import JSONField
# Create your models here.

#在这里我们创建存储区块链内容的model
class Block(models.Model):
    index = models.IntegerField(primary_key=True,)
    transactions = models.TextField()
    nonce = models.IntegerField()
    timestamp = models.FloatField()
    previous_hash = models.TextField()

class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.CharField(max_length=32)
    province = models.CharField(max_length=32)

class Emps(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.ForeignKey("Dep", on_delete=models.CASCADE)
    province = models.CharField(max_length=32)
class Dep(models.Model):
    title = models.CharField(max_length=32)

class SimpleBlock(models.Model):
    name = models.CharField(max_length=32)
    key = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

class MyDict(models.Model):
    data = JSONField()

my_dict = MyDict(data={'key1': ['value1', 'value2'], 'key2': ['value2', 'value3']})
my_dict.save()
# learning process is stopped here