import uuid
import random
import string
from decimal import Decimal
from django.utils import timezone
from django.conf import settings
from django.utils.timezone import now
from django.core.mail import send_mail
from django.template.loader import get_template

from utils.enum_utils import DiscountType

# When user creates device token will automatically create random 10 digit string
letters = string.ascii_lowercase
random_device_token = "".join(random.choice(letters) for i in range(10))

# Convert seconds to time
def seconds_to_time(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    parts = []
    if hours:
        parts.append(f"{hours} Hour" + ("s" if hours > 1 else ""))
    if minutes:
        parts.append(f"{minutes} Minute" + ("s" if minutes > 1 else ""))

    return " ".join(parts)


# Get average rating
def average_rating(num):
    rating = 0

    for n in num:
        rating = rating + n
    try:
        avg = rating / len(num)
        return avg
    except Exception as ex:
        return str(ex)


# Get discount price from promo code
def get_discount_price(promo_code, budget):
    """
    Calculate discount amount based on promo code and given budget.
    :param promo_code: PromoCode instance or None
    :param budget: Decimal or float
    :return: Decimal (discount amount)
    """
    if not promo_code or not promo_code.is_active:
        return Decimal("0.00")

    now = timezone.now()
    if not (promo_code.from_date <= now <= promo_code.end_date):
        return Decimal("0.00")

    # Ensure budget is Decimal
    budget = Decimal(budget)

    # Calculate discount
    if promo_code.discount_type == DiscountType.AMOUNT.value:
        discount = promo_code.amount
    elif promo_code.discount_type == DiscountType.PERCENTAGE.value:
        discount = (budget * Decimal(promo_code.parentage)) / 100
    else:
        discount = Decimal("0.00")

    # Don’t exceed total budget
    return min(discount, budget)


# Generate OTP 4 digits
def generate_otp(length=4):
    otp_chars = "0123456789"
    otp = "".join(random.choice(otp_chars) for _ in range(length))
    return otp


# Profile user upload path
def user_profile_upload_to(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.user.id}_{uuid.uuid4().hex[:6]}.{ext}"
    return f"user/profile/{now().strftime('%m/%Y')}/{filename}"


# Generic mail sending by SMTP
def generic_sent_mail(email, subject, message):
    to_email = [email]
    from_email = settings.EMAIL_HOST_USER
    send_mail(
        subject,
        message,
        from_email,
        to_email,
        fail_silently=False,
    )


# Sent link to change password
def sent_link_to_change_password(email, context):
    subject = "Reset your password"
    message = "Click the link below to reset your password."
    to_email = [email]
    template = get_template("email/email_password_reset.html").render(context)
    from_email = settings.EMAIL_HOST_USER
    send_mail(
        subject,
        message,
        from_email,
        to_email,
        html_message=template,
        fail_silently=False,
    )

