from rest_framework import serializers
from .models import Form

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = [
            'Name', 'FatherName', 'GuardianName', 'MotherName', 
            'DateofBirth', 'class1', 'SubjectName', 'School', 
            'Board', 'Address', 'ContactNo', 'Email', 
            'DateofJoining', 'AgreeToDeclaration'
        ]