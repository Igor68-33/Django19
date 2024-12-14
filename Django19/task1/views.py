from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Buyer, Game

# Create your views here.
info = {}
games_buy = []
# games_buy = ['Atomic Heart']
# games = ['Atomic Heart',
#          'Cyberpunk 2077']


def queryset_test(request):
    print('Привет, начинаем работать с базой данных.')
    games = Game.objects.all()
    # удалить все записи из таблицы с играми
    for game in games:
        game.delete()
    buyers = Buyer.objects.all()
    # удалить все записи из таблицы покупателей
    for buyer in buyers:
        buyer.delete()
    # создать покупателей, один младше 18
    for i in range(1, 4):
        Buyer.objects.create(username=f"user{i}", balance=i * 1234, age=16 + i)
    # создать игры, одна с ограничением по возрасту
    for i in range(1, 4):
        if i == 1:
            age_limited = False
        else:
            age_limited = True
        Game.objects.create(title=f"game{i}", cost=12 * i, size=13 * i, age_limited=age_limited)

    buyers = Buyer.objects.all()
    Game.objects.get(title="game1").buyer.set((buyers[0], buyers[1], buyers[2]))
    Game.objects.get(title="game2").buyer.set((buyers[1], buyers[2]))
    Game.objects.get(title="game3").buyer.set((buyers[1],))
    print('Базу данных заполнили.')
    return render(request, "index.html")


def home(request):
    return render(request, 'home.html')


def shop(request):
    games = Game.objects.all()
    context = {'games': games}
    # context = dict(zip(games_num, games_list))
    return render(request, 'shop.html', context)


def basket(request):
    len_games_buy = len(games_buy)
    print("len_games_buy", len_games_buy)
    context = {'games_buy': games_buy,
               'len_games_buy': len_games_buy}

    return render(request, 'basket.html', context)


def menu(request):
    return render(request, 'menu.html')


def sign_up_by_html(request):
    # print(request.method)
    info["info_text"] = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        print("username:", username)
        print("password:", password)
        print("repeat_password:", repeat_password)
        print("age:", age)
        info["info_text"] = parsing(username, password, repeat_password, age)
        if "Приветствуем" in info["info_text"]:
            return redirect('home/')
            # HttpResponse(info["info_text"])
    return render(request, 'registration_page.html', info)


def parsing(username, password, repeat_password, str_age):
    info_text = "Извините, что то пошло не так."
    # users = []
    users = Buyer.objects.all()

    for buyer in users:
        if username in buyer.username:
            info_text = "Пользователь уже существует"
            info_text = registration_user(username, password)
            return info_text
    if str_age.isnumeric():
        age = int(str_age)
        if age < 18:
            info_text = "Вы должны быть старше 18"
        elif len(password) < 8 or len(repeat_password) < 8:
            info_text = "Пароль должен быть не менее 8 символов."
        elif password == repeat_password:
            info_text = f"Приветствуем, {username}!"
            # print(f'добавим {username}')
            Buyer.objects.create(username=f"{username}", balance=1000, age=age)

    else:
        info_text = "Возраст должен быть целым числом"
    print(info_text)
    return info_text


def registration_user(username, password):
    if password == password:
        return f"Приветствуем, {username}!"
    return f"Пароль покупателя {username} не верный."
