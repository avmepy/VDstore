from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Profile

def profile_register(request):

    if request.method == 'POST':






@login_required
def profile_detail(request):

    user = request.user

    context = {
        'user': user
    }

    return render(request, 'account/profile_detail.html', context=context)

