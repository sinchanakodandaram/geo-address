from django.shortcuts import render

import openpyxl
from django.http import HttpResponse
from openpyxl import Workbook
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent='geoadd')


def index(request):
    if "GET" == request.method:
        return render(request, 'index.html', {})
    # if not GET then proceed
    else:
        excel_file = request.FILES["excel_file"]
        if not excel_file.name.endswith('.xlsx'):
            return HttpResponse("File is not Excel type")

        wb = openpyxl.load_workbook(excel_file)
        wba = Workbook(write_only=True)
        ws = wba.create_sheet()

        # getting a particular sheet
        worksheet = wb["Sheet1"]

        # reading a cell
        excel_data = list()

        # iterating over the rows and
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                location = geolocator.geocode(cell.value)
                row_data.append(str(location.latitude))
                row_data.append(str(location.longitude))
                row_data.append(str(cell.value))
            excel_data.append(row_data)

        if excel_data:
            for line in excel_data:
                ws.append(line)

        wba.save('address.xlsx')

        return render(request, 'index.html', {"excel_data": excel_data})
