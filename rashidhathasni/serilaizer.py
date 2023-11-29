from rest_framework import serializers
from.models import Address

class AddressSerlaizers(serializers.ModelSerializer):
    class Meta:
     model=Address
     fields=['id','name','phone']