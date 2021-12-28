from django_filters import rest_framework as filters
from .models import News


def get_client_ip(self, request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class MovieFilter(filters.FilterSet):
    category = filters.RangeFilter()

    class Meta:
        model = News
        fields = ('category',)
