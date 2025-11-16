from django.db import models

# Create your models here.
class StatusCheckResult(models.Model):
    service_name = models.CharField(max_length=255)
    success = models.BooleanField()
    http_status_code = models.PositiveBigIntegerField(null=True, blank=True)
    response_time_ms = models.FloatField(null=True, blank=True)
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        status = "SUCCESS" if self.success else "FAIlED"
        