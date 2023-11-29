from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . serilaizer import AddressSerlaizers
from.models import Address
from rest_framework.decorators import api_view

@api_view(["GET","POST"])
def index(request):
    if request.method=="GET":
        address=Address.objects.all()
        Serilaizer=AddressSerlaizers(address,many=True)
        return JsonResponse(Serilaizer.data,safe=False)
    if request.method=="POST":
        serilaizer=AddressSerlaizers(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return JsonResponse(serilaizer.data, safe=False)
    return JsonResponse()
def deatails(request,id):
    address=Address.objects.get(id=id)
    serilaizer=AddressSerlaizers(address)
    return JsonResponse(serilaizer.data)
