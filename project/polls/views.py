from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

slovar = {
    "leo": "Ты лев!", 
    "wolf": "Ты волк!", 
    "dog": "Ты собака!", 
    "cat": "Ты котик!"
}


def index(request): 
    person_types = list(slovar)
    li_elements = ""
    for person_type in person_types:
        pass


def get_person_type(request, sign_person_type: str):
    description = slovar.get(sign_person_type, None)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    else:
        return HttpResponseNotFound("Ошибочка вышла!")

  

def get_person_type_num(request, sign_person_type: int):
    person_types = list(slovar)
    if sign_person_type <= len(person_types) - 1:
        person_type = person_types[sign_person_type]
        redirect_url = reverse("polls_name", args=(person_type, ))
        # return HttpResponseRedirect(f'/polls/{person_type}')
        return HttpResponseRedirect(redirect_url)
    else: 
        return HttpResponseNotFound("Ошибочка вышла!")
