from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *

import pickle
# Create your views here.

def finder(request,data):
	queryset = DF_Model.objects.filter(warehouse=data['warehouse'], product_category=data['product_category'], date=data['date'])
	processed_data = [{"warehouse": obj.warehouse,
                       "product_category": obj.product_category,
                       "date": obj.date}
                      for obj in queryset]
	print("Processed data:", processed_data)

	actual = processed_data[-1]
	# {'warehouse': 'Hello', 'product_category': 'dfjklsdf', 'date': datetime.date(2023, 1, 17)}

	d = actual['date']
	print()
	# print(d.year)
	# print(d.month)
	# print(d.day)

	day_of_week = d.weekday()

	# Map the integer to the corresponding day name
	day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	day_name = day_names[day_of_week]

	with open("webApp/Weekday.h", "rb") as Weekday:
		Weekday_bin = pickle.load(Weekday)
	with open("webApp/Warehouse.h","rb") as Warehouse:
		Warehouse_bin = pickle.load(Warehouse)
	with open("webApp/Product_Category.h","rb") as Product:
		Product_bin = pickle.load(Product)

	warehouse_detail = Warehouse_bin.transform([actual['warehouse']])
	Product_detail = Product_bin.transform([actual['product_category']])
	weekday_detail = Weekday_bin.transform([day_name])

	lst = [0,warehouse_detail,Product_detail,int(d.day),int(d.month),int(d.year),weekday_detail]

	with open("webApp/model.h", "rb") as model:
		loaded_model = pickle.load(model)

	preds = loaded_model.predict([lst])
	print(preds)
	return {"order":preds[0]}

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
			result = finder(request,serializer._validated_data)
			return Response(result)	
