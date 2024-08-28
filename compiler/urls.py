from django.urls import path
from .views import CodeExecutionView, index

urlpatterns = [
    path('execute/', CodeExecutionView.as_view(), name='code-execution'),
    path('', index, name='index'),
]
