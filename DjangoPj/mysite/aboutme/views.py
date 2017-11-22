from django.shortcuts import render

def index(request):
    return render(request, 'aboutme/home.html')
def contact(request):
    return render(request, 'aboutme/simple.html', {'content': ['Please feel free to email me at jposey730@gmail.com', 'or', 'Give me a call at (706)836-0730']})
