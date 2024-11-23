from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register("api/form", views.FormViewSet, basename='Form')

urlpatterns = router.urls