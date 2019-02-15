from django.shortcuts import render

#
@csrf_exempt
def login_user(request):
    json_data = get_json(request)
    print(json_data)
    try:
        username = json_data['username']
        password = json_data['password']
    except KeyError:
        return HttpResponseBadRequest("username / password not specified")
    usr = authenticate(username=username, password=password)
    if usr is not None:
        login(request, usr)
        return JsonResponse({'message': 'successful login'})
    else:
        return HttpResponseForbidden("Invalid credentials")

@api_view(['POST'])
def logout_user(request):
    json_data = get_json(request)
    PushNotificationToken.objects.filter(token=json_data['expo']).delete()

    #shld also remove JWT from redis cache. but not rly impt.

    return JsonResponse({'message': 'logged out successfully'})


# not used in app
@csrf_exempt
def logout(request):
    logout(request)

    #removes push token from db

    print(request.__dict__)
    return





@csrf_exempt
def forget_password(request):
    """
    email data needed to send password
    """
    json_data = get_json(request)
    print(json_data)
    try:
        email = json_data['email']
    except KeyError:
        return HttpResponseBadRequest('Please specify email')
    try:
        usr = User.objects.get(username=email)
    except User.DoesNotExist:
        return HttpResponseForbidden('Email not found')
    #if usr.password_recently_reset:

    #	return HttpResponseBadRequest("Email with new password has been sent. Do check your email.")

    password = updatePassword(usr)
    task = forget_pw.apply_async([email, password], routing_key='normal', queue="normal")

    print(task.status)
    work = AsyncResult(task.id)
    print(work)
    result = work.get()
    print(result)
    print(task.status)
    if task.status == "PENDING":
        return JsonResponse({'message': 'Password successfully reset.'})
    else:
        return HttpResponseServerError('Email was not sent!')