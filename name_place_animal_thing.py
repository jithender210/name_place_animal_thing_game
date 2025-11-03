import nltk
import difflib
from nltk.corpus import wordnet
from nltk import word_tokenize,pos_tag,ne_chunk
import random
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download("words")
import time
class game():
    def __init__(self):
        pass
    def check_animal(self,animal):
        all_word=list(wordnet.all_lemma_names())
        close=difflib.get_close_matches(animal,all_word)
        animal=close[0]
        word=wordnet.synsets(animal)
         
        for sys in word:
            for hyper in sys.hypernym_paths():
                 
                for hyper1 in hyper:
                    if "animal" in hyper1.name().lower() or "bird" in hyper1.name().lower():
                        return True
        return False
    def check_name(self,name):
        tokens=nltk.word_tokenize(name)
        pos_tags=nltk.pos_tag(tokens)
         
        for word,tag in pos_tags:
            if tag in ["NN","NNS","NNP","NNPS"]:
                return True 
        return False
    def looks_like_non_place(self,word):
        syns = wordnet.synsets(word)
        for s in syns:
            # If WordNet says it's food, animal, or an artifact → Not a place
            if any(k in s.lexname() for k in ["noun.food", "noun.animal", "noun.artifact"]):
                return True
        return False

    def check_place(self,place):
        place=place.title()
        tokens=word_tokenize(place)
        pos_tags=pos_tag(tokens)
        chunks=ne_chunk(pos_tags)
          
        for chunk in chunks.subtrees():
            
            if hasattr(chunk,'label'):
                if chunk.label() in ["GPE","LOCATION","FACILITY"]:
                    if not self.looks_like_non_place(place):
                        return True

        return False
    def check_thing(self,thing):
        word=wordnet.synsets(thing)
        for sys in word:
            for hyper in sys.hypernym_paths():
                for hyper1 in hyper:
                    

                    if any(k in hyper1 .name() for k in ["artifact", "object", "instrumentality", "device", "tool", "furniture","implement",
                "equipment", "structure", "machine"]):
                        return True
        
g=game()
total=0
type=["Hi,👋👋 Welcome to name place animal thing game!",
      "here each coorect answer get 10 points 😊",
      "You will enloy the game 😄",
      "Let's start the game 🚀🚀"]
for i in type:
    for char in i:
        print(char,end="",flush=True)
        time.sleep(0.1)
    print()
while True:
    letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    letter=random.choice(letters)
    sum=0
    
    print("The Letter is :",letter)
    name=input("Enter the name with letter {}: ".format(letter))
    answer=g.check_name(name)
    if answer:
     sum+=10
    place=input("Enter the place with letter {}: ".format(letter))
    answer1=g.check_place(place)
    if answer1:
        sum+=10
    animal=input("Enter the animal name with letter {}: ".format(letter))
    result=g.check_animal(animal)
    if result:
     sum+=10
    thing=input("Enter the thing with letter {}: ".format(letter))
    answer2 =g.check_thing(thing)
    if answer2:
        sum+=10
    print("Your  Score is : ",sum)
    user_input=input("press enter to continue or type 'q' to quit: ")
    total+=sum
    if user_input.lower()=='q':
        break
    else:
        pass

print("Your Total Score is : ",total)


            
              

