from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, HttpResponse, JsonResponse
from . import serializers
from . import models
# Create your views here.
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings



class User(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = serializers.UserSerializer(models.CustomUser.objects.get(pk=request.user.id))
        return Response(serializer.data)


class verification(APIView):
    def get(self, request):
        status = request.GET.get('verification', None)
        if status is not None:
            return render(request=request, template_name="login/verification.html")
        else:
            domain = str(request.scheme)+"://"+str(request.META['HTTP_HOST'])
            return HttpResponseRedirect(redirect_to=domain)


class user_password_reset_request(APIView):

    def post(self, request):
        if request.method == "POST":
            email = request.data.get("email")
            # password_reset_form = PasswordResetForm(request.POST)
            # if password_reset_form.is_valid():
            if email is not None:
                User = get_user_model()
                # data = password_reset_form.cleaned_data['email']
                associated_users = User.objects.filter(Q(email=email))
                if associated_users.exists():
                    for user in associated_users:
                        subject = "Password Reset Requested"
                        email_template_name = "password/password_reset_email.txt"
                        c = {
                            "email": user.email,
                            'domain': '127.0.0.1:8000',
                            'site_name': 'Website',
                            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                            "user": user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                        }
                        domain = str(request.scheme)+"://"+str(request.META['HTTP_HOST'])
                        email = render_to_string(email_template_name, c)
                        email = email.replace(":baseurl:", ''+str(domain)+'')
                        try:
                            send_mail(subject, email, getattr(settings, 'EMAIL_HOST_USER'),
                                      [user.email], fail_silently=False)
                        except BadHeaderError:
                            return Response(status=status.HTTP_400_BAD_REQUEST)
                        return Response({"status": "mail sent"})
            return Response(status=status.HTTP_400_BAD_REQUEST)
