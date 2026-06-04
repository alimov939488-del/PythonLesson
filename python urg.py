def greet(name='guest') :
    print(name)
greet('diyorbek')
greet()
'''
'''
def show_age(age=18) :
    print(age)
show_age(19)
show_age()
'''
'''
def student(name='ali' , age=18) :
    print('salom' , name , 'yoshim' , age)
student('diyorbek' , 166)
student()
'''
'''
def check(is_active=True) :
    if is_active :
        print('faol')
    else :
        print('faol emas')
check()
'''
'''
def say(text='salom') :
    print(text)
say('salom')
say()
'''
'''
def user(name, age) :
    print('ism',name)
    print('yosh',age)
user('diyorbek' , 19)
'''
'''
def user(name , city) :
    print('ism' , name)
    print('shahar' , city)
user(name='diyorbek' , city='xorazm')
'''
'''
def car(brand , year) :
    print('brend' , brand)
    print('yili' , year)
car('bmw' , 2020)
car(brand='bmw' , year=2025)
'''
'''
def book(title , author , price) :
    print('taytli' , title)
    print('auyhor' , author)
    print('narxi' , price)
book('assalom' , author='assalom' , price=1000)
'''
'''
def name(first , last) :
    print('ismi' , first)
    print('familoyasi' , last)
name(first='diyorbek' , last='alimov')
'''
'''
name = 'ali'
def func() :
    print(name)
func()
'''
'''
def func() :
    age = 18
    print(age)
func()
'''
'''
x = 10
def func() :
    y = 20
    print(f'funsksiya ichidagi x' , x)
    print(f' funksiya ichidagi x' , y)

func()
'''
'''
def func() :
    x = 19
    print('funksiya ichidagi' , x)
func()
print('tashqaridagi' , x)
'''
'''
city = 'tashkent'
def func() :
    print(city)
func()
'''
'''
def func(*text) :
    print(text)
func(12 , 54 , 85 , 74 , 78)
'''
'''
def func(*yigindi) :
    d = 0
    for i in yigindi :
        d += i
    print(d)
func(12 , 25 , 45 , 47 , 78)
'''
'''
def func(**dict1) :
    for a , b in dict1.items() :
        print(a , b)
func(name='diyorbek' , age= 19 , city='xiva')
'''
'''
def func(**dict1) :
    for a in dict1 :
        print(a)
func(name='diyorbek' , age=20)
'''
