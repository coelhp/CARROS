from django.http import HttpResponse

def cars_view(request):
    html = '''
    <h1>Car View</h1>
        <head>
            <title>Car View</title>
        </head>
        <body>
            <h1>Welcome to the Car View Page</h1>
            <h3>Here you can find information about various cars.</h3>
        </body>
    '''
    return HttpResponse(html)
