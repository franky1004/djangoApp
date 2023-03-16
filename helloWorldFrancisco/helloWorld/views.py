from django.http import JsonResponse

def index(request):
    responseData = {
        'Message': 'Hello World!'
    }

    return JsonResponse(responseData)