from django.db import models

# Create your models here.
class ListOfCommonSpaces(models.Model):
    domain = models.CharField(max_length=30)
    SpaceName = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    Capacity = models.IntegerField() 
    availability = models.JSONField(default=dict) #THIS IS TAKING NOTE OF ALL THE AVAILABLE DATE AND TIME
    ReservationRestrictions = models.CharField(max_length=50, null=True)
    AdditionalFeatures = models.CharField(max_length=50, null=True)
    #Images - Milestone 3


class ListOfBookings(models.Model):
    #BOOKING ID - ID (default)
    placeid = models.IntegerField()
    domain = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    bookingdate = models.DateField()
    bookingday = models.CharField(max_length=10) 
    starttime = models.TimeField()
    endtime = models.TimeField()
    currentstatus = models.CharField(max_length=30) #scheduled, ongoing, cancelled (ideally must be removed)
    
class ListOfPastBookings(models.Model):
    bookingid = models.IntegerField()
    placeid = models.IntegerField()
    domain = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    bookingdate = models.DateField()
    bookingday = models.CharField(max_length=10) 
    starttime = models.TimeField()
    endtime = models.TimeField()
    currentstatus = models.CharField(max_length=30) #completed, cancelled 
    
    #########################################
    #                                       #
    # Status can be one of the following    #
    #                                       #
    # * Scheduled                           #
    # * Ongoing                             #
    # * Completed                           #
    # * Cancelled                           #
    #                                       #
    #########################################

class CompanyInfo(models.Model):
    domain = models.CharField(max_length=30)
    timezone = models.CharField(max_length=30)
