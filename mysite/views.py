from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from FileSharing.mysite.models import Document
from FileSharing.mysite.forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'users/index.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'users/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'users/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'users/model_form_upload.html', {
        'form': form
    })
