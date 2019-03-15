# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from twilio.twiml.voice_response import VoiceResponse, Dial
from twilio.twiml.messaging_response import MessagingResponse

from .decorators import twilio_view


@twilio_view
def message(request, message, to=None, sender=None, action=None,
            methods='POST', media=None, status_callback=None):
    """
    See: https://www.twilio.com/docs/api/twiml/sms/message
    """

    r = MessagingResponse()
    r.message(message, to=to, sender=sender, method='POST',
              action=action, statusCallback=status_callback,
              media=media)

    return r
