from django.db import models

# Create your models here.

class BookInfo(models.Model):
    bittle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField()
    bread=models.IntegerField(default=0)
    bcommet=models.IntegerField(null=False)
    idDelete=models.BooleanField(default=False)
    class Meta:
        db_table='bookinfo'

class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField(default=True)
    hcontent=models.CharField(max_length=100)
    isDelete=models.BooleanField(default=False)
    book=models.ForeignKey('BookInfo')

    def showname(self):
        return self.hname
