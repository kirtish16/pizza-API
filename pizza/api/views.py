from django.http.response import HttpResponseNotFound

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

from .models import *
from .serializers import *

# Provides an overview of all api calls
@api_view(['GET'])
def apiOverview(request):
    apiUrls = {
        'List': '/pizza-list',
        'Detail': '/pizza-detail/<str:pid>/',
        'Create': '/pizza-create',
        'Update': '/pizza-update/<str:pid>',
        'Delete': '/pizza-delete/<str:pid>',
        'Filter by type': '/pizza-filter/type/<str:ptype>',
        'Filter by size': '/pizza-filter/size/<str:psize>',
    }
    return Response(apiUrls)

# Returns list of all objects of model
@api_view(['GET'])
def pizzaList(request):
    pizzas = Pizza.objects.all()
    serializer = pizzaSerializers(pizzas, many=True)
    return Response(serializer.data)

# Returns the details of object of given object id
@api_view(['GET'])
def pizzaDetail(request, pid):
    # Gets object from model passed and if that object or model doesn’t exist it raise 404 error.
    pizzas = get_object_or_404(Pizza, id=pid)
    serializer = pizzaSerializers(pizzas, many=False)
    return Response(serializer.data)


# Creates an object of the model pizza
@api_view(['POST'])
def pizzaCreate(request):
    print(request.data)
    serializer = pizzaSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


# Updates an object of the model pizza
@api_view(['POST'])
def pizzaUpdate(request, pid):
    pizzaObject = get_object_or_404(Pizza, id=pid)
    serializer = pizzaSerializers(instance=pizzaObject, data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)

#Delete the object using object id
@api_view(['GET'])
def pizzaDelete(request, pid):
    # Gets object from model passed and if that object or model doesn’t exist it raise 404 error.
    try:
        pizzas = get_object_or_404(Pizza, id=pid)   
        pizzas.delete()
        return Response("Item deleted successfully",status=status.HTTP_200_OK)
    except:
        return Response("Inavlid pizza id",status=status.HTTP_404_NOT_FOUND)


# Filter all pizza order by Pizza Type
@api_view(['GET'])
def pizzaFilterbyType(request,ptype):
    #List containing all the allowed pizza types
    type_allowed = ['Regular','Square']
    if ptype not in type_allowed:
        return Response("Invalid pizza type",status=status.HTTP_404_NOT_FOUND)
    pizzas = Pizza.objects.filter(type=ptype)
    serializer = pizzaSerializers(pizzas, many=True)
   
    return Response(serializer.data)

# Filter all pizza order by Pizza Size
@api_view(['GET'])
def pizzaFilterbySize(request,psize):
    #List containing all the allowed pizza types
    size_allowed = ['Small','Medium','Large']
    if psize not in size_allowed:
        return Response("Invalid pizza size",status=status.HTTP_404_NOT_FOUND)
    pizzas = Pizza.objects.filter(size=psize)
    serializer = pizzaSerializers(pizzas, many=True)
   
    return Response(serializer.data)


