from django.db import models


class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('data_added',)

    def __str__(self):
        return f'Room: {self.room} - Username: {self.username}'
