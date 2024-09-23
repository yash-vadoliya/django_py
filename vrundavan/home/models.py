from django.db import models

# Create your models here.
class product(models.Model):
    pname = models.CharField(max_length=100)
    price = models.IntegerField()
    pdisc = models.CharField(max_length=500)
    pwidgth = models.FloatField()
    pimg = models.ImageField(upload_to='static/', null=True, blank=True)


    def __str__(self):
        return self.pname

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
        
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.IntegerField()
    messege = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
