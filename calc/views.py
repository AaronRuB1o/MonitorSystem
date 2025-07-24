from django.shortcuts import render
from django.db import models
from .models import Monitoring
from django.db.models import Q
from django.http import JsonResponse

Columns = []

def monitoring(request):
    global Columns
    #Selects and records the selection of the user for the column
    selected_columns = request.GET.getlist('column')
    has_data = False
    data = None
    #Rearrange the data properly so it would be more easily readable and manipulatable
    if selected_columns:
        has_data = True 
        Columns = [col for col in selected_columns if col != 'action']

    #Searches the corresponding Columns and records it inside an array
    if has_data:
        data = []
        for item in Monitoring.objects.all():
            row = [(column, getattr(item, column, '')) for column in Columns]
            data.append(row)        
    else:
        Columns = []
        data = None 


    #Columns will be used to to show which of the columns should only be displayed.

    template = 'MonitorSystem/index.html'

    allData = Monitoring.objects.all()

    context = {
        'data': data,
        'Columns': Columns,
        "allData": allData
    }

    if request.GET.get('action') == 'Reset':
        Columns = []
        data = None
        context = {
            'data': data,
            'Columns': Columns,
            "allData": allData
        }
    return render(request, template, context)



def search_data(request):
    #Retrieves the selected column
    selected_columns = request.GET.getlist('column')
    #Retrieves the value the user wants to search.
    search_query = request.GET.get('search_query', '')

    #Searches for the data within the database
    q_objects = Q()
    if search_query:
        for field in Monitoring._meta.fields:
            if isinstance(field, models.CharField):
                q_objects |= Q(**{f"{field.name}__contains": search_query})

    if selected_columns:
        filtered_data = [{col: getattr(item, col, '') for col in Columns} for item in Monitoring.objects.filter(q_objects)]
    else:
        filtered_data = Monitoring.objects.filter(q_objects).values(*Columns)

    #records only the matching datas and put it in the list
    serialized_data = list(filtered_data)

    return JsonResponse(serialized_data, safe=False)


def companyTree(request):
    template = 'CompanyTree/index.html'

    return render(request, template)

