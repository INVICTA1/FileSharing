from .database import get_file_by_id
from django.shortcuts import render
from .admin import get_id
import json
from django.http import JsonResponse, HttpResponse
from django.views.generic import View


def get_file(request, file_id):
    if request.method != 'POST':
        resc = "post" + str(file_id)
    else:
        resc = "get" + str(file_id)

    cursor = get_id(file_id)
    print(resc)
    print(cursor)

    return JsonResponse(cursor)
    # return render(request, 'users/get_file.html', cursor)
