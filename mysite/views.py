from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Document
from django.urls import reverse

def home(request):
    documents = Document.objects.all()
    return render(request, 'mysite/index.html', {'documents': documents})


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


@login_required
def user_files(request):
    if request.method != 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'mysite/index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'mysite/index.html')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('mysite:ipload_file'))
