
import random

#set player health
player_health = 200

"""
initial project goals/ideas:

enemy health and dmg randomizer-
so is player dmg but health isnt-
scale with difficulty x
add bosses that can randomly spawn x
say how much dmg/health is done each roundx
"""

def bars():
  print("-0=~~~~~~~~~~~~~~~~~~~~~~~~=0-")

#list of adjs for fight names
adject = ["adorable", "adventurous", "aggressive", "agreeable", "alert", "alive", "amused", "angry", "annoyed", "annoying", "anxious", "arrogant", "ashamed", "attractive", "average", "awful", "bad", "beautiful", "better", "bewildered", "black", "bloody", "blue", "blue-eyed", "blushing", "bored", "brainy", "brave", "breakable", "bright", "busy", "calm", "careful", "cautious", "charming", "cheerful", "clean", "clear", "clever", "cloudy", "clumsy", "colorful", "combative", "comfortable", "concerned", "condemned", "confused", "cooperative", "courageous", "crazy", "creepy", "crowded", "cruel", "curious", "cute", "dangerous", "dark", "dead", "defeated", "defiant", "delightful", "depressed", "determined", "different", "difficult", "disgusted", "distinct", "disturbed", "dizzy", "doubtful", "drab", "dull","eager", "easy", "elated", "elegant", "embarrassed", "enchanting", "encouraging", "energetic", "enthusiastic", "envious", "evil", "excited", "expensive", "exuberant", "fair", "faithful", "famous", "fancy", "fantastic", "fierce", "filthy", "fine", "foolish", "fragile", "frail", "frantic", "friendly", "frightened", "funny", "gentle", "gifted", "glamorous", "gleaming", "glorious", "good", "gorgeous", "graceful", "grieving", "grotesque", "grumpy", "handsome", "happy", "healthy", "helpful", "helpless", "hilarious", "homeless", "homely", "horrible", "hungry", "hurt", "ill", "important", "impossible", "inexpensive", "innocent", "inquisitive", "itchy", "jealous", "jittery", "jolly", "joyous", "kind"]
#names for enemies
names = ["Angel Slayer", "Whitewash", "Cyclone", "Oblique", "Red Saint", "Vex", "Discord", "Inferno", "Safari", "Recluse", "Moors Stalker", "Ditch", "Nashville Psycho", "Optic Nerve", "Blink", "Shivers", "Blackout", "Patch Galactic", "Buttons", "Killer Criminal", "Static", "Rundown", "Limerick", "Drift", "Dust", "Snake", "Mockingbird", "Aberration", "Frenzy", "Whistler", "Voodoo", "Mutilator", "Tempus", "West End Bandit", "Rampage", "Venom", "Genesis", "Bedlam", "Omega", "Crimson", "Felon", "Glitch", "Flux", "Monster of Edbury Hill", "Schism", "Spasm", "Miracle", "Apex", "Checkmate", "Mudlark", "Crypto", "Flatline", "Upgrade", "Trace", "Blue Collar Slayer", "Pitfall", "Imprint", "Whip", "Blitz", "Misfit", "Hex", "Cascade", "Wendigo", "Malice", "Spite", "Blur", "Death Angel", "Night Caller", "The Kingston Executioner", "Brownout Strangler", "Parallax", "Longshot", "Diamondback", "Five States Maniac", "Bloodline", "Atomic", "Burnout", "Tempo", "Lonely Heart", "Austin Body Snatcher", "Patches", "Transonic", "Pied Piper", "Engineer", "Overkill", "Solstice", "Old Lace", "Ethan", "Surge", "Avalanche", "Pyro", "Nocturne", "Mimic", "Grifter", "Guilty Conscience", "Red Cloud", "Sabbath", "Bipolar", "Live Wire", "Rewind", "Crossfire", "Standoff", "Flood", "Wild Onion", "Burn", "Hype", "Red Wolf", "After Party", "Denizen", "Sick Sin", "Cold Cut", "Deuces Wild", "Spike", "Badness", "Slicer", "Plague", "Freeze Dried", "Task Rabbit"]

#picks a random adj
def battleName():
  global a
  global adject
  a = random.choice(adject)

#picks a random name
def battleNamex():
  global n
  global names
  n = random.choice(names)

#Enemy choice (hit or heal)
def choiceEn():
  global choice
  choice = random.randint(1, 2)

#activate at start of fight to determain enemy health
def enemy_heal_rand():
  global enemy_health
  enemy_health = random.randint(80, 300)

#calls before doing dmg to determain how much itll do
def enemy_dmg_rand():
  global enemy_dmg
  enemy_dmg = random.randint(10, 35)

#introduction to the game which can be called to in the start screen
def tut():
  bars()
  print("In each battle you can either hit or heal")
  print("This rule applies to the ai demon you fight too")
  print("If you see XX its cause you hit, if you see [] its cause you chose to heal")
  print("X means the demon hit and {} means they healed")
  print("Everything is randomized from health, enemy name, and how much damage both partys do")
  print("The goal is too live through as many rounds as possible before dying")
  print("Goodluck!")

#player damaging enemy function
def player_hit():
  global enemy_health
  pDmg = random.randint(15, 30)
  enemy_health = enemy_health - pDmg

#called to when a player heals to determain how much health we gain
def player_heal():
  global player_health
  hAmount = random.randint(8, 20)
  player_health = player_health + hAmount

#called when enemy hits
def enemy_hit():
  global player_health
  global enemy_dmg
  enemy_dmg_rand()
  player_health = player_health - enemy_dmg

#called when enemy heals
def enemy_heal():
  global enemy_health
  hAmount = random.randint(20, 40)
  enemy_health = enemy_health + hAmount

#score = how many rounds survived
high_score = 0

#all the endings and resetting of all the stuff
def endingBad():
  global adject
  global player_health
  global high_score
  global a
  battleName()
  print("you died but had a " + a + " life")
  x = input("Type anything to restart: ")
  enemy_heal_rand()
  battleNamex()
  player_health = 200
  high_score = 0
  roundMix()
def endingGood():
  global adject
  global high_score
  global a
  battleName()
  print("Goodjob, you won and had a " + a + " battle, lets go again!")
  x = input("Type anything to restart: ")
  high_score = high_score + 1
  enemy_heal_rand()
  battleNamex()
  roundMix()

#sets enemy health
enemy_heal_rand()

#Makes a name for the enemy
battleNamex()

#main chunk of game for putting everything from before hand together to make the actual game
def roundMix():
  #calling to all the vars in other places
  global player_health
  global choice
  global enemy_health
  global enemy_dmg
  global high_score
  global n
  #main gui
  bars()
  print("Your high score so far is:")
  print(high_score)
  print("Your health is:")
  print(player_health)
  print("The demon " + n + " has a health of:")
  print(enemy_health)
  bars()
  #input
  player_choice = input("Do you want to hit(press 1) or heal(press 2): ")
  bars()
  #player and enemy choices
  if player_choice == "1":
    player_hit()
    print("XX")
  else:
    player_heal()
    print("[]")
  choiceEn()
  if choice == 1:
    enemy_hit()
    print("X")
  else:
    enemy_heal()
    print("{}")
  #after each round if health is less than zero than send the end functions
  if player_health < 0:
    endingBad()
  elif enemy_health < 0:
    endingGood()
  else:
    roundMix()

#Game starting
def gameStart():
  bars()
  print("Welcome to FightFlight")
  print("You play as a knight who kills demons")
  print("Survive for as many rounds as you can!")
  x = input("Press 1 to get game info, press anything else to start the game: ")
  if x == "1":
    tut()
    gameStart()
  else:
    roundMix()
  bars()

gameStart()
