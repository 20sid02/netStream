from django.shortcuts import render, get_object_or_404
from .models import Folder, MediaFiles
from django.conf import settings
import os

def index(request):
    folders = ['Music', 'Movies', 'Photos']
    return render(request, 'index.html', {'folders' : folders})

def folder_view(request, folder_name):
    folder_path = os.path.join(settings.MEDIA_ROOT, folder_name)
    try:
        files = os.listdir(folder_path)
    except FileNotFoundError:
        files = []
    return render(request, 'folder.html', {
        'folder_name': folder_name,
        'files': files,
        'media_url': settings.MEDIA_URL + folder_name + '/'
    })

def player_view(request, file_id):
    file = get_object_or_404(MediaFiles, id=file_id)
    return render(request, 'player.html', {'file' : file})
