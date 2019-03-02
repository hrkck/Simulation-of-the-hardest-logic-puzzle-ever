import random as rnd

words = ['Da', 'Ja']
types = ['honest', 'liar', 'random']
names = ['Alice', 'Bob', 'Chuck']

class Guy:
    __iam = 'A Recursive Centaur, half Horse, half Recursive Centaur.'
    def __init__(self, whoami, name, language_vocabulary):
        self.__iam = whoami
        self.name = name
        self.vocabulary = language_vocabulary
        self.inverse_vocabulary = {language_vocabulary[key]: key for key in language_vocabulary.keys()}

    def ask(self, question):
        if(self.__iam == 'honest'): return question
        elif(self.__iam == 'liar'): return not question
        elif(self.__iam == 'random'): return rnd.choice([True,False])
        else:
            raise Exception("This dude is confused, he calls his personality {}".format(self.__iam))

    def full_ask(self, question):
        return self.inverse_vocabulary[self.ask(question)]

    def whoami(self):
        return self.__iam

    def reveal_myself(self):
        print("My name is {} and i am {}.".format(self.name, self.__iam))

def generate_people(vocabulary):
    rnd.shuffle(types)
    people = {}
    people["Alice"] = Guy(types[0], "Alice", vocabulary)
    people["Bob"] = Guy(types[1], "Bob", vocabulary)
    people["Chuck"] = Guy(types[2], "Chuck", vocabulary)
    return people

def generate_meaning():
    meanings = [True, False]
    rnd.shuffle(meanings)
    mapping = {words[i]:meanings[i] for i in range(len(words))}
    return mapping

def reveal_characters(characters):
    for character_name in characters.keys():
        characters[character_name].reveal_myself()

# TODO: Simplify this and add possibility to ask about past and to ask about if someone would reply Ja/Da to specific question
def question_loop(previous_question):
    aboutSubject = input("Is the question about another subject?  (y / n):  ")
    if aboutSubject == 'y':

        whichSubject = None
        while whichSubject is None:
            whichSubject = input("About who is the question?  (Alice / Bob / Chuck):  ")
            if whichSubject not in names:
                print("You inserted an invalid response, you answered [{}], but only [Alice], [Bob] and [Chuck] are allowed.".format(whichSubject))
                whichSubject = None

        aboutQuestion = input("Is the question about what that subject would say?  (y / n):  ")
        if aboutQuestion == 'y':
            print("Describe now what your inquiry to the other subject be about.")
            question_filler = whichSubject + ".ask({})"
            current_question = previous_question.format(question_filler)
            print(current_question)
            return question_loop(current_question)

        elif aboutQuestion == 'n':
            return ask_subject_attitude(previous_question, whichSubject)

        else:
            print("You inserted an invalid response, you answered [{}], but only [y] and [n] are allowed.".format(aboutQuestion))

    elif aboutSubject == 'n':
        aboutLanguage = None
        while aboutLanguage is None:
            aboutLanguage = input("Is the question about the language?  (y / n):  ")
            if aboutLanguage == 'y':
                return ask_language_question(previous_question)
            elif aboutLanguage == 'n':
                return ask_true(previous_question)
            else:
                print("You inserted an invalid response, you answered [{}], but only [y] and [n] are allowed.".format(aboutLanguage))
                aboutLanguage = None

    else:
        print("You inserted an invalid response, you answered [{}], but only [y] and [n] are allowed.".format(aboutSubject))
        return question_loop(previous_question)


def ask_language_question(previous_question, vocabulary):
    print("Without loss of generality we will ask if Ja means Yes")
    question_filler = "vocabulary['Ja'] == True"
    current_question = previous_question.format(question_filler)
    return current_question

def ask_true(previous_question):
    print("Without loss of generality we will ask if True==True")
    current_question = previous_question.format("True")
    return current_question

def ask_subject_attitude(previous_question, subject):
    subjectAttitude = input("What would you like to ask if {} is?  (honest / liar / random):  ".format(subject))
    question_filler = "{}.whoami() == '{}'".format(subject, subjectAttitude)
    return previous_question.format(question_filler)

def create_question(question_n):
    askTo = None
    while askTo is None:
        askTo = input("To whom do you wish to ask question number {} (Alice / Bob / Chuck)? ".format(question_n))
        if askTo not in names:
            print("You can only ask to one of {}. You inserted {}, which is not available".format(names, askTo))
            askTo =  None
    initial_question = "{}"
    question = question_loop(initial_question)
    return askTo, question

def answer_question(subject, question, vocabulary):
    print(question)
    questions_answer = exec(question)
    subjects_answer = subject.full_ask(questions_answer)
    return subjects_answer

word_to_meaning = generate_meaning()
meaning_to_word = {word_to_meaning[key]: key for key in word_to_meaning.keys()}
people = generate_people(word_to_meaning)
Alice = people['Alice']
Bob = people['Bob']
Chuck = people['Chuck']


questions_count = 1
while questions_count<=3:
    subject, question = create_question(questions_count)
    answer = answer_question(people[subject], question, word_to_meaning)
    print("{}, to the question:\n{}\nanswers:\n\t{}".format(subject, question, answer))
    questions_count += 1

input("Ready to know who we are?")
reveal_characters(people)
print("Did you guess us right?")
