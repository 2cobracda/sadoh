from numpy import random
rand = random.randint(10000) 
def wabi_sabi():
  if rand%2 == 0:
    print("茶道プログラムが動かない")
  elif rand%3 == 0:
    print("マヨでも吸ってな")
  else:
    print("結構なお点前で")
