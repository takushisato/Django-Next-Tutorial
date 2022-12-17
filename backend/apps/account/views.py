from django.contrib.auth import get_user_model

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer

User = get_user_model()


# アカウント登録
class RegisterView(APIView):
    # AllowAnyにすると認証不要になる
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            data = request.data
            name = data['name']
            email = data['email'].lower()
            password = data['password']
            
            # emailでユーザーの登録を確認
            if not User.objects.filter(email=email).exists():
                # 未登録アドレスの場合は新規登録
                User.objects.create_user(
                    name=name, email=email, password=password
                )

                return Response(
                    {'success': '新規会員登録が成功しました。'},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {'error': 'このメールアドレスは既に使用されています。'},
                    status=status.HTTP_400_BAD_REQUEST
                )


        except:
            return Response(
                {'error': 'アカウント登録時に問題が発生しました。'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# ユーザー情報取得（AllowAnyがないため認証が必要になる）
class UserView(APIView):
    def get(self, request):
        try:
            # シリアライザーを通してjson形式でUser情報を返す
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )

        except:
            return Response(
                {'error': 'ユーザー情報取得に問題が発生しました。'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
