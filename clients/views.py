from django.shortcuts import render
from django.http import HttpResponse
import csv
from .forms import UploadFileForm
from .models import Client


def uploadCSV(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        importCSVFile(request.FILES['file'])
        return HttpResponse('success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def importCSVFile(file):
    """ Reads uploaded CSV file, converts it to string
        Saves into database using Django's bulk_create
        which uses a single SQL query regardless of the
        number of clients to save """
    str_text = ""
    for line in file:
        str_text += line.decode()
    reader = csv.DictReader(str_text.splitlines())
    clienti = [map_rows_to_fields(row) for row in reader]
    Client.objects.bulk_create([
        Client(**client) for client in clienti
        if not Client.objects.filter(id=client['id'])
    ])
    

# Helper function to convert read CSV to key_value pairs 
# that match the Client model
def map_rows_to_fields(row):
    csv_fields_to_model_fields = {
        'Codice Cliente (id)': 'id',
        'Codice Fiscale': 'codice_fiscale',
        'Ragione Sociale/Cognome': 'ragione_cognome',
        'Nome': 'nome',
        'Indirizzo': 'indirizzo',
        'Cap': 'cap',
        'Comune': 'comune',
        'Provincia': 'provincia',
        'Codice Stato (IT)': 'stato',
        'Email': 'email'
    }
    return {
        csv_fields_to_model_fields[key]: value
        for key, value in row.items()
    } 