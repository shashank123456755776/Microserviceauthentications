from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer, LoginSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully', 'uuid': user.uuid,'api_key':user.api_key}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                tokens = RefreshToken.for_user(user)
                return Response({
            
                    'uuid': str(user.uuid),
                    'refresh': str(tokens),
                    'access': str(tokens.access_token),
                    'role':user.role, 
                    'api_key':user.api_key,
                    'status':200
                })
            return Response({'error': 'Invalid credentials'}, status=401)
        return Response(serializer.errors, status=400)
class ApiKeyLoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        api_key = request.headers.get('X-API-KEY')
        
        if not api_key:
            return Response({'error': 'X-API-KEY header missing'}, status=400)
        
        try:
            user = User.objects.get(api_key=api_key)  # Retrieve user based on API key
        except User.DoesNotExist:
            return Response({'error': 'Invalid API key'}, status=401)
        
        tokens = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(tokens),
            'access': str(tokens.access_token),
            'username': user.username,
            'role': user.role,
            'uuid': str(user.uuid),
            'api_key': user.api_key
        })
