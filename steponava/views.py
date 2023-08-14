from django.shortcuts import render
from django.http import HttpResponse
from .models import Lapas, Vadovas, LapasInstance, Budas
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request):
    # Lapų skaičius
    #num_lapai = Lapas.

    # Naujų lapų skaičius (kurie turi statusą 'n')
    #num_nauji_lapai = LapasInstance.filter(status__exact='n').count()

    # Vadovų skaičius
    #num_vadovai = Vadovas.indexes.count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        #    'num_lapai': num_lapai,
        # 'num_nauji_lapai': num_nauji_lapai,
        #'num_vadovai': num_vadovai,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


# class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
#     model = LapasInstance
#     template_name = 'user_books.html'
#     paginate_by = 10
#
#     def get_queryset(self):
#         return LapasInstance.objects.filter(reader=self.request.user).filter(status__exact='p').order_by('due_valid')

@login_required
def profilis(request):
    return render(request, 'profilis.html')