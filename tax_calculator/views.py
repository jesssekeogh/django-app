from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from . import tax_calc

def tax_home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def tax(request):
        shares = request.POST.get('no_shares')
        purprice = request.POST.get('purchaseprice')
        salprice = request.POST.get('saleprice')
    
        if shares == '' or purprice == '' or salprice == '':
            error = True
            return render(request, 'home.html', {'error': error})
        
        elif float(shares) > 0 and float(purprice) >= 0 and float(salprice) >= 0:
            cgt_clicked = False
            if request.POST.get('cgt_button'):
                cgt_clicked = True
            error = False
            tax_topay = tax_calc.Stocks(float(salprice),float(shares),float(purprice))
            return render(request, 'tax.html', {'tax_topay': tax_topay, 'cgt_clicked': cgt_clicked})
    
        else:
            error = True
            return render(request, 'home.html', {'error': error})

