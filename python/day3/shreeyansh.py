def show_time():
    try:
        while True:
            import time
            print(time.asctime())
            time.sleep(1)
            display(clear=True)
    except:
        print("code has been stopped by user")

def check_palindrome(world:str):
    if type(world)==str:
        if world==world[::-1]:
            return 'palindrome'
        else:
            return 'not a palindrome'
    else:
        return 'invalid datatype'

def give_fibo(n):
    fibo = [0,1]
    for i in range(n-2):
        last_num=fibo[-1]
        second_last_num=fibo[-2]
        next_num=last_num+second_last_num
        fibo.append(next_num)
    return fibo

def pattern_building():
        n=int(input("enter a number: "))
        for i in range(1,n+1):
            print(" "*(n-i) + i*"* ")

def print_star(n = 5, typ = 'mid',shape="LOL"):
  if typ  == 'left':
    space  = ''

  elif typ == 'right':
    space = '  '

  elif typ == 'mid':
    space = ' '

  for i in range(1,n+1):
    print(space*(n-i) + i*f'{shape}')

def sum(number):
    result=0
    for i in range(1,number+1):
        result += i
        print(result)

def factorial(n):
    result=1
    for i in range(1,n+1):
        result *= i
    return result

def total_sales(*args):
    result=0
    for i in args:
        result+=i
    return result

sales=[45678,56,84,22,11]
def mini(*args):
    min_element=sales[0]
    for i in sales[1:]:
        if (i<min_element):
            min_element=i
    return min_element

def maxi(*args):
    max_element=sales[4]
    for i in sales[:4]:
        if(i>max_element):
            max_element=i
    return max_element

company=["ola","uber","tata","adani"]
def add_hashtag(*company):
    result=[]
    for i in company:
        result.append("#"+i.upper())
    return result

def store_records(**kwargs): #kwargs refers to dictionary
    import pandas as pd
    try:
        data=pd.DataFrame(kwargs)
        return data
    except:
        data=pd.DataFrame(kwargs,index=[1])
        return data

def soundbox(paisa):
    from gtts import gTTS
    text=f"paytm pe {paisa} prapt huye"
    audio=gTTS(text)
    audio.save("paytm.mp3")
    import pygame as pg
    pg.init()
    music=pg.mixer.Sound('paytm.mp3')
    music.play()

def vote(age):
  print('can Vote!!') if age >= 18 else print('can not Vote!!')

print("this is shreeyansh module in python")