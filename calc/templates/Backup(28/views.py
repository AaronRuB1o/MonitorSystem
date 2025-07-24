from django.shortcuts import render
from django.db import models
from .models import Monitoring
from django.db.models import Q
from django.http import JsonResponse

Columns = []

def your_view(request):
    global Columns
    
    if request.method == 'GET':
        selected_columns = request.GET.getlist('column')
        search_query = request.GET.get('search_query')


    if selected_columns:
        Columns = [col for col in selected_columns if col != 'action']

    if search_query:
        q_objects = Q()
        for field in Monitoring._meta.fields:
            if isinstance(field, models.CharField):
                q_objects |= Q(**{f"{field.name}__exact": search_query})
        searched_data = []
        for item in Monitoring.objects.filter(q_objects):
            row = [(column, getattr(item, column, '')) for column in Columns]
            searched_data.append(row)
    else:
        searched_data = None
    
    data = []
    for item in Monitoring.objects.all():
        row = [(column, getattr(item, column, '')) for column in Columns]
        data.append(row)

    Odata = Monitoring.objects.all()

    template = 'MonitorSystem/index.html'
    searched = bool(search_query)
    filter = bool(Columns)

    context = {
        'name': 'Delubio',
        'data': data,
        'searched_data': searched_data,
        'searched': searched,
        'filter': filter,
        'Columns': Columns,
        'Odata': Odata
    }

    if request.GET.get('action') == 'Reset':
        Columns = []
        searched_data = None
        data = []
        context = {
            'name': 'Delubio',
            'data': data,
            'searched_data': searched_data,
            'searched' : searched,
            'filter': filter,
            'Columns': Columns,
            'Odata': Odata
        }
        return render(request, 'MonitorSystem/index.html', context)
    elif request.GET.get('action') == 'Filter' or request.GET.get('search_query'):
        if 'search_query' in request.GET:
            searched = True
        elif request.GET.get('action') == 'Filter':
            filter = True 
        context = {
            'name': 'Delubio',
            'data': data,
            'searched_data': searched_data,
            'searched': searched,
            'filter': filter,
            'Columns': Columns,
            'Odata': Odata
        }                                
        return render(request, 'MonitorSystem/Filtered_index.html', context)   
    
    return render(request, template, context)


def search_data(request):
    search_query = request.GET.get('search_query', '')

    # Create a Q object to combine queries for each field
    q_objects = Q()
    for field in Monitoring._meta.fields:
        if isinstance(field, models.CharField):
            q_objects |= Q(**{f"{field.name}__contains": search_query})

    # Perform the search based on the combined Q object
    searched_data = Monitoring.objects.filter(q_objects)
    
    serialized_data = [{'Site': item.Site, 'PC_tag': item.PC_tag, 'MAC': item.MAC, 
                        'User': item.User, 'Local_IP': item.Local_IP, 
                        'Patch_V2': item.Patch_V2, 'vpncfg_nc': item.vpncfg_nc, 
                        'x_scr': item.x_scr, 'x_zm': item.x_zm, 
                        'ldap_ipa2': item.ldap_ipa2, 'ldaprs': item.ldaprs, 
                        'chmd_ipa': item.chmd_ipa, 'incog': item.incog} for item in searched_data]

    return JsonResponse(serialized_data, safe=False)


def search_data(request):
    selected_columns = request.GET.getlist('column')
    search_query = request.GET.get('search_query', '')

    q_objects = Q()
    if search_query:
        for field in Monitoring._meta.fields:
            if isinstance(field, models.CharField):
                q_objects |= Q(**{f"{field.name}__contains": search_query})

    data = []
    if selected_columns:
        for item in Monitoring.objects.filter(q_objects):
            row = {col: getattr(item, col, '') for col in selected_columns}
            data.append(row)
    else:
        data = Monitoring.objects.filter(q_objects).values(*selected_columns)

    serialized_data = list(data)

    return JsonResponse(serialized_data, safe=False)