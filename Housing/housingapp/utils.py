# utils.py
from django.utils import timezone
from .models import SavedProperty

def delete_old_saved_properties():
    expiry = timezone.now() - timezone.timedelta(min=1)
    SavedProperty.objects.filter(timestamp__lt=expiry).delete()


    
