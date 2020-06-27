import socket

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from .models import Document
from datetime import timedelta

def simple_upload(request):
    try:
        if request.method == 'POST' and request.FILES['file']:
            doc = Document()
            myfile = request.FILES['file']
            if myfile.size > 100000000:
                return render(request, 'mysite/home.html', {'error_size': "Please keep filesize under 100Mb. "})
            else:
                # install_password_file(myfile)
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                doc.name = filename
                doc.url = socket.gethostbyname(socket.gethostname())+uploaded_file_url
                duration = request.POST['duration']
                file_duration = get_duration(duration)
                doc.expires_doc = doc.uploaded_at + file_duration
                if request.user.is_authenticated:
                    doc.owner = request.user
                    doc.save()
                else:
                    doc.save()
                return render(request, 'mysite/home.html', {
                    'uploaded_file_url': uploaded_file_url
                })
        return render(request, 'mysite/home.html')
    except MultiValueDictKeyError:
        return render(request, 'mysite/home.html', {'error_file': "Please select a file. "})


def get_duration(dur):
    durations = {
        '1d': timedelta(days=1),
        '3d': timedelta(days=3),
        '7d': timedelta(days=7),
        '30d': timedelta(days=30)
    }
    for d in durations:
        if d == dur:
            return durations[d]
    return timedelta()
