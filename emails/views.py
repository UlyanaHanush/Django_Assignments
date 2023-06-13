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
                <div>Text1: {text1}<div> 
                <div>Text2: {text2}<div>
                <div>Recipient {recip}</div>
            """)
##templates/index1.html
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="utf-8" />
#     <title>EMAILS.COM</title>
# </head>
# <body>
#     <h2>User form</h2>
#     <form method="post" action="postuser/">
#         {% csrf_token %}
#         <p>Text1: <br />
#             <input name="text1" />
#         </p>
#         <p>Text2: <br />
#             <input name="text2" />
#         </p>
#         <p>
#             Recipient :<br />
#             <select multiple name="recipient">
#                 <option>Python</option>
#                 <option>JavaScript</option>
#                 <option>C++</option>
#                 <option>Java</option>
#              </select>
#         </p>
#         <input type="submit" value="Submit" />
#     </form>
# </body>
# </html>