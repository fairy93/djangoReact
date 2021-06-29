from django.db import models


class Post(models.Model):
    # sequence = models.AutoField(primary_key=True, default = 1000)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        managed =True
        db_table = 'posts'

    def __str__(self):
        return f'[{self.pk}] is username={self.sequence}'\
               f' title = {self.title}'\
               f'content = {self.content}'\
               f' created_at = {self.created_at}'\
               f' updated_at = {self.updated_at}'
