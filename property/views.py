from django.shortcuts import render,redirect,HttpResponse
from django.utils.encoding import smart_str
from .forms import ExcelFileForm
from rest_framework import viewsets 
from property.models import Property
from broker.models import Broker
from property.serializers import PropertySerializer
import pandas as pd
import pytz
from django.utils import timezone


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

# def export_data_to_excel(request):
#     objs = Property.objects.all()
#     data = []

#     for obj in objs:
#         data.append({
#             "broker" : obj.broker,
#             "title" : obj.title,
#             "address" : obj.address,
#             "city" : obj.city,
#             "state" : obj.state,
#             "zipcode" : obj.zipcode,
#             "description" : obj.description,
#             "price" : obj.price,
#             "bedrooms" : obj.bedrooms,
#             "bathrooms" : obj.bathrooms,
#             "garage" : obj.garage,
#             "sqft" : obj.sqft,
#             "plot_size" : obj.plot_size,
#             "status" : obj.status,
#             "photo_main" : obj.photo_main,
#             "photo_1" : obj.photo_1,
#             "photo_2" : obj.photo_2,
#             "photo_3" : obj.photo_3,
#             "photo_4" : obj.photo_4,
#             "photo_5" : obj.photo_5,
#             "photo_6" : obj.photo_6,
#             "is_published" : obj.is_published,
            
#         })

#     pd.DataFrame(data).to_excel('property.xlsx')
#     return redirect('dashboard')

# def import_data_from_excel(request):
#     df = pd.read_excel('property\property.xlsx')
    
#     for index, row in df.iterrows():
#         broker = {
#             'name': row['broker'],
            
#         }
#         broker, created = Broker.objects.get_or_create(**broker)

    
#         property = {
#             'broker': broker,
#             'title': row['title'],
#             'address': row['address'],
#             'city': row['city'],
#             'state': row['state'],
#             'zipcode': row['zipcode'],
#             'description': row['description'],
#             'price': row['price'],
#             'bedrooms': row['bedrooms'],
#             'bathrooms': row['bathrooms'],
#             'garage': row['garage'],
#             'sqft': row['sqft'],
#             'plot_size': row['plot_size'],
#             'status': row['status'],
#             'photo_main': row['photo_main'],
#             'is_published': row['is_published'],
            
#         }
#         property = Property.objects.create(**property)
#     return redirect('dashboard')


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
                    'city': row['city'],
                    'state': row['state'],
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
    properties = Property.objects.all().values('broker','title', 'address', 'city', 'state', 'zipcode', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'plot_size', 'status','photo_main','photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'is_published','list_date')
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
