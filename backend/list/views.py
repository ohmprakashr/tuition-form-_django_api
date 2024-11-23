from rest_framework.viewsets import ModelViewSet
from .models import Form
from .serializers import FormSerializer

class FormViewSet(ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer