from twilio.rest import Client

account_sid = "ACefad70b4197645889c4d677a6510820c"
auth_token = "2cd5a87702b8b85eacfc70a684a5f551"
client = Client(account_sid, auth_token)

for sms in client.messages.list():
    print(sms.to)

