from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index1.html")


def postuser(request):
    # получаем из строки запроса имя пользователя
    text1 = request.POST.get("text1", 'No text')
    text2 = request.POST.get("text2", 'No text')
    recip = request.POST.getlist("recipient", ["python"])


    return HttpResponse(f"""
                <div>Text1: {text1}  Text2: {text2}<div>
                <div>:Recipient {recip}</div>
            """)