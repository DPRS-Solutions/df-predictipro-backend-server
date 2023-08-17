from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
# Create your views here.

class DFView(APIView):
	
	serializer_class = DFSerializer

	def get(self, request):
		data = [ {"warehouse": data.warehouse,
	    		  "product_category": data.product_category,
				  "date": data.date}
		for data in DF_Model.objects.all()]
		return Response(data)

	def post(self, request):
		serializer = DFSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)	
