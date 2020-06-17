from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pymysql.cursors
from .models import Document
from .forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'mysite/index.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'mysite/upload_file.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'mysite/upload_file.html')
