from rest_framework import viewsets ,serializers
from .models import Essay , Album , Files
from .serializers import EssaySerializer , AlbumSerializer , FilesSerializer
from rest_framework.filters import SearchFilter

#다양한 리퀘스트 파일 형식들을 다룰 수 있게
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

class PostViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body')

    def perform_create(self, serializer): # 자동으로 author_name을 등록
        serializer.save(author = self.request.user)

    # 현재 request를 보낸유저 == self.request.user

    def get_queryset(self):
        qs = super().get_queryset()
        
        if self.request.user.is_authenticated:
            qs = qs.filter(author = self.request.user)
        else:
            qs = qs.none()
        return qs


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_create(self, serializer): # 자동으로 author_name을 등록
        serializer.save(author = self.request.user)





class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

    parser_classes = (MultiPartParser, FormParser) # 다양한 타입의 파일을 수락(인코딩)할 수 있는 파서들...
    # file업로드 오류 시(근데 난 왜 오류 안나지..)
    # parser_classes 지정 , create() 오버라이딩

    def perform_create(self, serializer): # 자동으로 author_name을 등록
        serializer.save(author = self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = FilesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = HTTP_201_CREATED)
        else:
            return Response(serializer.error , status = HTTP_400_BAD_REQUEST)