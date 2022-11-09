from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Student, Query
from django.db import models

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from django.db import connection


def my_custom_sql(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
    return columns, row


def api(request):
    header, data = list(my_custom_sql(Query.objects.get(pk=1).query))
    return JsonResponse({'data': data, 'header': header})


# class api(APIView):
#     def get(self, request):
#         """
#         Return a list of all users.
#         """
#         names = [e.name for e in Student.objects.raw(Query.objects.get(pk=1).query)]
#         return jsonResponse(names)


def home(request):
    header, data = list(my_custom_sql(Query.objects.get(pk=1).query))
    return render(request, 'index.html', {'data': data, 'header': header})
