print('Задача 9. Недоделка')
from datetime import datetime

def random(N):
  current_time = datetime.now().time()
  enpy = current_time.microsecond
  return enpy % N + 1

def rock_paper_scissors():
  machineStep = random(3) # камень - 1, ножницы - 2, бумага - 3

  print('Введите ваш ход: камень, ножницы или бумага \nДля выхода в меню введите 0')
  string = input()
  if string == '0':
    mainMenu()
  elif (string == 'Камень' or string == 'камень'):
    if machineStep == 1:
      print('Камень |', string)
    elif machineStep == 2:
      print('Ножницы |', string)
      print('!!!Вы выиграли!!!')
    else:
      print('Бумага |', string)
      print('Компьютер выиграл')
  elif (string == 'Ножницы' or string == 'ножницы'):
    if machineStep == 1:
      print('Камень |', string)
      print('Компьютер выиграл')
    elif machineStep == 2:
      print('Ножницы |', string)
    else:
      print('Бумага |', string)
      print('!!!Вы выиграли!!!')
  elif (string == 'Бумага' or string == 'бумага'):
    if machineStep == 1:
      print('Камень |', string)
      print('!!!Вы выиграли!!!')
    elif machineStep == 2:
      print('Ножницы |', string)
      print('Компьютер выиграл')
    else:
      print('Бумага |', string)
  else:
    print('Ошибка ввода!')
  rock_paper_scissors()

def guess_the_number():
  hidden_number = random(10) # машина выбирает число от 1 до 10

  number = int(input('Введите число от 1 до 10: '))
  if number == hidden_number:
    print('Угадал)))')
    mainMenu()
  else:
    guess_the_number()

def summa():
  a = int(input('Введите число A: '))
  b = int(input('Введите число B: '))
  print('Сумма', str(a)+'+'+str(b)+'=', a+b)
  mainMenu()

def mainMenu():
    print('Выберите игру: \n 1 - "Камень, ножницы, бумага" \n 2- "Угадай число"')
    game = int(input())
    if game == 1:
      print('Игра: камень, ножницы, бумага')
      rock_paper_scissors()
    elif game == 2:
      print('Игра: угадай число')
      guess_the_number()
    elif game == 3:
      print('Выбрано суммирование двух чисел')
      summa()
    elif game == 15:
      print('bonus for you')
      ptint('try later', str(game)+'$')
      mainMenu()
    else:
      print('Ошибка ввода!')
      mainMenu()

mainMenu()
