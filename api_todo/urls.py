

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"", views.TodoViewSet)


app_name = "todo"
urlpatterns = router.urls
