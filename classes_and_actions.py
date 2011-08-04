



#
#richard_tynan_rpg
#
import random, time
import pprint
import interface
import level

end_game = False

global Dead
Dead = "deaderror"

class deaderror:
        def __init__(self, value):
            self.value = value
        def __repr__(self):
            return self.value


def start():
    try:
        x = game()
        x.play_game()
    except deaderror as x:
        print "You are dead: %s"%x

#class with data important for game play
class game:
    def __init__(self):
        self.richard = player()            #references player class to define self.richard
        self.i = interface.interpreter(self.richard)        #references interface function in interpreter module and uses player (self.richard) as an argument

        self.level_1 = level.level_1(self.i, self.richard)   #defines level.1 here as the level_1 function in level, calls interface and player class as arguments

        return None

    def play_game(self):
        self.richard.change_health(0)
        self.level_1.play()            #calls the play() function in the class level_1

def highscore(gamername, score):
    if gamername != "test":
            path = '/home/thomas/Python/richard rpg/scorecard.txt'            #must change this specfically for each computer... installation...?
            scorecard = open(path, 'a')
            layout =  "\n %s ----------------------------------> %s \n" % (gamername, score)
            scorecard.write(layout)
            scorecard.close()
    else:
        return
        
        
    
class player:
    def __init__(self):
        

        self.inventory = {}

        self.health = 100

        self.coffee = 1

        self.drunkenness = 0

        self.slippers = False

        self.cat_happyness = 60

        self.depression_level = 0

        return None

    def change_depression(self, x, volatile=False):            #something which makes richard more volatle if he's drunk?..
        self.depression_level = self.depression_level + x             #annoying depression function which makes the game proceed slower if richard is depressed

        if self.depression_level<-75:
            print "Woe. You are depressed."
            print
            time.sleep(3)
            print "Sighhhhhhhhhhhhhhhhhhhhhhhhhhhhhh..........."
            time.sleep(4)
            print "Sighhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh..................."
            print
            time.sleep(2)
            print "Sighhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh............."
            print

    def change_health(self, x, medipack=False):

        if self.health >=100:
            if medipack == True:
                    print "You are already at full health."
                    pass
            pass
        elif self.health <100 and self.health >0:
                count = 0
                while self.health < 100 and count < x:
                        count += 1
                        self.health = self.health + 1          
        elif self.health <= 0:
            raise deaderror("You have died due to ill health.")

        return None
                
    def add_inventory(self, item):
        if item not in self.inventory.keys():
            self.inventory[item] = 1
        else:
            self.inventory[item] = self.inventory[item] + 1
        
    def equip_slippers(self):
        if "Slippers" in self.inventory:
            self.slippers = True
            

    def placate_cat(self):
        if self.coffee < 30:
            print "You do not have enough coffee levels to placate cat"
            return False
        elif phone or laptop not in self.inventory:
             print "You do not have the right communications equipment to placate cat"
             return False
        elif self.cat_happyness > 80:
             print "Cat is doing fine already."
             return False
        else:
             print "You have successfully placated cat"
             return True



    def drink_coffee(self):
        """should check value of slippers, whether coffee is in inventory and return a random response, then icnreases coffee levels by 10"""
        
        if "Slippers" not in self.inventory:
            print "You don't have your slippers! You must have your slippers to drink coffee in this room."
            return False
        elif self.slippers == False:
            print "You haven't equipped your slippers."
            return False
        elif 'Coffee' not in self.inventory:
            print "You do not have any coffee in your inventory."
            return False
        else:
            integer = random.randint(1, 10)
            coffee_responses = {1:"You drink some coffee.", 2:"mmm, coffee", 3:"That's some fine coffee", 4:"Coffee. Fucking. Coffee.",
            5:"mmm, I love me some coffee", 6:"You drank the coffee", 7:"This coffee's gone cold, but you drink it anyway",
            8:"A fine coffee. This coffee would go well with... more coffee...",
            9:"You slightly burn yourself on the coffee. DEVELOP MINUS HEALTH FUNCTION", 10:"You accidentally spill some coffee. DEVELOP PLUS DEPRESSION FUNCION"}

        output = coffee_responses[integer]
        print output
        self.coffee = self.coffee + 10
        return

    def check_levels(self):
        print "Health", self.health
        print "Coffee", self.coffee
        print "Drunkenness", self.drunkenness
        print "Cat happyness", self.cat_happyness
        print "Depression levels", self.depression_level


    def display_inventory(self):
        for element in self.inventory:
            print element, ':', self.inventory[element]

            


    
    

               
                

            
          


