from django.shortcuts import render
from django.http import *
from cms_templates.models import Pages

def logeado(request):
    if request.user.is_authenticated():
        headerHtml = "<header>Logged in as " + request.user.username \
            + ". <a href='/logout'> Logout </a></header><br>\n"
        return (True, headerHtml)
    elif not request.user.is_authenticated():
        headerHtml = "<header>Not logged in. <a href='/admin'> Login </a></header><br>\n"
        return (False, headerHtml)

def printAll(body):
    body = body +  "Estas son las paginas Disponibles" + "<ul>\n"
    listaPaginas = Pages.objects.all()
    for pagina in listaPaginas:
        body = body + "<li><a href='/" + pagina.nombreRec + "'> Pagina " \
            + pagina.nombreRec + "</a></li>"
    body = body + "</ul>"
    return body

# Create your views here.
def barra(request):
    logged, bodyHtml = logeado(request)
    if logged:
        if request.method == 'GET':
            bodyHtml = printAll(bodyHtml)
            bodyHtml = bodyHtml + "<form id='paginas' method='POST'>" \
                + "<label> Introduce el recurso y el contenido del recurso" \
                + "</br></label>" \
                + "<input name='name' type='text'>" \
                + "<br>" \
                + "<textarea name='page' rows='20' cols='100' ></textarea>" \
                + "<br>" \
                + "<input type='submit' value='Enviar'></form>"
            return HttpResponse(bodyHtml)
        elif request.method == 'POST':
            
