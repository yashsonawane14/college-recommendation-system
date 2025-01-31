from django.db import models

class CollegeData(models.Model):
    rank = models.IntegerField()
    percentile = models.FloatField()
    branch = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    category = models.CharField(max_length=255)
    fulfillment = models.CharField(max_length=255, null=True, blank=True)
    seat_type = models.CharField(max_length=255)
    primary_seat_type = models.CharField(max_length=255)
    secondary_seat_type = models.CharField(max_length=255)
    score_type = models.CharField(max_length=255)
    college_name = models.CharField(max_length=255)
    enrollment_no = models.CharField(max_length=255)
    branch_code = models.CharField(max_length=255)
