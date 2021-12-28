from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

review_list = ReviewModelViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

review_detail = ReviewModelViewSet.as_view({
    'get': 'example',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path("news/", NewsListViewSet.as_view({'get': 'list'})),
    path("news/<int:pk>/", NewsListViewSet.as_view({'get': 'retrieve'})),
    path("review/<int:pk>/", review_detail),
    path("review/", review_list),
    path("category/", CategoryListViewSet.as_view({'get': 'list'})),
    path("rating/", AddStarRatingViewSet.as_view({'post': 'create'})),
])
