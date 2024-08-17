from django.http import HttpResponse, HttpResponseNotFound


slovar = {
    "leo": "Ты лев!", 
    "wolf": "Ты волк!", 
    "dog": "Ты собака", 
    "cat": "Ты котик"
}



def get_person_type(request, sign_person_type: str):
    description = slovar.get(sign_person_type, None)
    if description:
        return HttpResponse(description)
    else:
        HttpResponseNotFound("Ошибочка вышла!")




