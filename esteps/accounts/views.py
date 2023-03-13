from django.shortcuts import render
from django.http import JsonResponse
import asyncio
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import  Profile , Locations
import json
# Create your views here.

def login(request):
   
   # my_list = list(user.values())
    username = request.GET.get('username')
    password = request.GET.get('pwd')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        response_data = {'status': 200 , 'message': user.id}
    else:
        response_data = {'status': 404 , 'message': "wrong"}
        


    



    


    print('test')
    return JsonResponse(response_data,safe=False)


def get_profile(request):
        id = request.GET.get('id')
        user=User.objects.get(id=id)

        profile=Profile.objects.get(user=user)

        p={'username':user.username, 'photo' : profile.profile_picture.url,
           'role':profile.role
           }

        return JsonResponse( p ,safe=False);


def change_location(request):
     
     id= request.GET['id']
     la = request.GET['la']
     lo = request.GET['lo']


     user=User.objects.get(id=id)
     profile=Profile.objects.get(user=user)
     locations=Locations.objects.get(profile=profile)
     locations.latitude=la
     locations.longitude=lo
     locations.save()

     return JsonResponse({"wored":1},safe=False)

def get_location(request):
     id=request.GET['id']
     user=User.objects.get(id=id)
     profile=Profile.objects.get(user=user)
     locations=Locations.objects.get(profile=profile)

     return JsonResponse({"latitude":locations.latitude,"longitude":locations.longitude},safe=False)



     