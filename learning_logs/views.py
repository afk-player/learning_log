from django.shortcuts import render


def index(request):
    """Learning_logs app homepage"""
    return render(request, 'learning_logs/index.html')
