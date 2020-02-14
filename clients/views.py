from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm

def uploadCSV(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        return HttpResponse('success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})