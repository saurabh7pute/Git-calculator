from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        val1 = request.POST['num1']
        ans = eval(val1)
        print(ans)
        return render(request, 'result.html', {'result': ans})
    return render(request,'index.html')

def res(request):
    return render (request,'result.html')