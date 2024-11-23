from django_filters import FilterSet
from .models import Form

class FormFilter(FilterSet):
    class Meta:
        model = Form
        fields = [
            'Name', 'FatherName', 'GuardianName', 'MotherName', 
            'DateofBirth', 'class1', 'SubjectName', 'School', 
            'Board', 'Address', 'ContactNo', 'Email', 
            'DateofJoining', 'AgreeToDeclaration'
        ]