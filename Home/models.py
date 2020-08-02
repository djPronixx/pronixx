from django.db import models

# Create your models here.

class cover(models.Model):
    cover_logo = models.ImageField(default='')
    cover_heading = models.CharField(max_length=50)
    cover_img = models.ImageField(default='')

    def __str__(self):
        return self.cover_heading

class home_info(models.Model):
    event_tagline = models.CharField(max_length=50)
    features_gallay_tagline = models.CharField(max_length=50)
    pakage_tagline = models.CharField(max_length=50)
    artist_wall_tagline = models.CharField(max_length=50)
    about_us = models.CharField(max_length=500)
    

    

class show(models.Model):
    show_id = models.AutoField
    show_poster = models.ImageField(default="")
    show_name = models.CharField(max_length=50)
    show_date = models.DateField(auto_now=False)
    show_start_time = models.TimeField(auto_now=False)
    show_end_time = models.TimeField(auto_now=False)
    show_artists = models.CharField(max_length=50)

    def __str__(self):
        return self.show_name
  


class features_gallay(models.Model):
    features_id = models.AutoField
    tag_line = models.CharField(max_length=60)
    features_img = models.ImageField(default='')
    click_date = models.DateField(auto_now=False)

    def __str__(self):
        return self.tag_line


    


class pakage(models.Model):
    pakage_id =models.AutoField
    pakage_img = models.ImageField(default='')
    pakage_name = models.CharField(max_length=60)
    pakage_details = models.CharField(max_length=600)

    def __str__(self):
        return self.pakage_name

   

class artist_wall(models.Model):
    artist_id =models.AutoField
    name = models.CharField(max_length=60)
    img = models.ImageField(default='')
    position = models.CharField(max_length=60)
    details = models.CharField(max_length=300)

    def __str__(self):
        return self.name


   