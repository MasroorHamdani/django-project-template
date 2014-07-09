from django.db import models
from django.contrib.auth.models import User


APPROVAL_CHOICES = (
    (u'1', u'Public'),
    (u'2', u'Private'),
)
STATUS_CHOICES = (
    (u'1', u'Open'),
    (u'2', u'Close'),
)


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_desc = models.CharField(max_length=500)
    task_status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_on = models.DateField()
    user = models.ForeignKey(User)
    task_priority = models.CharField(max_length=1, choices=APPROVAL_CHOICES)
    # def __unicode__(self):
    # return self.task_name ,self.task_desc, self.task_priority,self.time_status,self.created_on
