from django.contrib import admin
import pandas as pd
from django.http import HttpResponse
from django.utils import timezone
from property.models import Property
from broker.models import Broker
import pytz


# class PropertyAdmin(admin.ModelAdmin):
    
#   list_display = ('id', 'title', 'address', 'city', 'state', 'description', 'price')
#   list_display_links = ('id', 'title')
#   list_filter = ('title',)
#   list_editable = ('address', 'city', 'state', 'description', 'price')
#   search_fields = ('title', 'address', 'description')
#   list_per_page = 25
    
# admin.site.register(Property, PropertyAdmin)




# @admin.action(description='Export to Excel')
# def export_to_excel(modeladmin, request, queryset):
#     # Retrieve the data from the model
#     data = queryset.values()

#     # Convert the datetimes to timezone-unaware datetimes
#     for row in data:
#         for field in row:
#             if isinstance(row[field], timezone.datetime):
#                 row[field] = row[field].replace(tzinfo=None)

#     # Convert the data to a pandas DataFrame
#     df = pd.DataFrame.from_records(data)

#     # Create a response object with the Excel file
#     response = HttpResponse(content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=Properties.xlsx'

#     # Write the DataFrame to the response object
#     writer = pd.ExcelWriter(response, engine='xlsxwriter')
#     df.to_excel(writer, index=False)
#     writer.save()

#     return response

# @admin.action(description='Import data from Excel')
# def import_data(modeladmin, request, queryset):
#     # Load the Excel file into a pandas DataFrame
#     df = pd.read_excel('property\property.xlsx')    

#     # Iterate over the DataFrame rows and create model instances
#     for index, row in df.iterrows():
#         broker = {
#             'name': row['broker'],
            
#         }
#         broker, created = Broker.objects.get_or_create(**broker)

#         data = {
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
#         Property.objects.create(**data)

# class MyModelAdmin(admin.ModelAdmin):
#     list_display = ['broker','title','address','city','state', 'zipcode',  'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'plot_size', 'status', 'photo_main','is_published','list_date']
#     actions = [export_to_excel]

# admin.site.register(Property, MyModelAdmin)

from import_export.admin import ImportExportModelAdmin
from .resources import BrokerResource, PropertyResource
@admin.register(Broker)
class BrokerAdmin(ImportExportModelAdmin):
    resource_class = BrokerResource

@admin.register(Property)
class PropertyAdmin(ImportExportModelAdmin):
    resource_class = PropertyResource

