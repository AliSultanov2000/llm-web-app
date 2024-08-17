from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


slovar = {
    "leo": "Ты лев!", 
    "wolf": "Ты волк!", 
    "dog": "Ты собака!", 
    "cat": "Ты котик!"
}


def get_person_type(request, sign_person_type: str):
    description = slovar.get(sign_person_type, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound("Ошибочка вышла!")



def get_person_type_num(request, sign_person_type: int):
    person_types = list(slovar)
    if sign_person_type <= len(person_types) - 1:
        person_type = person_types[sign_person_type]
        print(person_type)
        return HttpResponseRedirect(f'/polls/{person_type}')
    else: 
        return HttpResponseNotFound("Ошибочка вышла!")
