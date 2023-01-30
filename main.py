import os, random, time, asyncio

money = 1500

os.system(command="CLS")

error_mmselect = False
error_mmselect_ = False

async def main_menu():
    os.system(command="CLS")
    global error_mmselect, error_mmselect_
    if error_mmselect:
        print("Укажи цифрами")
        error_mmselect = False
    elif error_mmselect_:
        print("Не правильное значение")
        error_mmselect_ = False
    print(f"Ваш баланс: {money}\n(1) Настройки\n(2) Начать играть")
    MM_select = input(">>> ")
    try:
        MM_select = int(MM_select)
    except:
        error_mmselect = True
        await main_menu()

    if MM_select == 1:
        await setting()
    elif MM_select == 2:
        await main_casino_menu()
    else:
        error_mmselect_ = True
        await main_menu()

money_update = False

async def edit_money():
    global error_mmselect, error_mmselect_, money_update
    os.system(command="CLS")
    if money_update:
        print(f"Ваш новый баланс: {money}")
        money_update = False
    if error_mmselect:
        print("Укажи цифрами")
        error_mmselect = False
    elif error_mmselect_:
        print("Не правильное значение")
        error_mmselect_ = False
    print("(1) Настроить деньги\n(2) Вернуться")
    MM_select = input(">>> ")
    try:
        MM_select = int(MM_select)
    except:
        error_mmselect = True
        await edit_money()

    if MM_select == 1:
        await set_money()
    elif MM_select == 2:
        await main_menu()
    else:
        error_mmselect_ = True
        await edit_money()

async def set_money():
    global money, error_mmselect, error_mmselect_, money_update
    os.system(command="CLS")
    if error_mmselect:
        print("Укажи цифрами")
        error_mmselect = False
    elif error_mmselect_:
        print("Не правильное значение")
        error_mmselect_ = False
    print(f"Старое: {money}")
    print("Напиши новое значение")
    MM_select = input(">>> ")
    try:
        MM_select = int(MM_select)
    except:
        error_mmselect = True
        await set_money()

    money = MM_select
    money_update = True
    await edit_money()

async def setting():
    global error_mmselect, error_mmselect_
    os.system(command="CLS")
    if error_mmselect:
        print("Укажи цифрами")
        error_mmselect = False
    elif error_mmselect_:
        print("Не правильное значение")
        error_mmselect_ = False
    print("(1) Изменить деньги\n(2) Вернуться")
    MM_select = input(">>> ")
    try:
        MM_select = int(MM_select)
    except:
        error_mmselect = True
        await edit_money()
    if MM_select == 1:
        await edit_money()
    elif MM_select == 2:
        await main_menu()
    else:
        error_mmselect_ = True
        await setting()

async def main_casino_menu():
    global error_mmselect, error_mmselect_
    os.system(command="CLS")
    if error_mmselect:
        print("Укажи цифрами")
        error_mmselect = False
    elif error_mmselect_:
        print("Не правильное значение")
        error_mmselect_ = False
    print("Рад вас видеть!\nДавай начнем?\n(1) Погнали!\n(2) Вернуться")
    MM_select = input(">>> ")
    try:
        MM_select = int(MM_select)
    except:
        error_mmselect = True
        await edit_money()

    if MM_select == 1:
        await game_start()
    elif MM_select == 2:
        await main_menu()
    else:
        error_mmselect_ = True
        await main_casino_menu()

bet = 0
bet_update = False
error_up = False

async def game_start():
    global error_mmselect, error_mmselect_, bet, bet_update, error_up
    os.system(command="CLS")
    if bet_update:
        print(f"Значение обновлено: {bet}")
        bet_update = False
    if error_up:
        print("Нельзя использоваться данное значение!")
        error_up = False
    if error_mmselect:
        print("Укажи цифрами")
        error_mmselect = False
    elif error_mmselect_:
        print("Не правильное значение")
        error_mmselect_ = False
    if bet == 0:
        print("(1) Указать ставку игры!\n(2) Погнали\n(3) Вернуться")
    else:
        print(f"Ваша ставка: {bet}\n(1) Изменить ставку игры!\n(2) Погнали\n(3) Вернуться")
    MM_select = input(">>> ")
    try:
        MM_select = int(MM_select)
    except:
        error_mmselect = True
        await edit_money()

    if MM_select == 1:
        await set_bet()
    elif MM_select == 2:
        if bet > 0:
            await game()
        else:
            await set_bet()
    elif MM_select == 3:
        await main_casino_menu()
    else:
        error_mmselect_ = True
        await game_start()


async def set_bet():
    global money, error_mmselect, error_mmselect_, bet_update, bet, error_up
    os.system(command="CLS")
    if error_mmselect:
        print("Укажи цифрами")
        error_mmselect = False
    elif error_mmselect_:
        print("Не правильное значение")
        error_mmselect_ = False
    print(f"Значение не должно привышать ваш баланс и не менее 250! Ваш баланс: {money}")
    if bet != 0:
        print("Укажи новое значение")
    else:
        print("Напиши значение")
    MM_select = input(">>> ")

    try:
        MM_select = int(MM_select)
    except:
        error_mmselect = True
        await set_bet()

    if MM_select > money or MM_select < 250:
        error_up = True
        await game_start()
    else:
        bet = MM_select
        bet_update = True
        await game_start()

dgekpot = False
luzer = False
win = False

async def game():
    global error_mmselect, error_mmselect_, dgekpot, luzer, win
    os.system(command="CLS")

    if error_mmselect:
        print("Укажи цифрами")
        error_mmselect = False
    elif error_mmselect_:
        print("Не правильное значение")
        error_mmselect_ = False

    if dgekpot:
        print("\nДЖЕКПОТ ЕМАЕ!\n")
        dgekpot = False
    elif win:
        print("\nпобеда!\n")
        win = False
    elif luzer:
        print("\nЛУЗЕЕЕР!\n")
        luzer = False

    print(f"Информация:\n    Баланс: {money}\n    Ставка: {bet}\n(1) Крутить \n(2) Вернуться")
    MM_select = input(">>> ")
    try:
        MM_select = int(MM_select)
    except:
        error_mmselect = True
        await game()

    if MM_select == 1:
        await speen_game()
    elif MM_select == 2:
        await game_start()
    else:
        error_mmselect_ = True
        await game()


num_1 = 0
num_2 = 0
num_3 = 0

async def speen_game():
    global money, bet, dgekpot, win, luzer
    money = money - bet
    os.system(command="CLS")
    global num_1, num_2, num_3
    # print("║=====║=====║=====║")
    # print("║  1  ║  1  ║  1  ║")
    # print("║=====║=====║=====║")
    num_1_dbag = 0
    while True:
        time.sleep(0.5)
        num_1_dbag += 1
        if num_1_dbag == 10:
            break
        os.system(command="CLS")
        num_1 = random.randint(1, 9)
        print("║=====║=====║=====║")
        print(f"║  {num_1}  ║  0  ║  0  ║")
        print("║=====║=====║=====║")

    num_2_dbag = 0
    while True:
        time.sleep(0.5)
        num_2_dbag += 1
        if num_2_dbag == 10:
            break
        os.system(command="CLS")
        num_2 = random.randint(1, 9)
        print("║=====║=====║=====║")
        print(f"║  {num_1}  ║  {num_2}  ║  0  ║")
        print("║=====║=====║=====║")


    num_3_dbag = 0
    while True:
        time.sleep(0.5)
        num_3_dbag += 1
        if num_3_dbag == 10:
            break
        os.system(command="CLS")
        num_3 = random.randint(1, 9)
        print("║=====║=====║=====║")
        print(f"║  {num_1}  ║  {num_2}  ║  {num_3}  ║")
        print("║=====║=====║=====║\n\n")

    time.sleep(0.5)

    if num_1 == num_2 or num_2 == num_3:
        bet_new = bet * 2
        money = money + bet_new
        win = True
        await game()
    elif num_1 == num_2 and num_2 == num_3:
        bet_new = bet * 10
        money = money + bet_new
        dgekpot = True
        await game()
    else:
        luzer = True
        await game()


async def result_game():
    pass

asyncio.run(main_menu())