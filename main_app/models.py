from django.db import models
from django.urls import reverse

# Create your models here.
class Collector(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('collectors_index', kwargs={'collector_id': self.id})

TYPES = (
  ('G', 'github'),
  ('D', 'deployed'),
)

class Website(models.Model):
  website = models.URLField()
  type = models.CharField(
    max_length=1,
    choices=TYPES,
    default=TYPES[0][0],
  )

  collector = models.ForeignKey(Collector, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.website} ({self.type} link)"


class Follower(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('followers_detail', kwargs={'pk': self.id})