import json
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, pagination, views, permissions
from rest_framework.response import Response
from service.models import *
from service.serializers import *
from django.contrib.auth import logout, login
from service.decorators import form_validation, required_fields, sms_verification
from service.authentication import BaseSessionAuthentication
from service.views.v1.filter import *


def logout_view(request):
    logout(request)
    return JsonResponse({'code': 'OK'})


class UserSignUpView(views.APIView):
    authentication_classes = (
        BaseSessionAuthentication,
    )

    # @form_validation(UserAuthSerializer)
    # user = serializer.signup()

    def post(self, request):
        data = json.loads(request.body)

        if User.objects.filter(username=data['username']).first():
            return JsonResponse(data={
                'code': 'NotRegister',
                'msg': '이미 존재하는 아이디입니다.\n다른 아이디를 입력해주세요.'
            }, status=409)
            # if User.objects.filter(phone_number=self.data['phone_number']).exists():
            #     raise ValidationError({'phone_number': '이미 사용 중인 전화번호입니다.'})
        elif User.objects.filter(nickname=data['nickname']).exists():
            return JsonResponse(data={
                'code': 'NotRegister',
                'msg': '이미 존재하는 닉네임입니다.\n다른 닉네임을 입력해주세요.'
            }, status=409)

        user = User.objects.create(
            username=data['username'], nickname=data['nickname'],
        )
        user.set_password(self.data['password'])
        user.save()
        login(request, user)

        return Response({'code': 'OK'})


class UserSignInView(views.View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # @form_validation(UserAuthSerializer)

    def post(self, request):

        logout(request)

        if request.user.is_authenticated:
            return JsonResponse({'code': 'OK'})

        data = json.loads(request.body)

        user = User.objects.filter(username=data['username']).first()
        if not user:
            return JsonResponse(data={
                'code': 'NotLogin',
                'msg': '사용자를 찾을 수 없습니다'
            })
        elif not user.check_password(data['password']):
            return JsonResponse(data={
                'code': 'NotLogin',
                'msg': '올바른 비밀번호를 입력해주세요'
            })
        login(request, user)
        return JsonResponse({'code': 'OK'})


class UserProfileView(views.APIView):
    authentication_classes = (
        BaseSessionAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request):
        serializer = UserProfileSerializer(instance=request.user)

        request.session.set_expiry(864000)
        return Response(serializer.data)

    @form_validation(UserProfileSerializer)
    def patch(self, request, serializer):
        serializer.instance = request.user
        serializer.save()
        return Response(serializer.data)
