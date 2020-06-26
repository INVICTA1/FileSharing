from .models import Document
from django.utils import timezone


def delete_database():
    documents = Document.objects.all()
    for doc in documents:
        if doc.expires_doc <= timezone.now():
            doc.delete()