import datetime
import os
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save


def get_User_file_path(request, filename):
    original_filename = filename
    nowtime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowtime, original_filename)
    return os.path.join('uploads/user/', filename)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn=models.CharField(max_length=13)
    publication_date=models.DateField(null=True,auto_now_add=True)
    genre=models.CharField(max_length=100)
    quantity=models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to=get_User_file_path,default='uploads/default.png',)


    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


def create_user(sender, *args, **kwargs):
    if kwargs['created']:
        user = User.objects.create(username=kwargs['instance'],password="dummypass")



class Student(models.Model):
    roll_no = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=10)
    total_books_due=models.IntegerField(default=0)
    email=models.EmailField(unique=True)
    def __str__(self):
        return str(self.roll_no)


post_save.connect(create_user, sender=Student)
class Borrower(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(null=True,blank=True)
    return_date = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.student.name+" borrowed "+self.book.title
