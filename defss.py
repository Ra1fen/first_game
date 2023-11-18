import random
from random import randint
from time import sleep

def magaz():
    shop = input('Можно купить меч или броню. Что ты хочешь купить? ')
    sleep(1)
    if shop == 'Броню':
        bronya()
    if shop == 'Меч':
        mech()

def bronya():
    armorr = {'Кожаная броня': 500, 'Железная броня': 1000, 'Алмазная броня': 2000}
    choise_armor = input(f'Какую броню вы хотите купить из этого списка: {armorr}? ')
    sleep(1)
    if choise_armor == 'Кожаную':
        print('Неплохой выбор')
        player['money'] -= 500
        player['hp'] += 150
        player_money = player['money']
        player_armor = player['hp']
        sleep(1)
        print(f'Теперь у тебя {player_armor} здоровья и {player_money} монет')
    if choise_armor == 'Железную':
        print('Хороший выбор')
        player['money'] -= 1000
        player['hp'] += 250
        player_money = player['money']
        player_armor = player['hp']
        sleep(1)
        print(f'Теперь у тебя {player_armor} здоровья и {player_money} монет')
    if choise_armor == 'Алмазную':
        print('Отличный выбор')
        player['money'] -= 2000
        player['hp'] += 400
        player_money = player['money']
        player_armor = player['hp']
        sleep(1)
        print(f'Теперь у тебя {player_armor} здоровья и {player_money} монет')




def mech():
    sword = {'Деревянный': 300, 'Железный': 600, 'Алмазный': 1000}
    choise_sword = input(f'Какой меч вы хотите купить из этого списка: {sword} ')
    sleep(1)
    if choise_sword == 'Деревянный':
        print('Можно было выбрать и лучше')
        player['money'] -= 300
        player['attack'] += 15
        player['inventory'] += 'Деревянный меч'
        player_attack = player['attack']
        player_money = player['money']
        player_inventory = player['inventory']
        sleep(1)
        print(f'Теперь у тебя {player_attack} урон и {player_money} монет')

    if choise_sword == 'Железный':
        print('Неплохой выбор')
        player['money'] -= 600
        player['attack'] += 20
        player['inventory'] += 'Железный меч'
        player_attack = player['attack']
        player_money = player['money']
        player_inventory = player['inventory']
        sleep(1)
        print(f'Теперь у тебя {player_attack} урон и {player_money} монет')
    
    if choise_sword == 'Алмазный':
        print('Лучший выбор')
        player['money'] -= 1000
        player['attack'] += 30
        player['inventory'] += 'Алмазный меч'
        player_attack = player['attack']
        player_money = player['money']
        player_inventory = player['inventory']
        sleep(1)
        print(f'Теперь у тебя {player_attack} урон и {player_money} монет')


def peshera():
    print(f'{player[name]} встретил Змей Горыныча')
    current_enemy = 1
    player_hp = player['hp']
    enemy = enemies[current_enemy]
    enemy_attack = enemies[current_enemy]['attack']
    enemy_hp = enemies[current_enemy]['hp']
    sleep(1)
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    sleep(1)
    input('Enter чтобы продолжить')
    print()
    sleep(1)
    while True:
            print(f'{player[name]} атакует {enemy["name"]}.')
            lucky = 'Змей отразил', 'Змей не отразил'
            atack = random.choice(lucky)
            if atack == 'Змей не отразил':
                sleep(1)
                print('У Змей Горыныча не получилось отразить атаку')
                enemy_hp -= player['attack']
            if atack == 'Змей отразил':
                sleep(1)
                print('Змей Горыныч удачно отразил атаку и нанёс удар в ответ')
                player['hp'] -= enemy['attack']
                player_hp == player['hp']
                enemy_hp == enemy['hp']
            sleep(1)
            print(f'''{player[name]} - {player['hp']}
{enemy['name']} - {enemy_hp}''')
            sleep(1)
            if enemy_hp <= 0:
                print(f'Змей Горыныч: {enemies[current_enemy]["win"]}')
            if player['hp'] <= 0:
                print(f'Змей Горыныч: {enemies[current_enemy]["loss"]}')
            print()
            sleep(1)
            if enemy_hp <= 0:
                break
            elif player['hp'] <= 0:
                break
        
def les():
    print(f'{player[name]} встретил Волка')
    current_enemy = 0
    player_hp = player['hp']
    enemy = enemies[current_enemy]
    enemy_attack = enemies[current_enemy]['attack']
    enemy_hp = enemies[current_enemy]['hp']
    sleep(1)
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    sleep(1)
    input('Enter чтобы продолжить')
    print()
    sleep(1)
    while True:
            print(f'{player[name]} атакует Волка.')
            lucky = 'Волк отразил', 'Волк не отразил'
            atack = random.choice(lucky)
            if atack == 'Волк не отразил':
                sleep(1)
                print('У Волка не получилось отразить атаку')
                enemy_hp -= player['attack']
            if atack == 'Волк отразил':
                sleep(1)
                print('У Волка получилось отразить атаку')
                hit = 'Волк парировал атаку', 'У волка не получилось парировать атаку'
                attack_in_response = random.choice(hit)
                if attack_in_response == 'Волк парировал атаку':
                    print('Волк парировал атаку и нанёс урон в ответ')
                    player['hp'] -= enemy['attack']
                if attack_in_response == 'У волка не получилось парировать атаку':
                    print('У Волка не получилось парировать атаку')
                enemy_hp == enemy['hp']
            sleep(1)
            print(f'''{player[name]} - {player['hp']}
{enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
            if enemy_hp <= 0:
                print(f'Волк: {enemies[current_enemy]["win"]}')
            if player['hp'] <= 0:
                print(f'Волк: {enemies[current_enemy]["loss"]}')
            sleep(1)
            if enemy_hp <= 0:
                break
            elif player['hp'] <= 0:
                break

def gorod():
    print(f'{player[name]} встретил Доминика Торетто')
    current_enemy = 2
    player_hp = player['hp']
    enemy = enemies[current_enemy]
    enemy_attack = enemies[current_enemy]['attack']
    enemy_hp = enemies[current_enemy]['hp']
    sleep(1)
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    sleep(1)
    input('Enter чтобы продолжить')
    print()
    sleep(1)
    while True:
            print(f'{player[name]} атакует {enemy["name"]}.')
            lucky = 'Доминик Торетто отразил', 'Доминик Торетто не отразил'
            atack = random.choice(lucky)
            if atack == 'Доминик Торетто не отразил':
                sleep(1)
                print('У Доминика Торетто не получилось отразить атаку')
                enemy_hp -= player['attack']
            if atack == 'Доминик Торетто отразил':
                sleep(1)
                print('Доминик Торетто удачно отразил атаку и нанёс удар в ответ')
                player['hp'] -= enemy['attack']
                player_hp == player['hp']
                enemy_hp == enemy['hp']
            sleep(1)
            print(f'''{player[name]} - {player['hp']}
{enemy['name']} - {enemy_hp}''')
            sleep(1)
            if enemy_hp <= 0:
                print(f'Доминик Торетто: {enemies[current_enemy]["win"]}. Happy End!!!')
            if player['hp'] <= 0:
                print(f'Доминик Торетто: {enemies[current_enemy]["loss"]}.')
            print()
            sleep(1)
            if enemy_hp <= 0:
                break
            elif player['hp'] <= 0:
                break

player = {
    'name': '',
    'armor': 0.95,
    'hp': 10000,
    'attack': 50,
    'luck': 10,
    'money': 10000,
    'inventory': []
}

enemies = [
    {
        'name': 'Волк',
        'hp': 20,
        'attack': 10,
        'script': 'Зачем ты здесь? Ты не сможешь меня победить. Принцесса больше не твоя, а чья - не твоя забота. Уходи, пока можешь.',
        'win': 'Ты - достойный противник, но до принцессы тебе всё равно никогда не добраться.',
        'loss': 'Ха! Я же говорил - тебе меня не одолеть. Уходи и не возвращайся.'
    },
    {
        'name': 'Змей Горыныч',
        'hp': 30,
        'attack': 25,
        'script': 'Не ожидал меня встретить? Я, если честно, тоже не думал, что здесь окажусь. После богатырей остаётся только фрилансить, в этот раз сказали защищать долину на пути к замку. В любом случае, ААААААрхрхрархгрх!! Ты не пройдёшь!',
        'win': 'На самом деле, я даже рад, что ты меня победил. Мой босс - дуралей, принцессу не заслужил. Иди дальше. Не зубадь там замолвить за меня словечко. Скажи, что я сражался как лев. Нет.. Как дракон!!',
        'loss': 'Могли бы просто побеседовать. Ты же и сам знал, что у тебя не получится меня убить.. Возвращайся как-нибудь, здесь довольно одиноко.'
    },

    {
        'name': 'Доминик Торетто',
        'hp': 200,
        'attack': 50,
        'script': 'Как ты смог добраться до сюда?! Как ты вообще посмел думать, что можешь со мной сражаться? Ты слаб! Принцесса будет моей, а ты уйдёшь ни с чем. Да будет битва! Самое важное - семья.',
        'win': 'Ты победил меня! Всё это время принцесса была у меня. Теперь она твоя :(',
        'loss': 'Прощай..'
    }
]

print('Здравствуй, путник. Король дал задание найти его дочь, и ты должен выполнить его.')
name = input('Какое твоё имя? ')
player[name] = name
sleep(1)
print('Куда ты пойдешь?')
sleep(1)
for i in range(10):
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