from django.db import models

# Create your models here.


class Post(models.Model):
    BOAST = "B"
    ROAST = "R"
    choices = [(BOAST, "Boast"), (ROAST, "Roast")]
    date = models.DateTimeField(auto_now=True)
    post = models.CharField(max_length=180)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    # vote_total = models.IntegerField(default=0)
    boast_or_roast_choice = models.CharField(choices=choices, max_length=1)

    def __str__(self):

        return self.post

    def vote_total(self):
        return self.up_vote + self.down_vote
