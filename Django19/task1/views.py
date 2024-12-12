from django.shortcuts import render
from .models import Buyer, Game


# Create your views here.

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
