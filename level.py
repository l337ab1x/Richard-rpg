
#
#level
#

import time, random, classes_and_actions, interface



def cat_calls(playerassignment, x=1, y=1):
    """function where cat calls and gives random dictionary response, or assigned response based on input x=1 or not. If response is acceptable, consequences.
       note room for expansion using assigned responses left."""
    integer, integer2 = random.randint(1, 10), random.randint(1, 3)
    phone_dict = {1:"Your mobile telephone device begins to ring.", 2:"Your mobile rings.", 3:"Your chair vibrates expectantly."}
    cat_topics = {1:"Your woman, Cataus, is upset about something or other.", 2:"Cat enquires as to why you did not answer her previous call.",
                  3:"'Love you', says Cat", 4:"'Are you ignoring me?' says Cat.", 5:"Your girlfriend, Cat, tells you an amusing anecdote about a bear stuck in a pond.",
                  6:"Cat recommends some tv programme for you to watch on iplayer.", 7:"Cat is drunk. She tells you about an exciting event happening nearby.", 
                  8:"Your woman Cat, talks about arts and crafts for a while and you doze off to the sound of her voice.", 9:"Love you!", 10:"Love you?!"}

    i = interface.interpreter(playerassignment)
    
    if x == 1:            #x=1 is cat_calls with random variable
        print phone_dict[integer2]
        time.sleep(1)
        z = i.read()
        acceptable_responses = ["answerphone", "answerthephone", "answer"]
        if z in acceptable_responses:      #possible ways of answering phone
            print cat_topics[integer]
            print
            answer = i.read()                       #if richard answers the phone and chooses the correct answer then he will reap benefits
            cap = playerassignment
            if integer > 4 and answer == "loveyou":
                cap.change_health(20)
                cap.depression_level = cap.depression_level - 5
                cap.coffee = cap.coffee + 5
            elif integer <= 4 and answer == "lethertalkforawhile" or "talk":
                cap.change_health(20)
                cap.depression_level = cap.depression_level - 5
                cap.coffee = cap.coffee + 5
            else:
                cap.change_health(-20)            # but if not there will be consequences
                cap.depression_level = cap.depression_level -5
                cap.coffee = cap.coffee - 5
                
    else:
        pass
##            print "You do not answer the phone." #consequences should be added when someone can be bothered
##    else:
##        print phone_dict[y]           #room left for specific phonecall expansion here
##        time.sleep(1)
##        z = self.i.read()
##        pass #etc
##        cat_topics[x]
##    

def mother_calls(playerassignment):
    print "Your mother calls. She wants to know if you've done that thing he asked."
    mother_responses = ["yes", "ihave", "yup", "i'mdoingitnow", "saymaybe", "maybe"]
    other_responses = ["iwilldo"]
    i = interface.interpreter(playerassignment)
    z = i.read()
    if z in mother_responses:
        if playerassignment.coffee < 5:
            print "She wears you down and eventually you admit you haven't done that thing. Coping with your mother would be easier with more coffee."
            playerassignment.depression_level = playerassignment.depression_level - 20
        else:
            print "You have successfully coped with your mother's questions."
            playerassignment.depression_level = playerassignment.depression_level + 20
    elif z in other_responses:
        print "Tactical move. Telling your mother you will do something will work for now, but you can't get away wth it for too long..."
    else:
        print "I gave birth to you %s, you could at least do this one thing. I'm only trying to help you. I care about you %s and this is how i'm treated...." % (classes_and_actions.x.gamername, x.gamername)
        playerassignment.depression_level = playerassignment.depression_level - 40
        
        



def answer_or_not(x):
            """Determines whether player answers phone

            >>>answer_or_not("answerphone")
            You answer the phone.
            
            """
            count = 0         #if phone has been answered before
            secondcount = 0    #if phone has rang out

            suitable_answers = ["answerphone", "answeranyway", "pickupphone", "answer", "nevertheless", "answercall", "pickupcall"]
            if count == 0 and x in suitable_answers:
                print "You answer the phone."
                count += 1
                return True
            elif count > 0 or secondcount > 0 and x in suitable_answers:
                print "The phone isn't ringing."
                return False
            elif secondcount > 0 and x in suitable_answers:
                print "You missed the phone. What now?"
            else:
                print "The phone continues to ring."
                time.sleep(1)
                print "Ring ring."
                time.sleep(1)
                print "The caller hangs up."
                secondcount += 1
                time.sleep(1)

                return False


class level_1:
    def __init__(self, interface, richard):
        self.i = interface
        self.richard = richard
    def play(self):
        complete = False
        while complete == False:
            
            outcome, complete = self.introduction()   #returns a string and a boolean based on level completion


    def introduction(self):
        print "-----------------------------------------------"
        print "              The Life of Tynan                "
        print "-----------------------------------------------"

        print "Welcome to The Life of Tynan, a text based RPG that depicts on the exploits of Richard Tynan."
        time.sleep(2)
        gamer_name = raw_input("Enter your name to continue ")
        print "Welcome %s, you are now Richard Tynan!" % gamer_name

        score = 0
        
        classes_and_actions.highscore(gamer_name, score)
        
        print "--------------------------------------------------------"
        time.sleep(1)
        print
        print "You are sitting in a chair in the kitchen."
        print
        raw_input()
        print 
        print "You wake up! The room glows unnervingly. You realise this is sunlight."
        print
        time.sleep(3)
        print "You won't survive much longer without some kind of elevating beverage."
        print 
        print "--- Check your coffee levels with \"check levels\" ---"
        print "--- Need a coffee? Try \"search for coffee\" ---"
       
        while True:
            x = self.i.read()
            count = 0
            if x == "searchforcoffee":
                print "You find some coffee. It has been added to your inventory."
                self.richard.add_inventory("Coffee")
                break
            else:
                count += 1
                print "That's not how to search for coffee."
                
                
        print "Why not try drinking coffee from your inventory? Try 'Drink coffee'. "
        count = 0
        while True:
            x = self.i.read()
            if x == "searchforslippers":
                print "You find your slippers!"
                self.richard.add_inventory("Slippers")
                break
            else:
                count += 1
                if count == 3:
                    print "Why not try searching for your slippers?"
                elif count > 3:
                    print "Fucking search for your slippers. Type 'search for slippers'"
        count = 0
        while True:
            x = self.i.read()
            if  x == "equipslippers":
                print "You equip your slippers, you feel it is now safe to drink your coffee."
                self.richard.equip_slippers()
                break
            else:
                count += 1
                if count == 3:
                    print "You have your slippers right here, you have to do something with them, but what?"
                elif count > 3:
                    print "Possibly, equip them?"
                    
        print
        print "The phone rings, you know that if you were to answer it this tired, it could be dangerous."

        
        if answer_or_not(self.i.read()) == True:
            mother_calls(self.richard)
        else:
            print "That could have been your mother. Not answering might mean dire consequences later, but let's forget about that now... another coffee?"
            x = self.i.read()
            if x == "searchforcoffee":
                print "You find some coffee. It has been added to your inventory."
                self.richard.add_inventory("Coffee")

        print "The day's getting on. I wonder if much is happening on facebook..."
        
        facebook_list = ["checkfacebook", "facebook", "goonfacebook", "login", "logintofacebook", "loginfacebook", "lookonfacebook"]
        while True:
            x = self.i.read()
            count = 0
            if x in facebook_list and "Laptop" in self.richard.inventory:
                print "You check facebook. Ahh facebook. Nothing's happening here."
                self.richard.change_depression(10)
                break
            elif x in facebook_list and "Laptop" not in self.richard.inventory:
                print "You do not have your laptop. Wherever could it be?"
            elif x == "searchforlaptop":
                print "You find your laptop! It has been added to your inventory."
                self.richard.add_inventory("Laptop")
            elif x == "equiplaptop":
                print "You load up chrome and it crashes and brings down the desktop with it. You restart and can't help but wonder if this would have happened with a unix based OS..."
            else:
                count += 1
                if count < 3:
                    print "You really should check facebook before you continue your day. It's fairly imperative."
                else:
                    print "After failing to log onto facebook severaltimes you take a quick nap to recover."
                    print
                    print "On awakening you find facebook has magically appeared on your screen."
                    print
                    print "%s has posted a new status! ' %s smells'" % (gamer_name)
                    print

        score += 1

        print "Perhaps you should do something today."
        print
        

        
    
        
        time.sleep(1)
        
        mother_calls(self.richard)
            
            
        

        cat_calls(self.richard)

            
                

                

        return "works", True
            
                    
                
##if __name__ == "__main__":
##    import doctest
##    doctest.testmod()
                
        
            
