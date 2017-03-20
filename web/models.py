#coding: utf-8

from __future__ import unicode_literals

from django.db import models


def image_path(instance, filename):                                                  
    ext = filename.split('.')[-1]                                                    
    filename = "%s.%s" % (uuid.uuid4(), ext)                                         
    return '/'.join(['dir_name', filename])

class ImageModel(models.Model):
    image = models.ImageField(
        height_field='image_height',      

        width_field='image_width',         

        upload_to=image_path,                       

        verbose_name=('image')                                           
    )   
    image_height = models.PositiveIntegerField(                                      
        verbose_name=('image height'),                                              
        blank=True,
        null=True
    )   
    image_width = models.PositiveIntegerField(                                       
        verbose_name=('image width'),                                               
        blank=True,                                                                  
        null=True                                                                    
    )
    
    def __unicode__(self):
        return unicode(self.image)

class Starlist(models.Model):
    self_name = models.CharField(max_length=50,)
    star_name = models.CharField(max_length=50, default='陳曉薇')
    rating = models.CharField(max_length=50,)
    star_id = models.CharField(max_length=50,default = '32')

    def __unicode__(self):
        return self.self_name



class JsonTest(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.TextField()  # This field type is a guess.

    def __unicode__(self):
        return unicode(self.id)

class Registration(models.Model):
    account_name = models.CharField(max_length=50, default='陳曉薇')
    gender = models.CharField(max_length=10, )
    matchgender = models.CharField(max_length=50, default='男')
    star = models.CharField(max_length=10, default='以後告訴您')
    height = models.CharField(max_length=10, null=False, default='165')
    hair = models.CharField(max_length=50,  default='以後告訴您')
    eye = models.CharField(max_length=50,  default='以後告訴您')
    political = models.CharField(max_length=50,  default='以後告訴您')
    job = models.CharField(max_length=50,  default='以後告訴您')
    income = models.CharField(max_length=100,  default='以後告訴您')
    relationship = models.CharField(max_length=50, default='以後告訴您')
    language = models.CharField(max_length=50,  default='以後告訴您')
    education = models.CharField(max_length=50,  default='以後告訴您')
    sport_habbit = models.CharField(max_length=50, default='以後告訴您')
    wantchild = models.CharField(max_length=50,  default='以後告訴您')
    children = models.CharField(max_length=50,   default='以後告訴您')
    figure = models.CharField(max_length=50,   default='以後告訴您')
    faith = models.CharField(max_length=50,  default='以後告訴您')
    smoke = models.CharField(max_length=50, default='以後告訴您')
    drink = models.CharField(max_length=50, default='以後告訴您')
    race = models.CharField(max_length=250,  default='以後告訴您')
    sport = models.CharField(max_length=250,  default='以後告訴您')
    interest = models.CharField(max_length=250,  default='以後告訴您')
    tag = models.CharField(max_length=250, )

    def __unicode__(self):
        return self.account_name

class Matchlist(models.Model):
    self_name = models.CharField(max_length=50,)
    self_id = models.CharField(max_length=50, )
    account_name = models.CharField(max_length=50, default='陳曉薇')
    account_id = models.CharField(max_length=50, )
    rating = models.CharField(max_length=50,)
    star = models.CharField(max_length=50, default='楊祐寧')
    star_id = models.CharField(max_length=50, default='29')
 
    def __unicode__(self):
        return self.self_name

class Choose(models.Model):
    star = models.CharField(max_length=250,)

    def __unicode__(self):
        return self.star
