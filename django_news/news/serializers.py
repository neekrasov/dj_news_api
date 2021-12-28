from rest_framework import serializers

from .models import News, Category, Review, Rating


class CreateRatingSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(  # Объект в rating, булевы значения в _
            ip=validated_data.get('ip', None),
            news=validated_data.get('news', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating

    class Meta:
        model = Rating
        fields = ("star", "news")


class ReviewSerializer(serializers.ModelSerializer):
    news = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Review
        fields = ("id", 'news', 'email', "name", "text")


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'name', 'text')


class NewsListSerializer(serializers.ModelSerializer):
    middle_star = serializers.FloatField()

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "middle_star",
            "created_at",
        )


class DetailNewsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="title", read_only=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = News
        exclude = ("is_published",)


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title",)
