from rest_framework import viewsets, permissions
from .models import Trip, Application
from .serializers import TripSerializer, ApplicationSerializer, ApplicationListSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .tasks import create_application_async


class TripPublicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [permissions.AllowAny]

class ApplicationPublicViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    # serializer_class = ApplicationListSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post']

    def get_serializer(self, *args, **kwargs):
        if
        return super().get_serializer(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = ApplicationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print('ok')
        # Запускаем асинхронную задачу
        task = create_application_async.delay(serializer.validated_data)
        
        # Немедленно возвращаем ответ
        return Response(
            {'status': 'processing', 'task_id': task.id},
            status=status.HTTP_202_ACCEPTED
        )




class TripPrivateViewSet(viewsets.ModelViewSet):
    print('serializer.data')
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)  # Добавляем парсеры файлов

    def perform_create(self, serializer):
        print(self.request.FILES.get('photo'))
        serializer.save(photo=self.request.FILES.get('photo'))


class ApplicationPrivateViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
