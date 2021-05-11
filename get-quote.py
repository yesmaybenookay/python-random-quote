import random
def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0,last)

  print("\033[94m" + quotes[rnd], end="" + "\033[0m")

def addQuote():
  answer = None
  while answer not in ("YES", "NO"):
    answer = input("\033[91m" + "Do you want to add a new quote to this program? " + "\033[0m").upper()
    if answer == "YES":
      newQuote = input("\033[91m" + "Type the quote you want to add and then press Enter. " + "\033[0m") + "\n"
      f = open("quotes.txt", "a")
      f.write(newQuote)
      f.close()
    elif answer == "NO":
      print("\033[91m" + "Fine. Be that way!" + "\033[0m")
    else:
      print("\033[91m" + "Please enter yes or no." + "\033[0m")

if __name__== "__main__":
  primary()
  addQuote()
