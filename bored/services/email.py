import requests

# send email template

msg = construct_veri_msg(user, domain)
print(msg)
mail = requests.post(
    MAILGUN_BASE_URL + 'messages',
    auth=("api", MAILGUN_API_KEY),
    data={
        'from': APP_EMAIL,
        'to': address,
        'o:tracking': 'no',
        'subject': "Activate Hawkins Account",
        'html': msg
    }
)
print("sending to {}".format(address))
return