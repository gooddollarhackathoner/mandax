# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

from .decorators import twilio_view
import datetime


@twilio_view
def say(request, text, voice=None, language=None, loop=None):
    """
See: http://www.twilio.com/docs/api/twiml/say.

Usage::

    # urls.py
    urlpatterns = patterns('',
        # ...
        url(r'^say/$', 'django_twilio.views.say', {'text': 'hello, world!'})
        # ...
    )
    """
    r = VoiceResponse()
    r.say(text, voice=voice, language=language, loop=loop)
    return r


@twilio_view
def play(request, url, loop=None):
    """
    See: http://www.twilio.com/docs/api/twiml/play.

    Usage::

        # urls.py
        urlpatterns = patterns('',
            # ...
            url(r'^play/$', 'django_twilio.views.play', {
                    'url': 'http://blah.com/blah.wav',
            }),
            # ...
        )
    """
    r = VoiceResponse()
    r.play(url, loop=loop)
    return r


@twilio_view
def gather(request, action=None, method='POST', num_digits=None, timeout=None,
           finish_on_key=None):
    """
    See: http://www.twilio.com/docs/api/twiml/gather.

    Usage::

        # urls.py
        urlpatterns = patterns('',
            # ...
            url(r'^gather/$', 'django_twilio.views.gather'),
            # ...
        )
    """
    r = VoiceResponse()
    r.gather(action=action, method=method, numDigits=num_digits,
             timeout=timeout, finishOnKey=finish_on_key)
    return r


@twilio_view
def record(request, action=None, method='POST', timeout=None,
           finish_on_key=None, max_length=None, transcribe=None,
           transcribe_callback=None, play_beep=None):
    """
    See: http://www.twilio.com/docs/api/twiml/record.

    Usage::

        # urls.py
        urlpatterns = patterns('',
            # ...
            url(r'^record/$', 'django_twilio.views.record'),
            # ...
        )
    """
    r = VoiceResponse()
    r.record(action=action, method=method, timeout=timeout,
             finishOnKey=finish_on_key, maxLength=max_length,
             transcribe=transcribe, transcribeCallback=transcribe_callback,
             playBeep=play_beep)
    return r


@twilio_view
def sms(request, message, to=None, sender=None, action=None, method='POST',
        status_callback=None):
    """
    NOTE: Now deprecated, please use message() instead
    See: http://www.twilio.com/docs/api/twiml/sms

    Usage::

        # urls.py
        urlpatterns = patterns('',
            # ...
            url(r'^sms/$', 'django_twilio.views.sms', {
                'message': 'Hello, world!'
            }),
            # ...
        )
    """
    r = MessagingResponse()
    r.message(message, to=to, sender=sender, method='POST', action=action,
              statusCallback=status_callback)
    return r


@twilio_view
def message(request, message, to=None, sender=None, action=None,
            methods='POST', media=None, status_callback=None):
    """
    See: https://www.twilio.com/docs/api/twiml/sms/message

    Usage::

        # urls.py
        urlpatterns = patterns('',
            # ...
            url(r'^sms/$', 'django_twilio.views.message', {
                'message': 'Hello, world!',
                'media': 'http://fullpath.com/my_image.png'
            }),
            # ...
        )
    """

    r = MessagingResponse()
    r.message(message, to=to, sender=sender, method='POST',
              action=action, statusCallback=status_callback,
              media=media)

    return r


@twilio_view
def dial(request, number, action=None, method='POST', timeout=None,
         hangup_on_star=None, time_limit=None, caller_id=None):
    """
    See: http://www.twilio.com/docs/api/twiml/dial.

    Usage::

        # urls.py
        urlpatterns = patterns('',
            # ...
            url(r'^dial/(?P<number>\w+)/$', 'django_twilio.views.dial'),
            # ...
        )
    """
    r = VoiceResponse()
    r.dial(number=number, action=action, method=method, timeout=timeout,
           hangupOnStar=hangup_on_star, timeLimit=time_limit,
           callerId=caller_id)
    return r


@twilio_view
def conference(request, name, muted=None, beep=None,
               start_conference_on_enter=None, end_conference_on_exit=None,
               wait_url=None, wait_method='POST', max_participants=None):
    """
See: http://www.twilio.com/docs/api/twiml/conference.

Usage::

    # urls.py
    urlpatterns = patterns('',
        # ...
        url(r'^conference/(?P<name>\w+)/$', 'django_twilio.views.conference',
                {'max_participants': 10}),
        # ...
    )
    """
    r = VoiceResponse()
    dial = Dial()
    dial.conference(name=name, muted=muted, beep=beep,
                    startConferenceOnEnter=start_conference_on_enter,
                    endConferenceOnExit=end_conference_on_exit,
                    waitUrl=wait_url, waitMethod=wait_method,
                    )
    r.append(dial)
    return r

from twilio.twiml.messaging_response import MessagingResponse
from django_twilio.decorators import twilio_view
# include decompose in your views.py
from django_twilio.request import decompose
from django_twilio.models import MandexUser, Transaction, Exchange

@twilio_view
def inbound_view(request):

    response = MessagingResponse()

    # Create a new TwilioRequest object
    twilio_request = decompose(request)

    # See the Twilio attributes on the class
    twilio_request.to

    print(twilio_request.__dict__)
    body_text = twilio_request.body
    broken_text = body_text.split()
    print(broken_text[0])
    if (broken_text[0] == 'hello') or (broken_text[0] == 'Hello'):
        NewUser=MandexUser(username=broken_text[-1],
                     phone = twilio_request.from_,
                     time= datetime.datetime.now(),
                     ils_balance = 100,
                     gdd_balance = 100)

        NewUser.save()
        response.message("""Welcome to MandaX!\n
Your balance is:\n
100 ils\n
100 gdd\n
send 'commands' for commands""")

    elif (broken_text[0] == 'commands') or (broken_text[0] == 'Commands'):
        response.message("""Send 'commands' for commands.\n
Send 'get balance' to view funds'\n
Send 'send <quantity> <currency> to <name>' \n
eg. 'send 20 ils to mordechai' \n
send 'exchange <quantity> <currency> to <currency>'\n
eg. 'exchange 20 ils to gdd'""")

    elif (broken_text[0] == 'send') or (broken_text[0] == 'Send'):

        print(twilio_request.__dict__)
        body_text = twilio_request.body
        broken_text = body_text.split()
        print(broken_text[0])

        sender_get=MandexUser.objects.filter(phone=twilio_request.from_)
        for e in sender_get:
            sender_data = e

        reciever_get=MandexUser.objects.filter(username=broken_text[4])
        for e in reciever_get:
            reciever_data = e

        if broken_text[2] == "ils":
            sender_data.ils_balance -= int(broken_text[1])
            reciever_data.ils_balance += int(broken_text[1])
            sender_balance = sender_data.ils_balance
            reciever_balance = reciever_data.ils_balance

        elif broken_text[2] == "gdd":
            sender_data.gdd_balance -= int(broken_text[1])
            reciever_data.gdd_balance += int(broken_text[1])
            sender_balance = sender_data.gdd_balance
            reciever_balance = reciever_data.gdd_balance
        sender_data.save()
        reciever_data.save()

        NewTransaction = Transaction(sent_from = twilio_request.from_,
                                     sent_to = broken_text[4],
                                     time= datetime.datetime.now(),
                                     quantity = broken_text[1],
                                     currency = broken_text[2])

        NewTransaction.save()

        response.message("""you have sent %s %s to %s, your new balance is %s %s""" % (broken_text[1],
                                                                                           broken_text[2],
                                                                                           broken_text[4],
                                                                                           sender_balance,
                                                                                           broken_text[2]))


        client = Client('ACefad70b4197645889c4d677a6510820c', '2cd5a87702b8b85eacfc70a684a5f551')
        message = client.messages \
                        .create(
                            body="You have recieved %s %s from %s. Your new balance is %s %s" % (broken_text[1],
                                                                                                 broken_text[2],
                                                                                                 twilio_request.from_,
                                                                                                 reciever_balance,
                                                                                                 broken_text[2]),
                            from_='+972527288545',
                            to=reciever_data.phone
                        )
        print(message.sid)

    elif (broken_text[0] == 'exchange') or (broken_text[0] == 'Exchange'):
        #NewTransaction = Transaction(user = twilio_request.from_,
                                     #origin_quantity = broken_text[1],
                                     #origin_currency = broken_text[2],
                                     #destination_quantity = int(broken_text[1]),
                                     #destination_currency = broken_text[3])

        #NewTransaction.save()
        sender_get=MandexUser.objects.filter(phone=twilio_request.from_)
        print(len(sender_get))
        for e in sender_get:
            sender_data = e

        if broken_text[2] == "ils":
            sender_data.ils_balance -= int(broken_text[1])
            print(sender_data.gdd_balance)
            sender_data.gdd_balance += int(broken_text[1])
            print(sender_data.ils_balance)

        elif broken_text[2] == "gdd":
            sender_data.gdd_balance -= int(broken_text[1])
            print(sender_data.gdd_balance)
            sender_data.ils_balance += int(broken_text[1])
            print(sender_data.ils_balance)

        sender_data.save()

        response.message("""You have exchanged %s %s for %s %s.
Your new balance is %s ils and %s gdd""" % (broken_text[1],
                                            broken_text[2],
                                            broken_text[1],
                                            broken_text[4],
                                            sender_data.ils_balance,
                                            sender_data.gdd_balance
                                            ))


    elif (broken_text[0] == 'get') or (broken_text[0] == 'Get'):
        data_get=MandexUser.objects.filter(phone=twilio_request.from_)
        for e in data_get:
            data_row = e 

        response.message("""hello %s
ils balance: %s \n
gdd balance: %s""" % (data_row.username, data_row.ils_balance, data_row.gdd_balance))

    elif (broken_text[0] == 'thank') or (broken_text[0] == 'Thank'):
        response.message("You're Welcome!.")


    else:
        response.message("Sorry but your command was not recognized. Send 'Commands' for commands.")
    return response
