# django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime
from django.shortcuts import get_object_or_404
# rest_framework
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
# local storage
from . import serializers
from . import models
import csv, xlwt

def index(request):
    return render(request, 'index.html')

def Exp_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=Expense' + str( datetime.now() ) +'.csv'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email'])

    useradd = models.UserAdd.objects.all()

    for user in useradd:
        writer.writerow([user.firstName,user.lastName, user.email])

    return response



def Exp_excel(request):
    response = HttpResponse(content_type='text/ms-excel')
    response['Content-Disposition']='attachment; filename=Expense' + str( datetime.now() ) +'.xls'

    wb = xlwt.workbook(encoding='utf-8')
    ws = wb.add_sheet('Excel')
    writer.writerow(['First Name', 'Last Name', 'Email'])

    useradd = models.UserAdd.objects.all()

    for user in useradd:
        writer.writerow([user.firstName,user.lastName, user.email])

    return response





class AddUserDetail(views.APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add_user.html'

    def get(self, request, *args, **kwargs):
        serializer = serializers.UserAddSerializer()
        return Response({'serializer': serializer})

    def post(self, request, *args, **kwargs):
        print('data---',request.data)
        data = request.data

        avatar = data.get('profile_avatar',None)
        firstName = data.get('firstname',None)
        lastName = data.get('lastname', None)
        companyName = data.get('companyname', None)
        contactPhone =data.get('phone', None)
        email = data.get('email', None)
        companySite = data.get('companywebsite', None)
        language = data.get('language', None)
        timeZone = data.get('timezone', None)
        communication =data.get('communication', None)
        passwordRV = data.get('passwordRV')
        address1 = data.get('address1', None)
        address2 = data.get('address2', None)
        postcode = data.get('postcode', None)
        city = data.get('city', None)
        state = data.get('state', None)
        country = data.get('country', None)

        data_dict = {
            'avatar' : avatar,
            'firstName' : firstName,
            'lastName'  : lastName,
            'companyName'  : companyName,
            'contactPhone'  : contactPhone,
            'email'  : email,
            'companySite'  : companySite ,
            'language'  : language,
            'timeZone'  : timeZone,
            'communication'  : communication,
            # 'passwordRV'  : passwordRV ,
            'address1'  : address1,
            'address2'  : address2,
            'postcode'  : postcode,
            'city'  : city,
            'state'  : state,
            'country'  : country, 
        }
        serializer = serializers.UserAddSerializer(data=data_dict)
        if serializer.is_valid():
            serializer.save()
            msgs = [
                serializer.data
            ]
            return redirect('/')
           
        errors = [
            str(serializer.errors)
        ]
        print(errors)
        messages.info(request,errors)
        return redirect('/adduser')
