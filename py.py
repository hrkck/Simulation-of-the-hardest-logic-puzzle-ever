from random import choice

class Guy:
  __iam = ''
  def __init__(self, whoami):
    self.__iam = whoami

  def ask(self, question):
    if(self.__iam == 'honest'): return question
    if(self.__iam == 'liar'): return not question
    if(self.__iam == 'random'): return choice([True,False])

  def whoami(self):
    return self.__iam


types = ['honest', 'liar', 'random']

alice = Guy(types.pop(choice(range(len(types)))))
bob = Guy(types.pop(choice(range(len(types)))))
chuck = Guy(types.pop(choice(range(len(types)))))

people = [alice, bob, chuck]
names = ['alice', 'bob', 'chuck']

x = choice([True,False])
shuffleAnswer = lambda answer: 'ka' if x==answer else 'da'

print("True is", shuffleAnswer(True), "and False is", shuffleAnswer(False))
print(alice.whoami())
print(bob.whoami ())
print(chuck.whoami())

while True:
  print("Alright, write below a person's name and start asking questions:")
  askMe = input("name: ")

  print("Now, formulate your question. You can ask such a question:")
  print("'", askMe, ", can you tell me if {person_name} is {type}?'", sep='')
  print("where personName = {alice, bob, chuck} and type = {honest, liar, random}")
  
  person_name = input("person_name:")
  type = input("type:")

  answer = ''
  exec("answer = " + askMe + ".ask(" + person_name + ".whoami() == '" + type +"')") # answer = chuck.ask(alice.whoami() == type)
  print(askMe, "answers:\t\t\t\t\t\t\t\t\t\t", shuffleAnswer(answer))


  # for c, person in enumerate(people):
  #   question = bool(input('Ask, '+names[c]+ ' True or False? '))
  #   print(names[c], "'s answer: ", person.ask(question))


# alice.whoami()
# bob.whoami()
# chuck.whoami()