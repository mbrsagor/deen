import ssl
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.utils.functional import cached_property
from django.contrib.auth.hashers import check_password
from django.core.mail.backends.smtp import EmailBackend as SMTPBackend

User = get_user_model()


class EmailBackend(SMTPBackend):
    @cached_property
    def ssl_context(self):
        if self.ssl_certfile or self.ssl_keyfile:
            ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)
            ssl_context.load_cert_chain(self.ssl_certfile, self.ssl_keyfile)
            return ssl_context
        else:
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            return ssl_context


class EmailPhoneAuthenticationBackend(object):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(Q(phone=username) | Q(email=username))

        except User.DoesNotExist:
            return None

        if user and check_password(password, user.password):
            if user.is_active:
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
