from django.contrib.sites.shortcuts import get_current_site
from django.core.mail.message import EmailMessage
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from rest_framework.request import Request

from .helpers import generate_token_for_user
from .models import CustomUser


def send_register_verification_email(request: Request, user: CustomUser):
    """
    Send verification email to newly created user

    @param request:
    @param user:
    """
    token = generate_token_for_user(user)

    mail_subject = _("Activate your user account.")
    message = render_to_string(
        "accounts/register_verification_email.html",
        {
            "user": user,
            "domain": get_current_site(request).domain,
            "token": token,
            "protocol": "https" if request.is_secure() else "http",
        },
    )
    email = EmailMessage(mail_subject, message, to=[user.email])
    email.send()
