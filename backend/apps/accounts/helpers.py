from datetime import timedelta

from django.core.signing import Signer
from django.utils.timezone import now

from .models import CustomUser


def generate_token_for_user(user: CustomUser, hours=1) -> str:
    """
    Generate signed token for user

    @param user:
    @param hours:
    @return:
    """
    valid_to = now() + timedelta(hours=hours)
    signer = Signer()
    return signer.sign_object({"id": user.pk, "valid_to": valid_to.isoformat()})
