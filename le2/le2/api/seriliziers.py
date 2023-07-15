from rest_framework import serializers

from .models import Student

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=20, validators = name_start_with_r)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=20)
    
    
    
#     # there are 3 types of validations which are as follows
#     # field level validation  in this we can specify custom field-level validation by adding validate_fieldName() method to our serilizers subclass
#     def validate_roll(self,value):
#         if value >= 100:
#             raise serializers.ValidationError('seat full')
#         return value
        
#     # object level validdation
#     # when we need to validate multiple fields we do object level validation by adding the method validate() to serilizers subclass 
#     def validate(self, data):
#         na = data.get('name')
#         ct = data.get('city')
#         if na.lower()=='sudip' and ct.lower()!='kathmandu':
#             raise serializers.ValidationError('city must be kathmandu')
#         return data
    
    # validators
def name_start_with_r(value):
    if value[0]!='r':
        raise serializers.ValidationError('Name Must be start with R ')
        
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, validators=[name_start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=20)
    #create or insert data method
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    #update meethod
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance