from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

def is_admin(user):
    return user.userprofile.role == 'Admin'
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/templates/relationship_app/admin_view.html')