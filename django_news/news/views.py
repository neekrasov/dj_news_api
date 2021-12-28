from rest_framework import generics, permissions, viewsets
from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .mixins import PermissionViewSetMixin

from .models import News,Review
from .serializers import (
    NewsListSerializer,
    DetailNewsSerializer,
    CreateRatingSerializer,
    NewsCategorySerializer, ReviewSerializer, ReviewListSerializer
)
from .service import get_client_ip, MovieFilter


class NewsListViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        news = News.objects.filter(is_published=True).annotate(middle_star=models.Avg("rating__star"))
        return news

    def get_serializer_class(self):
        if self.action == 'list':
            return NewsListSerializer
        if self.action == 'retrieve':
            return DetailNewsSerializer

    # ------generics.ListAPIView-------
    # serializer_class = NewsListSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = MovieFilter
    # permission_classes = [permissions.IsAuthenticated]
    # def get_queryset(self):
    #     news = News.objects.filter(is_published=True).annotate(middle_star=models.Avg("rating__star"))
    #     return news

    # ----------APIView---------------
    # def get(self, request):
    #     news = News.objects.filter(is_published=True).annotate(
    #         middle_star=models.Avg("rating__star")
    #     )
    #     serializer = NewsListSerializer(news, many=True)
    #     return Response(serializer.data)


class CategoryListViewSet(viewsets.ModelViewSet):
    serializer_class = NewsCategorySerializer

    # ------generics.ListAPIView-------
    # serializer_class = NewsCategorySerializer
    # queryset = Category.objects.all()

    # -----------APIView------------
    # def get(self, request):
    #     category = Category.objects.all()
    #     serializer = NewsCategorySerializer(category, many=True)
    #     return Response(serializer.data)


# class DetailNewsView(generics.RetrieveAPIView): теперь в классе NewsListViewSet
#     queryset = News.objects.filter(is_published=True)
#     serializer_class = DetailNewsSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# ----------APIView---------------
# def get(self, request, pk):
#     news = News.objects.get(id=pk, is_published=True)
#     serializer = DetailNewsSerializer(news)
#     return Response(serializer.data)


# class ReviewDestroy(generics.DestroyAPIView): теперь в классе ReviewCreateViewSet
#     queryset = Review.objects.all()
#     permission_classes = [permissions.IsAdminUser]


class ReviewModelViewSet(PermissionViewSetMixin, viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    permission_classes_by_action = {
        'list': [permissions.AllowAny],
        'create': [permissions.IsAuthenticated],
        'example': [permissions.AllowAny],
        'update': [permissions.IsAdminUser],
        'destroy': [permissions.IsAdminUser],
    }

    @action(detail=True)
    def example(self, request, *args, **kwargs):
        review = self.get_object()
        serializer = ReviewSerializer(review, many=False)
        return Response(serializer.data)
    #
    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [permissions.IsAuthenticated]
    #     elif self.action == 'example':
    #         permission_classes = [permissions.IsAdminUser]
    #     else:
    #         permission_classes = [permissions.IsAdminUser]
    #     return [permission() for permission in permission_classes]

    # def get_serializer_class(self):
    #     if self.action == 'create':
    #         return ReviewCreateSerializer
    #     if self.action == 'retrieve':
    #         return ReviewSerializer
    #     if self.action == 'list':
    #         return ReviewListSerializer

    # ------generics.UpdateAPIView, generics.CreateAPIView-------
    # serializer_class = ReviewCreateSerializer
    # permission_classes = [permissions.IsAdminUser]

    # ----------APIView---------------
    # def post(self, request):
    #     review = ReviewCreateSerializer(data=request.data)
    #     if review.is_valid():
    #         review.save()
    #     return Response(status=201)


class AddStarRatingViewSet(viewsets.ModelViewSet):
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))

    # ------generics.ListAPIView-------
    # serializer_class = CreateRatingSerializer
    #
    # def perform_create(self, serializer):
    #     serializer.save(ip=get_client_ip(self.request))

    # ----------APIView---------------
    # def post(self, request):
    #     serializer = CreateRatingSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(ip=get_client_ip(request))
    #         return Response(status=201)
    #     else:
    #         return Response(status=400)
