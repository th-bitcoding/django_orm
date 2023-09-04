from django.db import models

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name
    

class Members(models.Model):
    group = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    club_members = models.CharField(max_length=100)
    flag = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.group
    

class CsvFile(models.Model):
    csv_file = models.FileField(upload_to='csv_files/')

    def __str__(self):
        return self.csv_file

    