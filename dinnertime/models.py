from django.db import models

# Create your models here.
class MainDish(models.Model):
    main_course = models.TextField()

class SideDish(models.Model):
     side_dish = models.TextField()
