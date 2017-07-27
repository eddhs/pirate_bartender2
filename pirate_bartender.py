import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}
yes=1
y=1
no=0
n=0
answers={}
def user_pref():
    for x in questions:
        answer=input(questions[x])
        if answer == 1:
            answers[x]=True
        else:
            answers[x]=False
    return answers

def make_drink(answers,ingredients):
    print("I made ye a drink with these ingredients: ")
    for key,value in answers.items():
        if value == True:
            print("A {0}".format(ingredients[key][random.randint(0,2)]))
    return

if __name__ == "__main__":
    user_pref()
    make_drink(answers,ingredients)
    
        
    