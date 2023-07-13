from django.db import models


# Create your models here.
class lecture(models.Model):
    subject = models.CharField("Subject name", max_length=50)
    day = models.CharField("weekday", max_length=50)
    prof = models.CharField("prof name",max_length=50)
    startTime = models.TimeField("start time")
    endTime = models.TimeField("end time")
    classroom = models.IntegerField("classroom",default = 0)
    def __str__(self):
        return (str(self.classroom)+self.subject)
