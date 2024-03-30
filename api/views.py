from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Movie
from api.serializers import MovieSerializer
from rest_framework import status

#localhost:8000/helloworld/
# method:get()
class HelloWorldView(APIView):
    def get(self,request,*args,**kwargs):
        context = {"message":"helloworld"}
        return Response(data=context)

#localhost:8000/morning/
# method:get()   
class MorningView(APIView):
    def get(self,request,*args,**kwargs):
        context = {"message":"Good Morning"}
        return Response(data=context)

#url=localhost:8000/addition/
#method=post()
# data={"num1"=100 ,"num2"=20}
    
class AdditionView(APIView):
    def post(self,request,*args,**kwargs):
        n1 = request.data.get("num1")
        n2 = request.data.get("num2")
        result= int(n1)+int(n2)
        context={"result":result}
        return Response(data=context)

#url=localhost:8000/bmi/
#method=post()
# data={"height=165","weight"=50}
    
class BmiView(APIView):
    def post(self,request,*args,**kwargs):
        height_in_cm = request.data.get("height")
        weight = request.data.get("weight")

        height_in_m=height_in_cm/100
        bmi=weight/(height_in_m)**2
        context={"bmi":bmi}
        return Response(data=context)


#url=localhost:8000/calories/
#method=post()
# data={"height":160,"weight":50,"age":25,"gender":male}
    
class CalorieView(APIView):
    def post(self,request,*args,**kwargs):
        height=int(request.data.get("height"))
        weight=int(request.data.get("weight"))
        age=int(request.data.get("age"))
        gender=(request.data.get("gender"))

        bmr=0
        if gender == "male":
            bmr=(10*weight)+(6.25*height)-(5*age)+5
        elif gender == "female":
            bmr=(10*weight)+(6.25*height)-(5*age)-161

        context={"bmr":bmr}
        return Response(data=context)


# ALBUM CRUD
    
# --------API for listing all albums--------
#         url:localhost:8000/api/albums/
#         method:get()
#         data: nil

# --------API for creating new album--------
#         url:localhost:8000/api/albums/
#         method:post()
#         data: {}  

class AlbumListView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all()
        return Response(data=qs)

    
    def post(self,request,*args,**kwargs):

        context={"message":"logic for creating new album"}  
        # movie_obj=Movie.objects.create(
        #     title=request.data.get("title"),
        #     director=request.data.get("director"),
        #     genre=request.data.get("gentre"),
        #     run_time=request.data.get("run_time"),
        #     language=request.data.get("language"),
        #     year=request.data.get("year"),
        # )
        return Response(data=context)


# -----------------------------------------------------------------------
class MovieListCreateView(APIView):

    def get(self,request,*args,**kwargs):
        qs=Movie.objects.all()
        serializer_instance=MovieSerializer(qs,many=True)   #serialization
        return Response(data=serializer_instance.data)
    
    def post(self,request,*args,**kwargs):
        data=request.data
        serializer_instance=MovieSerializer(data=data)  #deserialization
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        return Response(data=serializer_instance.errors)


# url:localhost:8000/api/movies/{id}/
# method:get()
class MovieRetriveUpdateDestroyView(APIView):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        try:
            qs=Movie.objects.get(id=id)
            serializer_instance=MovieSerializer(qs)
            return Response(data=serializer_instance.data)
        except:
            context={"message":"requested resource does not exist"}
            return Response(data=context,status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")

        try:
            Movie.objects.get(id=id).delete()
            return Response(data={"message":"deleted"},status=status.HTTP_200_OK)
        
        except:
            return Response(data={"message":"resourse not found"},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        data=request.data
        movie_object=Movie.objects.get(id=id)
        serializer_instance=MovieSerializer(data=data,instance=movie_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)