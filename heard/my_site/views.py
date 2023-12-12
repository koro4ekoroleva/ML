from django.shortcuts import render
import pickle
import sklearn
import datetime

menu = [{'title': 'Главная', 'url': ''},
        {'title': 'Разработчик', 'url': 'me'}]


def home(request):
    data = {
        'title': 'Главная',
        'menu': menu}
    if request.GET:
        data['result'] = predict(request.GET)
        return render(request, 'my_site/home_result.html', context=data)
    return render(request, 'my_site/home.html', context=data)


def me(request):
    data = {
        'title': 'Главная',
        'menu': menu}
    return render(request, 'my_site/me.html', context=data)


with (open("my_site/heard-model", "rb")) as openfile:
    model = pickle.load(openfile)


def predict(req):
    data_for_predict = []
    need_data = ['weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc']
    age = req.get('age', '1999.01.01') + ' 00:00:00.0'
    age = datetime.datetime.strptime(age, "%Y-%m-%d  %H:%M:%S.%f").date()
    now = datetime.date.today()
    age = int(str(now - age).split(' ')[0])
    data_for_predict.append(age)
    for i in need_data:
        data_for_predict.append(float(req.get(i, 0)))
    pr = model.predict([data_for_predict])
    pr = int(pr[0])
    return int(model.predict([data_for_predict])[0])
