from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # هر کاربر فقط وظایف خودش را می‌بیند
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # هنگام ساخت وظیفه جدید، کاربر را خودکار ثبت می‌کند
        serializer.save(user=self.request.user)