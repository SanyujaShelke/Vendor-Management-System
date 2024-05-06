# vendors/models.py
from django.db import models
from django.db.models import Count, Avg, F, ExpressionWrapper, FloatField, Value
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    on_time_delivery_rate = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])


    def update_performance_metrics(self):
        # Calculate on-time delivery rate
        completed_orders = self.purchaseorder_set.filter(status='completed')
        total_completed_orders = completed_orders.count()
        if total_completed_orders > 0:
            on_time_deliveries = completed_orders.filter(delivery_date__lte=F('acknowledgment_date')).count()
            self.on_time_delivery_rate = (on_time_deliveries / total_completed_orders) * 100
        else:
            self.on_time_delivery_rate = 0

        # Calculate quality rating average
        self.quality_rating_avg = completed_orders.aggregate(avg_quality=Avg('quality_rating'))['avg_quality'] or 0

        # Calculate average response time
        response_times = completed_orders.annotate(response_time=ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=FloatField()))
        self.average_response_time = response_times.aggregate(avg_response=Avg('response_time'))['avg_response'] or 0

        # Calculate fulfillment rate
        total_orders = self.purchaseorder_set.count()
        if total_orders > 0:
            fulfilled_orders = completed_orders.filter(issue_date__lte=F('acknowledgment_date'))
            self.fulfillment_rate = (fulfilled_orders.count() / total_orders) * 100
        else:
            self.fulfillment_rate = 0

        self.save()

class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50, unique=True)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, created, **kwargs):
    if created or instance.status == 'completed':
        instance.vendor.update_performance_metrics()

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
