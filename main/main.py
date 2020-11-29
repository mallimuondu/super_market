from daterbase import *
now = time.datetime.now()
hour = now.hour
if hour < 12:
    print("Good morning")
elif hour > 12 and hour < 18:
    print("Good afternoon")
elif hour > 18 and hour < 19:
    print("Good evening")
else:
    print('Have a nice night.')

def securyty():
    print("guards are cheking your car ..")
    import time
    time.sleep(2)
securyty()
def card():
    import time
    a = input('take the ticket pls.press any key and enter to continue: ')
card()
def parking():
    b = input('''
    the only parkings are at:
    a.parking lot 23
    b.parking lot 34
    where do you want to park?:
    ''')
    if b == 'a' or b == 'b' or b == 'parking lot 23' or b == 'parking lot 34' or b == '23'or b == '34':
        print('go for securty cheek number 2')
    elif b == '' or b == ' ':
        print('you did not input anything. please try again')
        parking()
    else:
        print("parking is full try another one")
        parking()
parking()
def securty2():
    import random
    import time
    time.sleep(1)
    print('pls santize')
    def temreture():
        try:
            temreture1 = float(input("pls input your temreture: "))
            if temreture1 > 37:
                print("you can not enter becouse we thing you have covid19")
                exit()  
            elif temreture1 == '' or temreture1 == ' ':
                print('you have inputed nothing try again')
                temreture()
            elif temreture1 <  37:
                print('WELCOME TO MY SUPER MARKET')
            elif temreture1 == '' or temreture1 == ' ':
                print('inputed nothing')
        except ValueError:
            print ('That is not a number')
            temreture()
    temreture()
securty2()

def items():
    categorys = input('''
    WE HAVE FIVE CATEGORYS YOU CAN SHOP FROM:
    a.foods
    b.laundry
    c.electronics
    d.clothes
    e.hard where
    f.toys
    PLEASE CHOOSE A CATEGORY: 
    ''')
    if categorys == 'a' or categorys == 'foods':
        def food():
            d = input('''
            You are now in the food section
            WE HAVE:
            1.milk 40 ksh
            2.bread 60 ksh 
            3.yogurt 60 ksh
            4.sweet 5ksh
            5.crisps 20 ksh
            what do you want to buy
            ''')
            global total
            total = 0
            if d == '1':
                y = int(input('how many do you want:'))
                global e
                e = 40
                z = y*e
                total += z
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
                print('you have bought milk  for '+ str(z))
            elif d == '2':
                print('that is 60ksh for a loaf of bread')
                global f
                f = 60
                total += f
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
                print('you have bought loaf for'+ str(f))
            elif d == '3':
                print('that is 60ksh for a paket of yogat')
                global g
                g = 60
                total += g
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
                print('you have bought yogat for'+ str(g))
            elif d == '4':
                print('that is 5ksh for 1 sweet')
                global h
                h = 5
                total += h
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
                print('you have bought a sweet for'+ str(h))
            elif d == '5':
                print('that is 20ksh for 1 paket')
                global i
                i = 20
                total += i
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
                print('you have bought crisps for'+ str(i))
            else:
                print('item not found try again')
                food()
            j = input('do you want to buy a nother item y or any leter to give bill:')
            if j == 'y':
                items()
        food()
        
    elif categorys  == 'b' or categorys == 'laundry':
        def londry():
            m = input('''
            You are now in the londry section
            a.soap 20ksh
            b.shampoo 650ksh
            c.cloth 190ksh
            what do you want to buy
            ''')
            global total
            total = 0
            if m == 'a':
                print('that is 20ksh for 1 bar')
                n = 20
                total += n
                c.execute('INSERT INTO billing(bill)VALUES(?)',(total,))
                conn.commit()
            elif m == 'b':
                print('that is 650 par paket')
                o = 650
                total += o
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
            elif m == 'c':
                print('that is 190 par scraber')
                p = 190
                total += p
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
            else:
                print('item not found try again')
                londry()
            j = input('do you want to buy a nother item y or any leter to give bill:')
            if j == 'y':
                items()
        londry()
    elif categorys == 'c' or categorys == 'electronics':
        def electroniks():
            q = input('''
            You are now in the electronics section
            a.T.V 21579ksh
            b.washing machine 18868ksh
            c.fridge 26242ksh
            d.laptop 32423ksh
            what do you want to buy
            ''')
            global total
            total = 0
            if q == 'a':
                print('that is 21579 for 1 T.V')
                r = 21579
                total += r
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
            elif q == 'b':
                print('that is 18868 for i one washing machine')
                s = 18868
                total += s
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
            elif q == 'c':
                print('that is 26242 for one frige')
                t = 26242
                total += t
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
            elif q == 'd':
                print('that is 32423 for one laptop')
                u = 32423
                total += u
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
            else:
                print('item not found try again')
                electroniks()
            j = input('do you want to buy a nother item y or any leter to give bill:')
            if j == 'y':
                items()
        electroniks()
        
    elif categorys == 'd' or categorys == 'clothes':
        def cloths():

            a = input('''
            You are now in the coths section
            a.Tshirts 300ksh
            b.shorts 300ksh
            c.jens 400ksh
            what do you want to buy
            ''')
            global total
            total = 0
            if a == 'a':
                print('that is 300 ksh for one')
                b = 300
                total += b
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
            elif a == 'b':
                print('that is 300 for one')
                d = 300
                total += d
            elif a == 'c':
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
                print('that is 400 for one')
                e = 400
                total += e
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
            else:
                print('item not found try again')
                items()
            j = input('do you want to buy a nother item y or any leter to give bill:')
            if j == 'y':
                cloths()
        cloths()
    elif categorys  == 'e'or categorys == 'hard where':
        def hard_where():
            e = input('''
            You are now in the hard_where section
            a.wheelbarow 500ksh
            b.hammer 750 ksh
            c.scew driver 270ksh
            what do you want to buy
            ''')
            global total
            total = 0
            if e == 'a':
                print('that is for 500 ksh')
                f = 500
                total += f
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
            elif e == 'b':
                print('that is 750 ksh')
                g = 750
                total += g
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
            elif e == 'c':
                print('that is 270 ksh')
                h = 270
                total += h
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
            else:
                print('item not found try again')
                hard_where()
            j = input('do you want to buy a nother item y or any leter to give bill:')
            if j == 'y':
                items()
        hard_where()
    elif categorys == 'f'or categorys == 'toys':
        def toys():
            e = input('''
            You are now in the toys section
            a.drown 3900ksh
            b.nerf gun 1000
            c.Waterproof RC Monster Truck Stunt Car 4551ksh
            what do you want to buy
            ''')
            global total
            total = 0
            if e == 'a':
                print('that is for 3900 ksh')
                f = 3900
                total += f
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
            elif e == 'b':
                print('that is 1000 ksh')
                g = 1000
                total += g
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
            elif e == 'c':
                print('that is 4551 ksh')
                h = 4551
                total += h
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
            else:
                print('item not found try again')
                toys()
            j = input('do you want to buy a nother item y or any leter to give bill:')
            if j == 'y':
                items()
        toys()
    else:
        print('oya you inputed wrong thing try again')
        items()
            
items()
            
        
def total():
    print("your total is ")
    global autput
    autput = 0
    for store in c.execute('SELECT * FROM food'):
        autput += store[0]
        print(autput)
        print('_______')
        

total()

def paying():
    a = int(input('pls pay(pay more or equal):'))
    if a > autput:
        print('your channge is:')
        d = a - autput
        print(d)
    else:
        print('pls return trawily')
paying()
print('good bye')
    
    
    
    
    
    
    
    
    
    
    
    
    