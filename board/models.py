from django.db import models

# Create your models here.

class Board(models.Model):
    b_no = models.AutoField(primary_key=True)
    b_title = models.CharField(max_length=255)
    b_note = models.CharField(max_length=4096, blank=True, null=True)
    b_writer = models.CharField(max_length=50, blank=True, null=True)
    parent_no = models.IntegerField(blank=True, null=True)
    b_cout = models.IntegerField(blank=True, null=True)
    b_date = models.DateTimeField(blank=True, null=True)
    usage_flag = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board'

    def __str__(self):
        return f'"제목 : {self.b_title}", "작성자 : {self.b_writer}"'