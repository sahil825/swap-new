from django.conf import settings
from django.core.checks import messages
from django.utils.text import slugify
from django.conf import settings
from django.core.mail import send_mail


import string
import random


def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
    return res


def generate_slug(text):
    new_slug = slugify(text)
    from home.models import BlogModel

    if BlogModel.objects.filter(slug = new_slug).exists():
        return generate_slug(text + generate_random_string(5))
        return new_slug 


def send_mail_to_user(token , email):
    subject = f"your accout need to be verified"
    messages = f"hi past the link to verified account http://     /verify/{token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, messages, email_from, recipient_list)
    return True