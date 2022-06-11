from django.db import models

class JobModel(models.Model):
    job_id = models.PositiveBigIntegerField(primary_key=True)
    company = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    logo_url = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'my_table'
        indexes = [
            models.Index(fields=['job_id'], name='job_id')
        ]