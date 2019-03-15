# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


@python_2_unicode_compatible
class Caller(models.Model):
    """
    A caller is defined uniquely by their phone number.

    :param bool blacklisted: Designates whether the caller can use our
        services.
    :param char phone_number: Unique phone number in `E.164
        <http://en.wikipedia.org/wiki/E.164>`_ format.

    """
    blacklisted = models.BooleanField(default=False)
    phone_number = PhoneNumberField(unique=True)

    def __str__(self):
        return '{phone_number}{blacklist_status}'.format(
            phone_number=str(self.phone_number),
            blacklist_status=' (blacklisted)' if self.blacklisted else '',
        )

    class Meta:
        app_label = 'django_twilio'


@python_2_unicode_compatible
class Credential(models.Model):
    """
    A Credential model is a set of SID / AUTH tokens for the Twilio.com API

        The Credential model can be used if a project uses more than one
        Twilio account, or provides Users with access to Twilio powered
        web apps that need their own custom credentials.

    :param char name: The name used to distinguish this credential
    :param char account_sid: The Twilio account_sid
    :param char auth_token: The Twilio auth_token
    :param key user: The user linked to this Credential

    """

    def __str__(self):
        return '{name} - {sid}'.format(name=self.name, sid=self.account_sid)

    name = models.CharField(max_length=30)

    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)

    account_sid = models.CharField(max_length=34)

    auth_token = models.CharField(max_length=32)

    class Meta:
        app_label = 'django_twilio'

class MandexUser(models.Model):
    "the user model has name, phone number, ils balance, gdd balance"
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    time = models.DateTimeField()
    ils_balance = models.DecimalField(max_digits=28, decimal_places=8)
    gdd_balance = models.DecimalField(max_digits=28, decimal_places=8)

class Transaction(models.Model):
    "transaction model has sender reciever quantity, currency, time"
    sent_from = models.CharField(max_length=50)
    sent_to = models.CharField(max_length=50)
    time = models.DateTimeField()
    quantity = models.DecimalField(max_digits=28, decimal_places=8)
    currency = models.CharField(max_length=3)

class Exchange(models.Model):
    "exchange has user, quantity, origin_currency, destination_currency, time"
    user = models.CharField(max_length=50)
    time = models.DateTimeField()
    origin_quantity = models.DecimalField(max_digits=28, decimal_places=8)
    origin_currency = models.CharField(max_length=3)
    destination_quantity = models.DecimalField(max_digits=28, decimal_places=8)
    destination_currency = models.CharField(max_length=3)
