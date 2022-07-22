from django.db import models


class Actual(models.Model):
    name = models.CharField(max_length=200,blank=True)
    text = models.CharField(max_length=200,blank=True)
    url_adress = models.CharField(max_length=200,blank=True)
    guid = models.CharField(max_length=200,blank=True)
    creator_name = models.CharField(max_length=200,blank=True)
    category = models.CharField(max_length=200,blank=True)
    pub_date = models.DateTimeField(null=True)
    image_url = models.CharField(null=True,max_length=200)

    def __str__(self):
        return self.name

class Newest(models.Model):
    name = models.CharField(max_length=200,blank=True)
    text = models.CharField(max_length=200,blank=True)
    url_adress = models.CharField(max_length=200,blank=True)
    guid = models.CharField(max_length=200,blank=True)
    creator_name = models.CharField(max_length=200,blank=True)
    category = models.CharField(max_length=200,blank=True)
    pub_date = models.DateTimeField(null=True)
    image_url = models.CharField(null=True,max_length=200)

    def __str__(self):
        return self.name

class News(models.Model):
    name = models.CharField(max_length=200,blank=True)
    text = models.CharField(max_length=200,blank=True)
    url_adress = models.CharField(max_length=200,blank=True)
    guid = models.CharField(max_length=200,blank=True)
    creator_name = models.CharField(max_length=200,blank=True)
    category = models.CharField(max_length=200,blank=True)
    pub_date = models.DateTimeField(null=True)
    image_url = models.CharField(null=True,max_length=200)

    def __str__(self):
        return self.name

class Sport(models.Model):
    name = models.CharField(max_length=200,blank=True)
    text = models.CharField(max_length=200,blank=True)
    url_adress = models.CharField(max_length=200,blank=True)
    guid = models.CharField(max_length=200,blank=True)
    creator_name = models.CharField(max_length=200,blank=True)
    category = models.CharField(max_length=200,blank=True)
    pub_date = models.DateTimeField(null=True)
    image_url = models.CharField(null=True,max_length=200)

    def __str__(self):
        return self.name

class Tech(models.Model):
    name = models.CharField(max_length=200,blank=True)
    text = models.CharField(max_length=200,blank=True)
    url_adress = models.CharField(max_length=200,blank=True)
    guid = models.CharField(max_length=200,blank=True)
    creator_name = models.CharField(max_length=200,blank=True)
    category = models.CharField(max_length=200,blank=True)
    pub_date = models.DateTimeField(null=True)
    image_url = models.CharField(null=True,max_length=200)

    def __str__(self):
        return self.name

class Lifestyle(models.Model):
    name = models.CharField(max_length=200,blank=True)
    text = models.CharField(max_length=200,blank=True)
    url_adress = models.CharField(max_length=200,blank=True)
    guid = models.CharField(max_length=200,blank=True)
    creator_name = models.CharField(max_length=200,blank=True)
    category = models.CharField(max_length=200,blank=True)
    pub_date = models.DateTimeField(null=True)
    image_url = models.CharField(null=True,max_length=200)

    def __str__(self):
        return self.name

class Show(models.Model):
    name = models.CharField(max_length=200,blank=True)
    text = models.CharField(max_length=200,blank=True)
    url_adress = models.CharField(max_length=200,blank=True)
    guid = models.CharField(max_length=200,blank=True)
    creator_name = models.CharField(max_length=200,blank=True)
    category = models.CharField(max_length=200,blank=True)
    pub_date = models.DateTimeField(null=True)
    image_url = models.CharField(null=True,max_length=200)

    def __str__(self):
        return self.name

class Viral(models.Model):
    name = models.CharField(max_length=200,blank=True)
    text = models.CharField(max_length=200,blank=True)
    url_adress = models.CharField(max_length=200,blank=True)
    guid = models.CharField(max_length=200,blank=True)
    creator_name = models.CharField(max_length=200,blank=True)
    category = models.CharField(max_length=200,blank=True)
    pub_date = models.DateTimeField(null=True)
    image_url = models.CharField(null=True,max_length=200)


    def __str__(self):
        return self.name



