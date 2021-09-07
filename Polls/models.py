from django.db import models



class Messages(models.Model):
    username = models.CharField(max_length=300)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Chats(models.Model):
    title = models.CharField(max_length=200)
    disc = models.TextField(blank=True)
    messages = models.ManyToManyField(Messages, blank=True)

    def __str__(self):
        return self.title

    


