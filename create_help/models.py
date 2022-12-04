from django.db import models
from django.db.models import CharField
import uuid


class HelpTicket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField()
    response = models.TextField()

    class Meta:
        db_table = 'help_ticket'