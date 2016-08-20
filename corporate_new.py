from random import choice, randint
from twython import Twython
import argparse

#Grab more from https://en.wikipedia.org/wiki/List_of_buzzwords#Business.2C_sales_and_marketing

class Letter(object):
    def __init__(self):
        self.salutations1 = ["I RESPECT YOU", "WELL DONE", "KEEP IT UP",
                             "YOU DESERVE A PROMOTION", "YOU\'VE BEEN SO PROACTIVE", 
                             "GOOD WORK", "DON\'T GIVE UP", "YOU ARE ADMIRABLE", 
                             "YOUR EFFORT IS NOT WASTED", "QUIT AND BE MY PARTNER",
                             "YOU ARE CERTAINLY MOVING UP IN THE WORLD",
                             "I\'M IN AWE OF YOU", "PLEASE KEEP WORKING HERE"]
                             
        self.salutations2 = ["COWORKER", "SUBORDINATE", "BOSS", "MANAGER",
                             "FELLOW EMPLOYEE", "ASSISTANT", "REGIONAL MANAGER",
                             "SENPAI", "SENSEI", "MASTER", "LORD", "KING",
                             "YOUR HIGHNESS", "SIR", "MADAME", "SERVANT"]
                             
        self.adverbs      = ["SYNERGISTICALLY", "REASONABLY", "CAREFULLY",
                             "RESPECTFULLY", "DIRECTLY", "ECONOMICALLY",
                             "POLITICALLY", "TECHNOLOGICALLY", "PROACTIVELY",
                             "ANALYTICALLY", "KNOWLEDGEABLY", "SEAMLESSLY",
                             "EFFICIENTLY", "IMMEDIATELY", "ENTIRELY"]

        self.adjectives   = ["SYNERGISTIC", "REASONABLE", "CAREFUL", 
                             "RESPECTFUL", "DIRECT", "ECONOMIC",
                             "POLITICALLY CORRECT", "TECHNOLOGICAL",
                             "PROACTIVE", "ANALYTICAL", "KNOWLEDGEABLE",
                             "SEAMLESS", "BALLPARK", "BUSINESS-TO-BUSINESS",
                             "CUSTOMER-CENTRIC", "INTEGRATED", "COMPETENT",
                             "CREATIVE", "VISIBLE", "HANDY", "PASSIONATE",
                             "UNDERRATED", "INTRIGUING", "FANTASTIC", 
                             "FUNCTIONAL", "WISE", "CRITICAL", "IMPRESSIVE",
                             "SATISFYING", "COMPLETE", "APT", "QUALITY", 
                             "HOLISTIC", "GENUINE", "PROFITABLE"]

        self.nouns        = ["SYNERGY", "CAREFULNESS", "RESPECTFULNESS",
                             "DIRECTNESS", "ECONOMY", "POLITICAL CORRECTNESS",
                             "TECHNOLOGY", "PROACTIVENESS", "ANALYSIS", 
                             "KNOWLEDGE", "SEAMLESSNESS", "CUSTOMER-CENTRICITY",
                             "INTEGRATION", "COMPETITIVENESS", "HANDINESS",
                             "PASSION", "CREATIVITY", "COMPETENCE", "VISIBILITY",
                             "BALLPARK FIGURE", "BANDWIDTH", "COMPANY", 
                             "LOW HANGING FRUIT", "ENTITLEMENT", "OUTSOURCING",
                             "COMPLIANCE", "ENTERPRISE"]

        self.verbs        = ["RESPECTS", "PROMOTES", "LIKES", "LISTENS TO", 
                             "COMPLIMENTS", "COMPLEMENTS", "SUPPORTS", "OUTSOURCES",
                             "MIMICS", "PRACTICES", "OBSERVES", "WATCHES", 
                             "APPROVES OF", "HOPES FOR THE CONTINUATION OF",
                             "ENDORSES", "FINANCIALLY SUPPORTS", "PAYS FOR"]
        
    def generate(self, sentences_num):
        self.sentences_num = sentences_num
        self.message = "\n" + choice(self.salutations1) + " " + choice(self.salutations2) + "," + "\n"
        for i in range(sentences_num):
            rnum = randint(1, 6)
            if rnum == 1:
                self.message += "I BELIEVE YOUR " + choice(self.nouns) + " IS " + choice(self.adjectives) + "! "
            elif rnum == 2:
                self.message += "AROUND HERE, YOU ARE THE " + choice(self.nouns) + " THAT " + choice(self.adverbs) + " KEEPS US RUNNING " + choice(self.adverbs) + ". "
            elif rnum == 3:
                self.message += "MY " + choice(self.nouns) + " " + choice(self.verbs) + " YOUR " + choice(self.adverbs) + " " + choice(self.adjectives) + " " + choice(self.nouns)+ ". "
            elif rnum == 4:
                self.message += "CONTINUE YOUR " + choice(self.nouns) + ", PLEASE. "
            elif rnum == 5:
                self.message += "I JUST WANTED TO CONGRATULATE YOU ON " + choice(self.adverbs) + " GAINING THE RANK OF " + choice(self.salutations2) + "! "
            else:
                self.message += "WOULD YOU BE ABLE TO PROVIDE SOME " + choice(self.nouns) + " TO MY " + choice(self.salutations2) + "? "
        self.message += "\n\nYOURS " + choice(self.adverbs) + "," + "\n\n" + "CORPORATE."
        print(self.message)
    
    def tweet(self, app_key, app_secret, token_key, token_secret):
        self.noun1 = choice(self.nouns)
        self.noun2 = choice(self.nouns)
        self.adjective = choice(self.adjectives)
        self.adverb1 = choice(self.adverbs)
        self.adverb2 = choice(self.adverbs)
        self.verb = choice(self.verbs)
        self.salutation2 = choice(self.salutations2)
        self.option1 = "I BELIEVE YOUR " + self.noun1 + " IS " + self.adjective + "!"
        self.option2 = "AROUND HERE, YOU ARE THE " + self.noun1 + " THAT " + self.adverb1 + " KEEPS US RUNNING " + self.adverb2 + "."
        self.option3 = "MY " + self.noun1 + " " + self.verb + " YOUR " + self.adverb1 + " " + self.adjective + " " + self.noun2 + "."
        self.option4 = "WOULD YOU BE ABLE TO PROVIDE SOME " + self.noun1 + " TO MY " + self.salutation2 + "?"
        self.option5 = "I JUST WANTED TO CONGRATULATE YOU ON " + self.adverb1 + " GAINING THE RANK OF " + self.salutation2 + "!"
        self.option6 = "CONTINUE YOUR " + self.noun1 + ", PLEASE."
        twitter = Twython(app_key, app_secret, token_key, token_secret)
        untweeted = True
        while(untweeted):
            rnum = randint(1, 6)
            if rnum == 1 and len(self.option1) <= 140:
                twitter.update_status(status = self.option1)
                print("Tweeting '{}' ...".format(self.option1))
                untweeted = False
            elif rnum == 2 and len(self.option2) <= 140:
                twitter.update_status(status = self.option2)
                print("Tweeting '{}' ...".format(self.option2))
                untweeted = False
            elif rnum == 3 and len(self.option3) <= 140:
                twitter.update_status(status = self.option3)
                print("Tweeting '{}' ...".format(self.option3))
                untweeted = False
            elif rnum == 4 and len(self.option4) <= 140:
                twitter.update_status(status = self.option4)
                print("Tweeting '{}' ...".format(self.option4))
                untweeted = False
            elif rnum == 5 and len(self.option5) <= 140:
                twitter.update_status(status = self.option5)
                print("Tweeting '{}' ...".format(self.option5))
                untweeted = False
            elif rnum == 6 and len(self.option6) <= 140:
                twitter.update_status(status = self.option6)
                print("Tweeting '{}' ...".format(self.option6))
                untweeted = False
        else:
            print("Tweeted!")
    
def main():
    parser = argparse.ArgumentParser(description = "Talk like corporate!")
    parser.add_argument("-g", "--generate", 
                        dest = "sentences_num", 
                        help = "Generate a corporate letter with SENTENCES_NUM sentences.", 
                        metavar = "SENTENCES_NUM", 
                        nargs = "?", 
                        const = 5, 
                        type = int)
    parser.add_argument("-t", "--tweet",
                        dest = "keys_and_secrets",
                        help = "Tweet a single sentence. Use APP_KEY APP_SECRET TOKEN_KEY TOKEN_SECRET for your Twitter app, in that order.",
                        metavar = ("APP_KEY", "APP_SECRET", "TOKEN_KEY", "TOKEN_SECRET"),
                        nargs = 4,
                        type = str)
    args = parser.parse_args()
    if args.sentences_num >= 1:
        letter = Letter()
        letter.generate(args.sentences_num)
    elif len(args.keys_and_secrets) == 4:
        letter = Letter()
        letter.tweet(args.keys_and_secrets[0], 
                     args.keys_and_secrets[1], 
                     args.keys_and_secrets[2], 
                     args.keys_and_secrets[3])
    
if __name__ == "__main__":
    main()