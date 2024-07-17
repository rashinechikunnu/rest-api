from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop_app.models import person
from .serializer import personSerializer

# Create your views here.
@api_view(['GET','POST','PUT'])

def index(request):
    if request.method == 'GET':
        people_details={
            'name': 'rashi',
            'age' : 20,
            'palce' : 'arimbra'
        }
        return Response(people_details)
    
    elif request.method == 'POST':
        return Response('THIS METHOD IS POST')
    

    elif request.method == 'PUT':
        return Response('THIS METHOD IS PUT')



#   MODEL SERIALIZER

@api_view(['GET','POST','PUT','PATCH','DELETE'])

def persons(request):
    if request.method == 'GET':
        obj1 = person.objects.filter(team__isnull=False)
        serialzer = personSerializer(obj1,many=True)
        return Response(serialzer.data)
    
    elif request.method == 'POST':
        data = request.data
        serialzer = personSerializer(data=data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        return Response(serialzer.errors)
    
    elif request.method == 'PUT' :
        data = request.data
        obj = person.objects.get(id=data['id'])
        serialzer = personSerializer(obj,data=data,partial=False)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        return Response(serialzer.errors)
    
    elif request.method == 'PATCH':
        data= request.data
        obj=person.objects.get(id=data['id'])
        serialzer = personSerializer(obj,data=data,partial=True)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        return serialzer(serialzer.errors)
    
    else:
        data = request.data
        obj = person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message':'person deleted'})
