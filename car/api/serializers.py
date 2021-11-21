from rest_framework.serializers import ModelSerializer
from car.models import Car

class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'model','year','color','plate_number'
        ]
        read_only_fields = ['owner'] 
