# -*- coding: utf-8 -*-
from django.db import models

class Votes(models.Model):
    nairobi = models.IntegerField(default=0)
    athens = models.IntegerField(default=0)
    bangkok = models.IntegerField(default=0)
    reykjavik = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __unicode__(self):
        return self.total