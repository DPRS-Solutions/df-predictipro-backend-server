from rest_framework import serializers
from . models import *

class DFSerializer(serializers.ModelSerializer):
	class Meta:
		model = DF_Model
		fields = ['warehouse', 'product_category','date']
