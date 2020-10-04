from rest_framework import serializers
from service.models import Post, User, Region
from service.serializers import UserProfileSerializer


class RegionSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name')
    city_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Region
        fields = (
            'id',
            'name',
            'city_id',
            'city_name',
        )


class PostSerializer(serializers.ModelSerializer):
    has_favorite = serializers.SerializerMethodField(read_only=True)
    user = UserProfileSerializer(read_only=True)
    status = serializers.CharField(read_only=True, source='get_status_display')
    region = RegionSerializer(many=False, read_only=True)
    is_mine = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'content',
            'status',
            'hire_limit',
            'favorite_count',
            'has_favorite',
            'start_time',
            'end_time',
            'region',
            'is_mine',
            'created_at',
        )

    def get_is_mine(self, obj):
        if not self.context['request'].user.is_authenticated:
            return False
        return obj.user_id == self.context['request'].user.id

    def get_has_favorite(self, obj):
        return self.context['request'].user.id in [favorite_user for favorite_user in obj.favorite_users.all()]



