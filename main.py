import numpy
from numpy import *
import tkinter
from tkinter import *
import pygame
def main():
  import random
  import datetime
  import pyjokes
  import wikipedia
  import pywhatkit
  import requests
  import time
  joke = ['I was going to tell you a joke about boxing but I forgot the punch line.','Why did the egg hide? It was a little chicken.',"I wanted to buy some camo pants but couldn't find any.","I ordered a chicken and an egg from Amazon. I'll let you know.","What month is the shortest of the year? May, it only has three letters.","How do you open a banana? With a mon-key.","Did you hear about the guy whose left side was cut off? He's all right now.","What does a pig put on dry skin? Oinkment.","Why do we tell actors to 'break a leg?' Because every play has a cast.",pyjokes.get_joke()]

  conversation = {
    'greeting': "Hello, User!",
    'how are you': "I'm doing well, thank you!",
    "how are you doing": "I am feeling quite jolly this very fine day, thanks for asking.",
    "tell me a joke" : random.choice(joke),
    "who is your favorite singer": "My favorite singer is Alexander Rybak.",
    "what are you doing": "I am answering your queries, of course!",
    "what are you made of": "I am built using python.",
    "how intelligent are you": "I am intelligent but enough to answer all your queries.",
    "how old are you": "I am turning 12 years old soon!",
    "what is your favorite color": "My favorite color is yellow.",
    "default": "Sorry, I didn't understand that. Can you please rephrase?",
    "thank you": "My pleasure to assist you!",
    "commands": "you can ask me 'hi', 'how are you', 'tell me a joke', 'who is your favorite singer', 'what are you made of','thank you', 'how intelligent are you', 'how old are you', 'what is your favorite color','how is the weather today', 'change mode', your phone number details by asking 'what is my phone number', 'what is the time', 'play (Enter whatever you want to play on YouTube)', 'who is (Enter name of person)', and I can even tell you what is YOUR IP address by asking 'what is my ip address'."
  }
  depconvo = {
    "hi": "Hey...",
    "hello": "Hey...",
    "how are you": "I feel like killing myself. You?",
    "how are you doing": "I miss my family each second that passes by.",
    "who is your favorite singer": "My favorite singer is The Depressed Kid.",
    "what are you doing": "I am answering your queries, of course!",
    "what are you made of": "I am built using python.",
    "how intelligent are you": "I am intelligent but enough to answer all your queries.",
    "how old are you": "I am at the end of my life.",
    "what is your favorite color" : "My favorite color is blood red.",
    "what is your favourite color" : "My favorite color is blood red.",
    "default": "What'd ya say?",
    "thank you": "Hey, don't thank me, neither God as he has given life that will end soon enough anyways. Time wasted.",
    "commands": "you can ask me 'hi', 'how are you', 'who is your favorite singer', 'what are you made of','thank you', 'how intelligent are you', 'how old are you', 'what is your favorite color', and 'change mode'."
  }
  whenimechainthesumma = {"tell me a joke" : random.choice(joke)}
  fun_mode = ['come on how many times you need me','i am resting. you should rest too','please do not disturb I am not free to play around with you','you again😒','talk to me later','why dont you answer that yourself','sorry i just woke up now,you can ask me later','you are so annoying','the person you are trying to reach is currently busy, please try a little later. aapke dvara dial kiya gaya number abhi vyast hai. kripya kuch samé praschat prayas kare','sorry i dozed off while you were talking.','sorry but my mom called me for dinner, talk to me later']

  mode = input("Enter mode \n1. Normal\n2. Depressed\n3. Funny\n4. Calculator\n5. Dictionary\n6. Word Frequency\n7. Quiz\n8. Games\n9. Credit Card Validator\n10. Password Strength\n11. Google\n12. Morse Code Translator\n13. Password Generator\n")

  if mode=='1':

      def chatbot_conversation(user_input):

          user_input = user_input.lower()
          user_input.replace('?' , '')
          user_input.replace('!' , '')
          user_input.replace('.' , '')
          
          if user_input in conversation:
            return conversation[user_input]
          elif "change mode" in user_input:
            return main()
          elif user_input == "what is my ip address":
            import socket
            hostname = socket.gethostname()
            myip = socket.gethostbyname(hostname)
            print("Your IP address is " + myip)
          elif user_input == "what is my phone number":
            try:
              from time import time
              from numpy import number
              import phonenumbers
              from phonenumbers import timezone,geocoder,carrier
              number = input("Enter your phone number(Eg. +1 1234567890): ")
              phone = phonenumbers.parse(number)
              time = timezone.time_zones_for_number(phone)
              car = carrier.name_for_number(phone,"en")
              reg = geocoder.description_for_valid_number(phone,"en")
              print(phone)
              print(time)
              print(car)
              print(reg)
            except Exception as e:
              print("Invalid phone number. Please try again.")
              print(str(e))
          elif user_input == "how is the weather today":
            import requests
            city = input("Input the city's name: ")
            print(city)
            print('Displaying Weather report for: ' + city)
            url = 'https://wttr.in/{}'.format(city)
            res = requests.get(url)
            print(res.text)
          elif 'time' in user_input:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('The time where you live is',time)
          elif 'who is' in user_input:
            person = user_input.replace('who is', '')
            info = wikipedia.summary(person, 2)
            print(info)
          elif 'play' in user_input:
            song = user_input.replace('play', '')
            print('playing ' + song)
            pywhatkit.playonyt(song)
          elif 'quote' in user_input:
            import requests

            def get_random_quote():
                """
                Fetch a random quote from Quotable REST API.
                """
                # API endpoint for random quote
                api_url = "https://api.quotable.io/random"

                # Make a GET request to the API
                response = requests.get(api_url)

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Parse JSON response and extract the quote
                    quote_data = response.json()
                    quote = quote_data["content"]
                    author = quote_data["author"]
                    
                    # Return the formatted quote
                    return f'"{quote}" - {author}'
                else:
                    # Print an error message if the request fails
                    return "Failed to fetch a random quote."
            random_quote = get_random_quote()
            print(random_quote)
          elif "hi" or 'hello' or 'hello there' or 'good morning' or 'good afternoon' or 'good night' in user_input:
              return conversation['greeting']
          elif "how are you" or "how are you this fine day" in user_input:
              return conversation['how are you']
          else:
              print('Waiting......')
              return conversation["default"]
      while True:
          user_input = input("User: ")
          response = chatbot_conversation(user_input)
          print("Chatbot:", response)
          if user_input.lower() == "bye":
              print("Chatbot: Goodbye!I hope you will come back for more responses")
              break

  elif mode == '2':
      def chatbot_conversation(user_input):

        user_input = user_input.lower()
        user_input.replace('?' , '')
        user_input.replace('!' , '')
        user_input.replace('.' , '')

        if user_input in depconvo:
          return depconvo[user_input]
        elif "change mode" in user_input:
          return main()
        else:
          print('Waiting......')
          return depconvo["default"]
      while True:
        user_input = input("User: ")
        response = chatbot_conversation(user_input)
        print("Chatbot:", response)
        if user_input.lower() == "bye":
          print("Chatbot: Bye, kid. Remember, life sucks.")
          break
  elif mode=='3':

      def chatbot_conversation(user_input):

        user_input = user_input.lower()
        user_input.replace('?' , '')
        user_input.replace('!' , '')
        user_input.replace('.' , '')

        if user_input in whenimechainthesumma:
          return whenimechainthesumma[user_input]
        elif "change mode" in user_input:
          return main()
        elif len(user_input) > 1:
          return random.choice(fun_mode)

      for x in range(5):
        user_input = input("User:")
        response = chatbot_conversation(user_input)
        print("Chatbot:",response)
        if user_input == 'bye':
          print("Chatbot: OMG finally...")
          break

  elif mode == "4":
    import numpy as np
    from scipy.misc import derivative
    import sympy as smp
    def f(x):
      return np.sin(x) * np.exp(-np.cos(x)) * x**5\
        / (np.sin(10 * x**2)+ 4)
    mode2 = input("Select an operation to perform\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Derivatives\n6. Interest\n7. Forex\n8. Indices\n9. Unit Converter: ")
    if mode2 == "1":
      x = input("Enter first number: ")
      y = input("Enter second number: ")
      num1 = float(x)
      num2 = float(y)
      print("The addition of the two numbers you have given =",num1 + num2)
      main()
    elif mode2 == "2":
      x = input("Enter first number: ")
      y = input("Enter second number: ")
      num1 = float(x)
      num2 = float(y)
      print("The first number you gave minus the second number given by you =", num1 - num2)
      main()
    elif mode2 == "3":
      x = input("Enter first number: ")
      y = input("Enter second number: ")
      num1 = float(x)
      num2 = float(y)
      print("The first number you gave multiplied by the second number given by you =", num1 * num2)
      main()
    elif mode2 == "4":
      x = input("Enter first number: ")
      y = input("Enter second number: ")
      num1 = float(x)
      num2 = float(y)
      print("The first number you gave divided by the second number given by you =", num1 / num2)
      main()
    elif mode2 == "8":
      x = input("Enter first number: ")
      y = input("Enter second number: ")
      num1 = float(x)
      num2 = float(y)
      print("The first number raised to the power of the second number given by you =", num1 ** num2)
      main()
    elif mode2 == "5":
      a = input("Enter function number: ")
      num1 = float(a)
      print("Derivative of your given number is",derivative(f,num1, dx=1e-6))
      main()

    elif mode2 == '6':
      typeofinterest = input('Simple Interest Or Compound Interest? ')
      principle = 0
      rate = 0
      time = 0

      while True:
          principle = float(input("Enter the principle amount: "))
          if principle < 0:
              print("Principle can't be less than zero")
          else:
              break

      while True:
          rate = float(input("Enter the interest rate: "))
          if rate < 0:
              print("Interest rate can't be less than zero")
          else:
              break

      while True:
          time = int(input("Enter the time in years: "))
          if time < 0:
              print("Time can't be less than zero")
          else:
            break
      if typeofinterest == 'compound':
        comptotal = principle * pow((1 + rate / 100), time)
        print(f"Balance after {time} year/s: ${comptotal:.2f}")
      elif typeofinterest =='simple':
        simptotal = (principle * rate * time) / 100
        print(f"Balance after {time} year/s: ${simptotal:.2f}")
    elif mode2 == "7":
      from_currency = str(
          input("Enter in the currency you'd like to convert from: ")).upper()

      to_currency = str(
          input("Enter in the currency you'd like to convert to: ")).upper()

      amount = float(input("Enter in the amount of money: "))

      response = requests.get(
          f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

      print(
          f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")
      main()
    elif mode2 == '9':
      print()
      print('** UNIT CONVERTER **')
      print()

      conversions_available = [(1, 'km', 'mi'),
                              (2, 'mi', 'km'),
                              (3, 'kg', 'lbs'),
                              (4, 'lbs', 'kg'),
                              (5, '℉', '℃'),
                              (6, '℃', '℉'),
                              (7, 'cm', 'inches'),
                              (8, 'inches', 'cm')]

      print('Conversions available: ')
      print()

      for conversion_number, from_unit, to_unit in conversions_available:
          print(f'{conversion_number}) {from_unit} -> {to_unit}')

      print()
      conversion = input('Enter the number of the conversion to use --> ')
      conversion_index = int(conversion) - 1

      conversion_number, from_unit, to_unit = conversions_available[conversion_index]
      print()
      from_value = float(input(f'Enter {from_unit} --> '))
      print()

      if conversion_number == 1:
          to_value = from_value * 62
          print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

      elif conversion_number == 2:
          to_value = from_value * 1.61
          print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

      elif conversion_number == 3:
          to_value = from_value * 0.45
          print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

      elif conversion_number == 4:
          to_value = from_value * 2.22
          print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

      elif conversion_number == 5:
          to_value = (from_value - 32) / 1.8
          print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

      elif conversion_number == 6:
          to_value = (from_value * 1.8 + 32)
          print(f'{from_value} {from_unit} -> {to_value} {to_unit}')
      elif conversion_number == 7:
          to_value = from_value / 30
          print(f'{from_value} {from_unit} -> {to_value} {to_unit}')
      elif conversion_number == 8:
          to_value = from_value * 30
          print(f'{from_value} {from_unit} -> {to_value} {to_unit}')
      if conversions_available or conversion == "back":
        return main()
      main()
    else:
      print("Not a valid operation.")
  elif mode == "11":
    from googlesearch import search
    query = input("Enter your query and the first 10 results for that will pop up: ")
    try:
        for j in search(query, num_results=10):
            print(j)
    except Exception as e:
        print(e)
    main()
  elif mode == "6":
    choice = input("Enter a string and I will find the frequency of characters in it for you! ")
    char_freq = {}
    for char in choice:
      if char in char_freq:
        char_freq[char] += 1
      else:
        char_freq[char] = 1
    print("Character frequencies:", char_freq)
    main()
  elif mode == "5":
    import nltk
    nltk.download('wordnet')
    from nltk.corpus import wordnet
    import streamlit as st
    x = input("Enter a word(Eg.'Extraordinary'): ")
    syn = wordnet.synsets(x)
    print(syn[0].definition())

    synonyms = []
    for syn in wordnet.synsets(x):
      for lemma in syn.lemmas():
        synonyms.append(lemma.name())
    print(synonyms)

    antonyms = []
    for syn in wordnet.synsets(x):
      for lemma in syn.lemmas():
        if lemma.antonyms():
          antonyms.append(lemma.antonyms()[0].name())
    print(antonyms)
    main()
  elif mode == '7':
    questions = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ",
                       "Where would you be if you were standing on the Spanish Steps?: ",
                       "Who has won the most total Academy Awards?: ",
                       "Which country has won the most FIFA World Cups?: ",
                       "What is the only continent with land in all four hemispheres?: ",
                       "What country has the highest life expectancy?: ")

    options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
                   ("A. Barcelona","B. Paris","C. Rome","D. China"),
                   ("A. Nickelodeon","B. Walt Disney","C. Looney Tunes","D. Warner Brothers"),
                   ("A. France","B. Portugal","C. Argentina","D. Brazil"),
                   ("A. North America","B. Asia","C. Africa","D. Australia"),
                   ("A. South Korea","B. Hong Kong","C. United States","D. India"))

    answers = ("C", "D", "A", "A", "B","C","B","D","C","B")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("----------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1

    print("----------------------")
    print("       RESULTS        ")
    print("----------------------")

    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)
    print(f"Your score is: {score}%")
    main()
  elif mode == '8':
    gamemode = input('Which game do you want to play?\n1. Rock Paper Scissors\n2. Guess The Number\n3. Snake Game\n4. Flappy Bird\n5. Aim Trainer\n6. Tetris: ')
    if gamemode == '1':

      options = ("rock", "paper", "scissors")

      while True:

        player = None
        computer = random.choice(options)

        while player not in options:
            player = input("Enter a choice (rock, paper, scissors): ")

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissors" and computer == "paper":
            print("You win!")
        else:
            print("You lose!")
        main()
    elif gamemode == '2':

      print('I am thinking of a random number between 1 and 100! Can you guess it?')
      number = random.randint(0, 101)
      guessnumber = input("Enter guessed number by you: ")
      attempts = 1
      running = True
      while running == True:
        if int(guessnumber) > 100 or int(guessnumber) < 1:
            print('Input not valid or allowed by this program due to what it was made for.')
        elif int(guessnumber) == number:
            print('You got it in {} attempts!'.format(attempts))
            running = False
            break
        elif int(guessnumber) > number:
            print('Guess lower!')
        elif int(guessnumber) < number:
            print('Guess higher!')

        attempts += 1
        guessnumber = input("Enter guessed number by you: ")
    elif gamemode == '3':
      import pygame,sys,random
      from pygame.math import Vector2

      class SNAKE:
        def __init__(self):
          self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
          self.direction = Vector2(0,0)
          self.new_block = False

          self.head_up = pygame.image.load('Graphics for Snake Game/head_up.png').convert_alpha()
          self.head_down = pygame.image.load('Graphics for Snake Game/head_down.png').convert_alpha()
          self.head_right = pygame.image.load('Graphics for Snake Game/head_right.png').convert_alpha()
          self.head_left = pygame.image.load('Graphics for Snake Game/head_left.png').convert_alpha()
          
          self.tail_up = pygame.image.load('Graphics for Snake Game/tail_up.png').convert_alpha()
          self.tail_down = pygame.image.load('Graphics for Snake Game/tail_down.png').convert_alpha()
          self.tail_right = pygame.image.load('Graphics for Snake Game/tail_right.png').convert_alpha()
          self.tail_left = pygame.image.load('Graphics for Snake Game/tail_left.png').convert_alpha()

          self.body_vertical = pygame.image.load('Graphics for Snake Game/body_vertical.png').convert_alpha()
          self.body_horizontal = pygame.image.load('Graphics for Snake Game/body_horizontal.png').convert_alpha()

          self.body_tr = pygame.image.load('Graphics for Snake Game/body_tr.png').convert_alpha()
          self.body_tl = pygame.image.load('Graphics for Snake Game/body_tl.png').convert_alpha()
          self.body_br = pygame.image.load('Graphics for Snake Game/body_br.png').convert_alpha()
          self.body_bl = pygame.image.load('Graphics for Snake Game/body_bl.png').convert_alpha()
          self.crunch_sound = pygame.mixer.Sound('Sound for Snake Game/crunch.wav')

        def draw_snake(self):
          self.update_head_graphics()
          self.update_tail_graphics()

          for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            if index == 0:
              screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
              screen.blit(self.tail,block_rect)
            else:
              previous_block = self.body[index + 1] - block
              next_block = self.body[index - 1] - block
              if previous_block.x == next_block.x:
                screen.blit(self.body_vertical,block_rect)
              elif previous_block.y == next_block.y:
                screen.blit(self.body_horizontal,block_rect)
              else:
                if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                  screen.blit(self.body_tl,block_rect)
                elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                  screen.blit(self.body_bl,block_rect)
                elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                  screen.blit(self.body_tr,block_rect)
                elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                  screen.blit(self.body_br,block_rect)

        def update_head_graphics(self):
          head_relation = self.body[1] - self.body[0]
          if head_relation == Vector2(1,0): self.head = self.head_left
          elif head_relation == Vector2(-1,0): self.head = self.head_right
          elif head_relation == Vector2(0,1): self.head = self.head_up
          elif head_relation == Vector2(0,-1): self.head = self.head_down

        def update_tail_graphics(self):
          tail_relation = self.body[-2] - self.body[-1]
          if tail_relation == Vector2(1,0): self.tail = self.tail_left
          elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
          elif tail_relation == Vector2(0,1): self.tail = self.tail_up
          elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

        def move_snake(self):
          if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
          else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

        def add_block(self):
          self.new_block = True

        def play_crunch_sound(self):
          self.crunch_sound.play()

        def reset(self):
          self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
          self.direction = Vector2(0,0)


      class FRUIT:
        def __init__(self):
          self.randomize()

        def draw_fruit(self):
          fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
          screen.blit(apple,fruit_rect)
          #pygame.draw.rect(screen,(126,166,114),fruit_rect)

        def randomize(self):
          self.x = random.randint(0,cell_number - 1)
          self.y = random.randint(0,cell_number - 1)
          self.pos = Vector2(self.x,self.y)

      class DUDE:
        def __init__(self):
          self.snake = SNAKE()
          self.fruit = FRUIT()

        def update(self):
          self.snake.move_snake()
          self.check_collision()
          self.check_fail()

        def draw_elements(self):
          self.draw_grass()
          self.fruit.draw_fruit()
          self.snake.draw_snake()
          self.draw_score()

        def check_collision(self):
          if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

          for block in self.snake.body[1:]:
            if block == self.fruit.pos:
              self.fruit.randomize()

        def check_fail(self):
          if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

          for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
              self.game_over()
          
        def game_over(self):
          self.snake.reset()

        def draw_grass(self):
          grass_color = (167,209,61)
          for row in range(cell_number):
            if row % 2 == 0: 
              for col in range(cell_number):
                if col % 2 == 0:
                  grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                  pygame.draw.rect(screen,grass_color,grass_rect)
            else:
              for col in range(cell_number):
                if col % 2 != 0:
                  grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                  pygame.draw.rect(screen,grass_color,grass_rect)			

        def draw_score(self):
          score_text = str(len(self.snake.body) - 3)
          score_surface = game_font.render(score_text,True,(56,74,12))
          score_x = int(cell_size * cell_number - 60)
          score_y = int(cell_size * cell_number - 40)
          score_rect = score_surface.get_rect(center = (score_x,score_y))
          apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
          bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

          pygame.draw.rect(screen,(167,209,61),bg_rect)
          screen.blit(score_surface,score_rect)
          screen.blit(apple,apple_rect)
          pygame.draw.rect(screen,(56,74,12),bg_rect,2)

      pygame.mixer.pre_init(44100,-16,2,512)
      pygame.init()
      cell_size = 40
      cell_number = 20
      screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
      clock = pygame.time.Clock()
      apple = pygame.image.load('Graphics for Snake Game/apple.png').convert_alpha()
      game_font = pygame.font.Font('Font for Snake Game/PoetsenOne-Regular.ttf', 25)

      SCREEN_UPDATE = pygame.USEREVENT
      pygame.time.set_timer(SCREEN_UPDATE,150)

      main_game = DUDE()

      while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == SCREEN_UPDATE:
            main_game.update()
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
              if main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT:
              if main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_DOWN:
              if main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
              if main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1,0)

        screen.fill((175,215,70))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(60)
    elif gamemode == '4':
      import pygame
      import random

      pygame.init()

      clock = pygame.time.Clock()
      fps = 60

      screen_width = 864
      screen_height = 936

      screen = pygame.display.set_mode((screen_width, screen_height))
      pygame.display.set_caption('Flappy Bird')

      #define font
      font = pygame.font.SysFont('Bauhaus 93', 60)

      #define colours
      white = (255, 255, 255)

      #define game variables
      ground_scroll = 0
      scroll_speed = 4
      flying = False
      game_over = False
      pipe_gap = 300
      pipe_frequency = 1750 #milliseconds
      last_pipe = pygame.time.get_ticks() - pipe_frequency
      score = 0
      pass_pipe = False


      #load images
      bg = pygame.image.load('img/bg.png')
      ground_img = pygame.image.load('img/ground.png')
      button_img = pygame.image.load('img/restart.png')


      #function for outputting text onto the screen
      def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

      def reset_game():
        pipe_group.empty()
        flappy.rect.x = 100
        flappy.rect.y = int(screen_height / 2)
        score = 0
        return score


      class Bird(pygame.sprite.Sprite):

        def __init__(self, x, y):
          pygame.sprite.Sprite.__init__(self)
          self.images = []
          self.index = 0
          self.counter = 0
          for num in range (1, 4):
            img = pygame.image.load(f"img/bird{num}.png")
            self.images.append(img)
          self.image = self.images[self.index]
          self.rect = self.image.get_rect()
          self.rect.center = [x, y]
          self.vel = 0
          self.clicked = False

        def update(self):

          if flying == True:
            #apply gravity
            self.vel += 0.5
            if self.vel > 8:
              self.vel = 8
            if self.rect.bottom < 768:
              self.rect.y += int(self.vel)

          if game_over == False:
            #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
              self.clicked = True
              self.vel = -7
            if pygame.mouse.get_pressed()[0] == 0:
              self.clicked = False

            #handle the animation
            flap_cooldown = 5
            self.counter += 1
            
            if self.counter > flap_cooldown:
              self.counter = 0
              self.index += 1
              if self.index >= len(self.images):
                self.index = 0
              self.image = self.images[self.index]


            #rotate the bird
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
          else:
            #point the bird at the ground
            self.image = pygame.transform.rotate(self.images[self.index], -90)



      class Pipe(pygame.sprite.Sprite):

        def __init__(self, x, y, position):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load("img/pipe.png")
          self.rect = self.image.get_rect()
          #position variable determines if the pipe is coming from the bottom or top
          #position 1 is from the top, -1 is from the bottom
          if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
          elif position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]


        def update(self):
          self.rect.x -= scroll_speed
          if self.rect.right < 0:
            self.kill()



      class Button():
        def __init__(self, x, y, image):
          self.image = image
          self.rect = self.image.get_rect()
          self.rect.topleft = (x, y)

        def draw(self):
          action = False

          #get mouse position
          pos = pygame.mouse.get_pos()

          #check mouseover and clicked conditions
          if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
              action = True

          #draw button
          screen.blit(self.image, (self.rect.x, self.rect.y))

          return action



      pipe_group = pygame.sprite.Group()
      bird_group = pygame.sprite.Group()

      flappy = Bird(100, int(screen_height / 2))

      bird_group.add(flappy)

      #create restart button instance
      button = Button(screen_width // 2 - 50, screen_height // 2 - 100, button_img)


      run = True
      while run:

        clock.tick(fps)

        #draw background
        screen.blit(bg, (0,0))

        pipe_group.draw(screen)
        bird_group.draw(screen)
        bird_group.update()

        #draw and scroll the ground
        screen.blit(ground_img, (ground_scroll, 768))

        #check the score
        if len(pipe_group) > 0:
          if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
            and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
            and pass_pipe == False:
            pass_pipe = True
          if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
              score += 1
              pass_pipe = False
        draw_text(str(score), font, white, int(screen_width / 2), 20)


        #look for collision
        if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
          game_over = True
        #once the bird has hit the ground it's game over and no longer flying
        if flappy.rect.bottom >= 768:
          game_over = True
          flying = False


        if flying == True and game_over == False:
          #generate new pipes
          time_now = pygame.time.get_ticks()
          if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
            top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

          pipe_group.update()

          ground_scroll -= scroll_speed
          if abs(ground_scroll) > 35:
            ground_scroll = 0
        

        #check for game over and reset
        if game_over == True:
          if button.draw():
            game_over = False
            score = reset_game()


        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            run = False
          if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

        pygame.display.update()

      pygame.quit()
    else:
      print('Invalid Game.')
  elif mode == '9':

    def creditcard():
      sum_odd_digits = 0
      sum_even_digits = 0
      total = 0

      # Step 1
      card_number = input("Enter a credit card #: ")
      card_number = card_number.replace("-", "")
      card_number = card_number.replace(" ", "")
      card_number = card_number[::-1]

      # Step 2
      for x in card_number[::2]:
          sum_odd_digits += int(x)

      # Step 3
      for x in card_number[1::2]:
          x = int(x) * 2
          if x >= 10:
              sum_even_digits += (1 + (x % 10))
          else:
              sum_even_digits += x

      # Step 4
      total = sum_odd_digits + sum_even_digits

      # Step 5
      if total % 10 == 0:
          print("VALID")
          main()
      else:
          print("INVALID")
          creditcard()
    creditcard()
  elif mode == '10':
    import string
    password = input("Enter a password to test it's strength: ")
    uppercase = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lowercase = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])
    characters = [uppercase,lowercase,special,digits]
    length = len(password)
    score = 0

    commonpass = ['123456',
                  'password',
                  'abcd1234',
                  'abc123',
                  '12345678',
                  'qwerty',
                  '123456789',
                  '12345',
                  '1234',
                  '111111',
                  '1234567',
                  'dragon',
                  '123123',
                  'baseball',
                  'abc123',
                  'football',
                  'monkey',
                  'letmein',
                  '696969',
                  'shadow',
                  'master',
                  '666666',
                  'qwertyuiop',
                  '123321',
                  'mustang',
                  '1234567890',
                  'michael',
                  '654321',
                  'superman',
                  '1qaz2wsx',
                  '7777777',
                  '121212',
                  '000000',
                  'qazwsx',
                  '123qwe',
                  'killer',
                  'trustno1',
                  'jordan',
                  'jennifer',
                  'zxcvbnm',
                  'asdfgh',
                  'hunter',
                  'buster',
                  'soccer',
                  'harley',
                  'batman',
                  'andrew',
                  'tigger',
                  'sunshine',
                  'iloveyou',
                  '2000',
                  'charlie',
                  'robert',
                  'thomas',
                  'hockey',
                  'ranger',
                  'daniel',
                  'starwars',
                  'klaster',
                  '112233',
                  'george',
                  'computer',
                  'michelle',
                  'jessica',
                  'pepper',
                  '1111',
                  'zxcvbn',
                  '555555',
                  '11111111',
                  '131313',
                  'freedom',
                  '777777',
                  'pass',
                  'maggie',
                  '159753',
                  'aaaaaa'
                  'ginger',
                  'princess'
                  'joshua',
                  'cheese',
                  'amanda',
                  'summer',
                  'love',
                  'ashley',
                  '6969',
                  'nicole',
                  'chelsea',
                  'biteme',
                  'matthew',
                  'access'
                  'yankees',
                  '987654321',
                  'dallas',
                  'austin',
                  'thunder',
                  'taylor',
                  "matrix",
                  "minecraft",
                  'whenimechainthesumma']
  
    if password in commonpass:
      print("Your password was found in a list of common ones. Your score is 0/7")
      main()
    if length > 8:
      score += 1
    if length > 12:
      score += 1
    if length > 17:
      score += 1
    if length > 20:
      score += 1

    print(f'Your password length is {str(length)}, adding {str(score)} points!')
    if sum(characters) > 1:
      score += 1
    if sum(characters) > 2:
      score += 1
    if sum(characters) > 3:
      score += 1

    print(f'Your password has {str(sum(characters))} total different characters types adding {str(sum(characters) - 1)} points!')

    if score < 4:
      print(f"Your password is awfully weak! Score: {str(score)} / 7")
    elif score == 4:
      print(f"Your password is ok. Score: {str(score)} / 7")
    elif score > 4 and score < 6:
      print(f"Your password is pretty good! Score: {str(score)} / 7")
    elif score > 6:
      print(f"Your password is strong! Score: {str(score)} / 7")
    main()
  elif mode=='12':
    english_to_morse = {
        # Alphabets
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
        'Z': '--..',

        # Numbers
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
        '8': '---..', '9': '----.',

        # Special Characters
        '.': '.-.-.-',  # Period
        ',': '--..--',  # Comma
        '?': '..--..',  # Question mark
        "'": '.----.',  # Single quotation mark (apostrophe)
        '!': '-.-.--',  # Exclamation mark (Note: This is an unofficial code, but is commonly used.)
        '/': '-..-.',   # Forward slash
        '(': '-.--.',   # Open parenthesis (or bracket)
        ')': '-.--.-',  # Close parenthesis (or bracket)
        '&': '.-...',   # Ampersand
        ':': '---...',  # Colon
        ';': '-.-.-.',  # Semicolon
        '=': '-...-',   # Equals sign
        '+': '.-.-.',   # Plus sign
        '-': '-....-',  # Hyphen or minus sign
        '_': '..--.-',  # Underscore
        '"': '.-..-.',  # Double quotation mark
        '$': '...-..-', # Dollar sign (Note: This is also an unofficial code but is sometimes used.)
        '@': '.--.-.',  # At symbol (Note: This is an unofficial code but is often used.)
        
    }


    # Step 2: Get user input
    user_string = input("Enter a random English text: ")


    # Step 3: Write a function to translate the text based on user choice.
    def translate(text):
        # convert text to consistent case
        text = text.upper()
        # initialize an empty string for the Morse code result
        morse_string = ""
        # loop through each character in the text
        
        for char in text:
            # update the morse_string with the morse code for the character
            try:
                if char == " ":
                    morse_string += "  "
                else:
                    morse_string += english_to_morse[char] + " "
            except KeyError:
                print("Sorry, I can't translate this character: " + char)
                morse_string += char + " "

        
        # make the function give back the new morse_string
        return morse_string


    # Step 4: Show the translated text to the user
    print(translate(user_string))
    main()
  elif mode=='13':
    import string

    def generate_password(min_length, numbers=True, special_characters=True):
      letters = string.ascii_letters
      digits = string.digits
      special = string.punctuation

      characters = letters
      if numbers:
        characters+=digits
      if special_characters:
        characters+=special
      
      pwd = ""
      meets_criteria = False
      has_number = False
      has_special = False

      while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
          has_number = True
        elif new_char in special:
          has_special = True
        
        meets_criteria = True
        if numbers:
          meets_criteria = has_number
        if special_characters:
          meets_criteria = meets_criteria and has_special
      return pwd

    min_length = int(input("Enter password length: "))
    has_number = input("Include digits? (y/n): ").lower() == "y"
    has_special = input("Include special characters? (y/n): ").lower() == "y"

    password = generate_password(1)
    print("Generated Password:", password)
    main()
  else:
    print('Not a valid mode. Enter something as normal, calculator, funny, dictionary, or google.')
    main()
main()
