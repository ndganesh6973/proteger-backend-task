from rest_framework import viewsets
from .models import Task
from django.contrib.auth.models import User
from .serializers import TaskSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Bonus: Filter tasks by status [cite: 43, 44]
    def get_queryset(self):
        status = self.request.query_params.get('status')
        if status:
            return Task.objects.filter(status=status)
        return Task.objects.all()