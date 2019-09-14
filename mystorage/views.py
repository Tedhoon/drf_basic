from rest_framework import viewsets ,serializers
from .models import Essay 
from .serializers import EssaySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    def perform_create(self, serializer): # 자동으로 author_name을 등록
        serializer.save(author = self.request.user)