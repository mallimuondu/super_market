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
    print('Good night.')

def securyty():
    print("guards are cheking car ..")
    import time
    time.sleep(2)
securyty()
def card():
    import time
    a = input('take the ticket pls take(ok or thankyou): ')
    if a == 'ok' or a =='thankyou':
        time.sleep(1)
        print('welcome')
    else:
        print("you have inputed the wrong thing try again")
        card()
card()
def parking():
    b = input('''
    there is a parking at:
    a.parking lot 23
    b.parking lot 34
    which do you want to park in:
    ''')
    if b == 'a' or b == 'b' or b == 'parking lot 23' or b == 'parking lot 34' or b == '23'or b == '34':
        print('go for securty cheek number 2')
    else:
        print("parking is full try another one")
        parking()
parking()
def securty2():
    import random
    import time
    time.sleep(1)
    print('pls sanitizer')
    print("your tempreture is")
    import random
    a = random.randrange(35,37)
    print(a)
securty2()

def items():
    categorys = input('''
    WE HAVE THREE CATEGORYS :
    a.foods
    b.londry
    c.electronics
    d.colths
    e.hard where
    : 
    ''')
    if categorys == 'a':
        def food():
            d = input('''
            WE HAVE:
            1.milk
            2.bread
            3.yogat
            4.sweet
            5.crisps
            ''')
            global total
            total = 0
            if d == '1':
                print('that is 40ksh for 1 paket')
                global e
                e = 40
                total += e
                c.execute('INSERT INTO food(total)VALUES(?)',(total,))
                conn.commit()
                print('you have bought milk  for '+ str(e))
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
                items()
            j = input('do you want to buy a nother item y or n:')
            if j == 'y':
                items()
        food()
    elif categorys  == 'b' :
        def londry():
            m = input('''
            a.soap
            b.shampoo
            c.cloth
            ''')
            if m == 'a':
                print('that is 20ksh for 1 bar')
                n = 20
            elif m == 'b':
                print('that is 650 par paket')
                o = 650
            elif m == 'c':
                print('that is 190 par scraber')
                p = 190
            j = input('do you want to buy a nother item y or n:')
            if j == 'y':
                items()
        londry()
    elif categorys == 'c':
        def electroniks():
            q = input('''
            a.T.V
            b.washing machine
            c.frige
            d.laptop
            ''')
            if q == 'a':
                print('that is 21579 for 1 T.V')
                r = 21579
            elif q == 'b':
                print('that is 18868 for i one washing machine')
                s = 18868
            elif q == 'c':
                print('that is 26242 for one frige')
                t = 26242
            elif q == 'd':
                print('that is 32423 for one laptop')
                u = 32423
            j = input('do you want to buy a nother item y or n:')
            if j == 'y':
                items()
        electroniks()
        
    elif categorys == 'd':
        def cloths():
            a = input('''
            a.Tshirts
            b.shorts
            c.jens
            ''')
            if a == 'a':
                print('that is 300 ksh for one')
                b = 300
            elif a == 'b':
                print('that is 300 for one')
                c = 300
            elif a == 'c':
                print('that is 400 for one')
                d = 400
            j = input('do you want to buy a nother item y or n:')
            if j == 'y':
                items()
        cloths()
    elif categorys  == 'e':
        def hard_where():
            e = input('''
            a.wheelbarow
            b.hammer
            c.scrow driver
            ''')
            if e == 'a':
                print('that is for 500 ksh')
                f = 500
            elif e == 'b':
                print('that is 750 ksh')
                g = 750
            elif e == 'c':
                print('that is 270 ksh')
                h = 270
            j = input('do you want to buy a nother item y or n:')
            if j == 'y':
                items()
        hard_where()
            
items()
            
        
def paying():
    print("your total is ")
    for a in c:
        for item in a:
            res.append(item)
    ading = sum(c)
    print(ading)
    k = int(input('pls pay : '))
    l = k - total
paying()
    
    
    
    
    
    
    
    
    
    
    
    
    