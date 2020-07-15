from django.db import models


class Topic(models.Model):
    """Topic, that user stydies"""

    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text