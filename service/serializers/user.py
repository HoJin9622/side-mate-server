from rest_framework import serializers

from service.exceptions import ValidationError, ConflictError
from service.models import *
from service.serializers import *



class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    # phone_number = serializers.CharField()
    nickname = serializers.CharField()

    def signup(self):
        if User.objects.filter(username=self.data['username']).exists():
            raise ConflictError({'username': '이미 존재하는 아이디입니다.'})
        # if User.objects.filter(phone_number=self.data['phone_number']).exists():
        #     raise ValidationError({'phone_number': '이미 사용 중인 전화번호입니다.'})
        if User.objects.filter(nickname=self.data['nickname']).exists():
            raise ConflictError({'nickname': '이미 사용 중인 닉네임입니다.\n다른 닉네임을 입력해주세요.'})

        user = User.objects.create(
            username=self.data['username'], nickname=self.data['nickname'],
        )
        user.set_password(self.data['password'])
        user.save()

        return user


class UserSignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def signin(self):
        user = User.objects.filter(username=self.data['username']).first()
        if not user:
            raise ValidationError({'username': '가입되지 않는 아이디입니다.'})
        elif not user.check_password(self.data['password']):
            raise ValidationError({'password': '올바른 비밀번호를 입력해주세요.'})

        return user


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'nickname',
            # 'email',
            # 'phone_number',
        )
