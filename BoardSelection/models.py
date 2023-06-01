from django.db import models

# Create your models here.
class Topic(models.Model):
    order_number = models.IntegerField()
    board_name = models.CharField(max_length=40)
    subject_name = models.CharField(max_length=40)
    class_name = models.CharField(max_length=25)
    chapter_name = models.CharField(max_length=40)
    topic_name = models.CharField(max_length=40)
    def __str__(self):
        return self.chapter_name+' - '+ self.topic_name

class Chapter(models.Model):
    order_number = models.IntegerField()
    board_name = models.CharField(max_length=40)
    subject_name = models.CharField(max_length=40)
    class_name = models.CharField(max_length=25)
    chapter_name = models.CharField(max_length=40)
    pdf_link = models.CharField(max_length=255)
    def __str__(self):
        return self.chapter_name+' - '+ self.subject_name