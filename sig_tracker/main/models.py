from django.db import models


# Create your models here.
class Sig(models.Model):
    sig_name = models.CharField(blank=False, max_length=100)
    co_ordinator = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sig_name

class DevSig(models.Model):
    topic = models.CharField(max_length=1000)
    topic_gist = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    resources = models.TextField(blank=True)
    conductors = models.TextField(blank=True)
    co_ordinator = models.CharField(max_length=250)

    def __str__(self):
        return self.topic

class MlSig(models.Model):
    topic = models.CharField(max_length=1000)
    topic_gist = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    resources = models.TextField(blank=True)
    conductors = models.TextField(blank=True)
    co_ordinator = models.CharField(max_length=250)

    def __str__(self):
        return self.topic

class CpSig(models.Model):
    topic = models.CharField(max_length=1000)
    topic_gist = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    resources = models.TextField(blank=True)
    conductors = models.TextField(blank=True)
    co_ordinator = models.CharField(max_length=250)

    def __str__(self):
        return self.topic




