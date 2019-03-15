from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACefad70b4197645889c4d677a6510820c'
auth_token = '2cd5a87702b8b85eacfc70a684a5f551'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello to MandaX.",
                     from_='+972527288545',
                     to='+9720587988631'
                 )

print(message.sid)
