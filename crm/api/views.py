from cgitb import lookup
from telnetlib import STATUS
from django.shortcuts import HttpResponse
from .serializers import LeadsSerializer
from .serializers import UserSerializer
from .models import Leads
#from .models import User
from django.contrib.auth.models import User

#from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import status
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
#from rest_framework.parsers import JSONParser

from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated




#Model ViewSEt 
class LeadViewset  (viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

class UserViewset  (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)






'''
#Generic View SEt with Mixins
class LeadViewset  (viewsets.GenericViewSet,
                    mixins.ListModelMixin ,
                     mixins.CreateModelMixin ,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin, ):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer






class LeadViewset  (viewsets.ViewSet):
    def list(self ,request):
        lead = Leads.objects.all()
        serializer = LeadsSerializer(lead,many = True)
        return Response (serializer.data)
    def create (self,request):
        serializer = LeadsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def retrieve (self,request,pk = None):
            queryset = Leads.objects.all()
            lead = get_object_or_404(queryset,pk=pk)
            serializer = LeadsSerializer(lead)
            return Response (serializer.data)
    def update  (self,request, pk= None):
            lead = Leads.objects.get (pk=pk)
            serializer = LeadsSerializer(lead,data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status= status.HTTP_201_CREATED)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def destroy  (self,request,pk=None):
            lead = Leads.objects.get(pk = pk)
            lead.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


          

         




        

    
    
'''








'''

class LeadList (generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer

  
    def get(self ,request): 
        return self.list(request)
    def post(self ,request): 
        return self.create(request)

        

    


class LeadDetails (generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer
    lookup_field = 'id'
    def get(self ,request,id): 
        return self.retrieve(request,id=id)
    def put(self ,request,id): 
        return self.update(request,id=id)
    def delete(self ,request,id): 
        return self.destroy(request,id=id)



#tree     model.Leads >> serializer.modelserializer.Leads >> view.serilizer >>url.view.function
#tree      Leads>>serilizer>>view>>Leads_List()>>url.Leads
'''

'''
#class without mixins
class LeadList (APIView):

    def get(self ,request):
        lead = Leads.objects.all()
        serializer = LeadsSerializer(lead,many = True)
        return Response (serializer.data)
    def post (self,request):
        serializer = LeadsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class LeadDetails (APIView):

    def get_object(self , id):
         try:
             return Leads.objects.get(id=id)

         except Leads.DoesNotExist:
             return  Response(status=status.HTTP_404_NOT_FOUND)

    def get(self ,request, id):  
        lead = self.get_object(id)
        serializer = LeadsSerializer(lead)
        return Response (serializer.data)
    
    def put(self ,request, id):  
        lead = self.get_object(id)
        serializer = LeadsSerializer(lead, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self ,request, id):  
        lead = self.get_object(id)
        lead.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        




'''






'''
#function base browsability django

@api_view(['GET','POST'])
def Leads_List(request, seializer=None):

    if request.method == 'GET':
        lead = Leads.objects.all()
        serializer = LeadsSerializer(lead,many = True)
        return Response (serializer.data)

    elif request.method == 'POST':

        serializer = LeadsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','PUT','DELETE'])
def leads_detail(request, pk, seializer=None):
    try:
     lead = Leads.objects.get(pk=pk)

    except Leads.DoesNotExist:
            return  Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        seializer = LeadsSerializer(lead)
        return Response(seializer.data)

    elif request.method == 'PUT' :

        serializer = LeadsSerializer(lead, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lead.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@csrf_exempt

def  Leads_List(request, serializer = None):
 if request.method == 'GET':
       lead = Leads.objects.all()
       serializer = LeadsSerializer(lead,many = True)
       return JsonResponse(serializer.data,safe=False)

 elif request.method == 'POST' :
       data = JSONParser().parse(request)
       serializer = LeadsSerializer(data=data)
       if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data,status=201)
       return JsonResponse(serializer.errors,status=400)


@csrf_exempt

def leads_detail( request,pk):
    try:
       lead = Leads.objects.get(pk=pk)
    except Leads.DoesNotExist:
       return  JsonResponse (status=404)

    if  request.method == 'GET':
      serializer = LeadsSerializer(lead)
      return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LeadsSerializer(lead, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400) 

    elif request.method=='DELETE':
       lead.delete()
       return HttpResponse(status=204)



'''


# Create your views here.
# return render (request ,'index.html')

#def Index (request):
   # return HttpResponse("it is working")