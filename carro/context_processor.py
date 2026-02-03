def importe_total_carro(request):
    total = 0
    carro = request.session.get("carro", {})
    if request.user.is_authenticated:
        for key, value in carro.items():
            total += float(value["precio"])
    else:
        total = "Debes hacer login."
    return {"importe_total_carro": total}
