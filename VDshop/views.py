from django.shortcuts import render, get_object_or_404, redirect


def redirect_to_store(request):
    """
    redirecting to home page form "/"
    :param request: request
    :return: redirect
    """
    return redirect("store:home")
