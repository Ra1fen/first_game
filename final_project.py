from defss import *

print('Здравствуй, путник. Король дал задание найти его дочь, и ты должен выполнить его.')
name = input('Какое твоё имя, путник? ')
player[name] = name
sleep(1)
print('Куда ты пойдешь?')
sleep(1)
while True:
    choise = input('Можно пойти в лес, в пещеру, в город и на рынок: ')
    sleep(1)
    if choise == 'в лес':
        print(f'{player[name]} пошёл в лес')
        sleep(1)
        les()
        print('Вы возвращаетесь назад')
        sleep(1)

    if choise == 'на рынок':
        print(f'{player[name]} пошёл на рынок')
        sleep(1)
        magaz()
        sleep(1)
        while True:
            replay = input('Хотите купить что-нибудь ещё? ')
            sleep(1)
            if replay == 'Да':
                magaz()
            else:
                break
        print('Вы возвращаетесь назад')
        sleep(1)

    if choise == 'в пещеру':
        print(f'{player[name]} пошёл в пещеру')
        sleep(1)
        peshera()
        print('Вы возвращаетесь обратно к выбору')
        sleep(1)

    if choise == 'в город':
        print(f'{player[name]} пошёл в город')
        sleep(1)
        gorod()
        break