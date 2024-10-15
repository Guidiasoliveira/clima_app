from django.shortcuts import render
import requests

API_KEY = "8a150ef426004a139f4173712241510"  # Sua chave da API

def clima_view(request):
    cidade = "Belo Horizonte"  # Cidade padrão
    if request.method == "POST":
        cidade = request.POST.get("cidade")  # Obtém o nome da cidade do formulário

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={cidade}&aqi=no"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        temperatura = dados["current"]["temp_c"]
        condicao = dados["current"]["condition"]["text"]
        chance_chuva = dados["current"]["precip_mm"]
        umidade = dados["current"]["humidity"]
        vento = dados["current"]["wind_kph"]

        return render(request, 'clima/index.html', {
            'temperatura': temperatura,
            'condicao': condicao,
            'chance_chuva': chance_chuva,
            'umidade': umidade,
            'vento': vento,
            'cidade': cidade,  # Passa o nome da cidade para o template
        })
    else:
        return render(request, 'clima/index.html', {'erro': 'Erro ao obter dados do clima.'})
