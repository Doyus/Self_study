from django.shortcuts import render

def hello(request):
    context          = {}

    context['name']    = 'alice'
    context['age']     = 19
    context['sex']     = 1
    context['score'] = {'Chinese':80,'math':90,'english':91}
    return render(request, 'hello.html', context)
