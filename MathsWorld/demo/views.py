#harsh

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def si(request):
    return render(request, 'si.html')

def si_result(request):
    P=int(request.POST.get('P'))
    R = int(request.POST.get('R'))
    T = int(request.POST.get('T'))
    SI = (P * R * T) / 100
    Amount = P + SI
    data={'Principle':P,'Rate':R,'Time':T,'SimpleInterest':SI,'Amount':Amount}
    return render(request, 'si_result.html',data)

def ci(request):
    return render(request, 'ci.html')

def ci_result(request):
    P=int(request.POST.get('P'))
    R = int(request.POST.get('R'))
    T = int(request.POST.get('T'))
    Amount = int(P * (1 + R / 100) ** T)
    CI = int(Amount - P)

    data={'Principle':P,'Rate':R,'Time':T,'CompoundInterest':CI,'Amount':Amount}
    return render(request, 'ci_result.html',data)

def hcf_lcm(request):
    return render(request, 'hcf_lcm.html')

def hcf_lcm_result(request):
    n1=int(request.POST.get('n1'))
    n2 = int(request.POST.get('n2'))

    if n1 > n2:
        t2 = n1
        t1 = n2
    else:
        t2 = n2
        t1 = n1

    while t2 % t1 != 0:
        tmp = t1
        t1 = t2 % t1
        t2 = tmp

    HCF = t1

    LCM = int((n1 * n2) / HCF)

    data={'Number1':n1,'Number2':n2,'HCF':HCF,'LCM':LCM}
    return render(request, 'hcf_lcm_result.html',data)

def profit_loss(request):
    return render(request, 'profit_loss.html')

def profit_loss_result(request):
    CP=int(request.POST.get('CP'))
    SP= int(request.POST.get('SP'))

    diff = SP - CP

    if diff == 0:
        PL = "No Profit and Loss"
        R = 0
        P = 0
    elif diff > 0:
        PL = "Profit"
        R = diff
        P = ((diff * 100) / CP)
    else:
        PL = "Loss"
        R = -diff
        P = (-((diff * 100) / CP))

    data={'CP':CP,'SP':SP,'PL':PL,'R':R,'P':P}
    return render(request, 'profit_loss_result.html',data)

def km_to_m(request):
    return render(request, 'km_to_m.html')

def km_to_m_result(request):
    km=int(request.POST.get('km'))
    m = km * 1000
    data={'km':km,'m':m}
    return render(request, 'km_to_m_result.html',data)

def km_to_cm(request):
    return render(request, 'km_to_cm.html')

def km_to_cm_result(request):
    km=int(request.POST.get('km'))
    cm = km * 100000
    data={'km':km,'cm':cm}
    return render(request, 'km_to_cm_result.html',data)

def d_to_b(request):
    return render(request, 'd_to_b.html')

def d_to_b_result(request):
    decimal=int(request.POST.get('decimal'))
    y = bin(decimal)[2::]

    data={'decimal':decimal,'binary':y}
    return render(request, 'd_to_b_result.html',data)

def d_to_o(request):
    return render(request, 'd_to_o.html')

def d_to_o_result(request):
    decimal=int(request.POST.get('decimal'))
    y = oct(decimal)[2::]

    data={'decimal':decimal,'octal':y}
    return render(request, 'd_to_o_result.html',data)

def d_to_h(request):
    return render(request, 'd_to_h.html')

def d_to_h_result(request):
    decimal=int(request.POST.get('decimal'))
    y = hex(decimal)[2::]

    data={'decimal':decimal,'hexadecimal':y}
    return render(request, 'd_to_h_result.html',data)
