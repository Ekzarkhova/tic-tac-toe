field = [['-  '] * 3 for _ in range(3)]
def show_field(f):
    print('  0   1   2')
    for i in range(len(field)):
      print(str(i), *field[i])
def users_input(f):
    while True:
        place=input('Введите координаты: ') .split()
        if len(place)!=2:
            print("Введите две координаты через пробел -_-")
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x,y= map(int, place)
        if not(x>=0 and x<3 and y>=0 and y<3):
            print('Вышли из диапазона =c')
            continue
        if f[x][y] != '-  ':
            print('Клетка занята =0')
            continue
        break
    return x,y

def win_game(f):
    def chek_line(a1, a2, a3, user):
        if a1==user and a2==user and a3==user:
            return True
    for n in range(3):
        if chek_line(f[n][0], f[n][1], f[n][2], user) or \
            chek_line(f[0][n], f[1][n], f[2][n], user) or \
            chek_line(f[0][0], f[1][1], f[2][2], user) or \
            chek_line(f[2][0], f[1][1], f[0][2], user):
            return True
    return False

count=0
while True:
    if count%2==0:
        user= "X"
    else:
        user= "0"
    show_field(field)
    x, y = users_input(field)
    field[x] [y]=user
    if count == 9:
        print("Ничья=)")
        break
    if win_game(field):
        print(f"Победил {user}. Поздравляем! ")
        break
    count+=1