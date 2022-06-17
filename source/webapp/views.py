from django.shortcuts import render


# Create your views here.


def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    else:

        context = {
            "first_number": request.POST.get("first_number"),
            "second_number": request.POST.get("second_number"),
            "user": request.POST.get("user"),
            "result": "",
            "znak": ""
        }
        print(context)
        if context['user'] == 'add':
            context['znak'] = '+'
            context['result'] = int(context['first_number']) + int(context['second_number'])
        if context['user'] == 'subtract':
            context['znak'] = '-'
            context['result'] = int(context['first_number']) - int(context['second_number'])
        if context['user'] == 'multiply':
            context['znak'] = '*'
            context['result'] = int(context['first_number']) * int(context['second_number'])
        if context['user'] == 'divide':
            context['znak'] = '/'
            context['result'] = int(context['first_number']) / int(context['second_number'])
        return render(request, 'create.html', context)

