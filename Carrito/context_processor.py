def importe_total_carro(request):
    total = 0
    cantidad =0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total+float(value['precio'])
            cantidad = cantidad+int(value['cantidad'])
            
    else:
        total = 'Debes hacer login'
    
    return {'importe_total_carro':total, 'total_producto':cantidad}


