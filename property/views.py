from django.shortcuts import render,redirect,HttpResponse
from django.utils.encoding import smart_str
from .forms import ExcelFileForm
from rest_framework import viewsets 
from broker.models import Broker
from property.models import Property,Country,State,City
from property.serializers import PropertySerializer
import pandas as pd
import pytz
from django.utils import timezone

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


def import_data_from_excel(request):
    if request.method == 'POST':
        form = ExcelFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Read the Excel file
            df = pd.read_excel(request.FILES['file'])
            
            # Loop over rows and create objects with foreign key relationships
            for index, row in df.iterrows():
                broker = {
                    'name': row['broker'],
                    }
                broker, created = Broker.objects.get_or_create(**broker)

    
                property = {
                    'broker': broker,
                    'title': row['title'],
                    'address': row['address'],
                    'country': row['country'],
                    'state': row['state'],
                    'city': row['city'],
                    'zipcode': row['zipcode'],
                    'description': row['description'],
                    'price': row['price'],
                    'bedrooms': row['bedrooms'],
                    'bathrooms': row['bathrooms'],
                    'garage': row['garage'],
                    'sqft': row['sqft'],
                    'plot_size': row['plot_size'],
                    'status': row['status'],
                    'photo_main': row['photo_main'],
                    'is_published': row['is_published'],
                    
                }
                property = Property.objects.create(**property)
            
            # Return a response
            return render(request, 'pages/import_data.html', {'form': form, 'success': True})
    else:
        form = ExcelFileForm()
    
    return render(request, 'pages/import_data.html', {'form': form})


def export_data_to_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Properties.xlsx"'

    # Convert timezone-aware datetimes to a specific timezone or remove timezone information
    properties = Property.objects.all().values('broker','title', 'address', 'country','state','city', 'zipcode', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'plot_size', 'status','photo_main','photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'is_published','list_date')
    data = []
    for prop in properties:
        if prop['list_date'] is not None:
            prop['list_date'] = prop['list_date'].strftime('%Y-%m-%d %H:%M:%S')
        data.append(prop)

    # Write data to the response
    writer = pd.ExcelWriter(response, engine='xlsxwriter')
    df = pd.DataFrame(list(data))
    df.to_excel(writer, sheet_name='Properties', index=False)
    writer.save()

    return response

from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class StateList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        country=request.data['country']
        state={}
        if country:
            states=Country.objects.get(id=country).states.all()
            state={p.name:p.id for p in states}
        return JsonResponse(data=state, safe=False)

class CityList(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        state=request.data['state']
        city={}
        if state:
            cities=State.objects.get(id=state).cities.all()
            city={p.name:p.id for p in cities}
        return JsonResponse(data=city, safe=False)
