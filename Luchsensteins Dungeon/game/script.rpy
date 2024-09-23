# ---------------------------------
# Willkommen zum Renpy Projekt "Luchsensteins Dungeon"!
# ---------------------------------
# Von Lea Kriegler & Kristina Barufke

# Hier gibt es nur Notizen für den Code speziell, 
# aber in dem beigefügten PDF-Dokument gibt es viele weitere Infos zu dem Projekt allgemein :D
# Vorweg noch: Die Benutzung von Einrückungen allgemein, doch vor allem bei den Labels 
# ist sehr wichtig, um die Übersicht beim Skript zu behalten.

# Notizen für uns: 
# - Code markieren, f1 und dann: Create Manual Folding Range from Selection 
# -> richtig gut um code zusammenzufassen -> wäre schön auch dauerhaft und nicht nur temporär


define config.developer = True

# Das ist eine Variable, welche True ist, wenn die VN zu einem Buch verglichen wird. False, wenn nicht.
default book = False

# Standardangaben (Muss nicht gespeichert werden)
default player_hp = 100
default enemy_hp = 50
default timeT = 0.7
default biteCounter = 0

# Standardangaben (Müssen gespeichert werden)
default player_name = ""
default player_class = ""

# Endings (Müssen gespeichert werden/ Ausprobieren von "persistent.")
default persistent.ending_1 = False
default persistent.ending_2 = False
default persistent.ending_3 = False
default persistent.ending_4 = False
default persistent.ending_5 = False
default persistent.ending_6 = False
default persistent.ending_7 = False
default persistent.ending_8 = False
default persistent.ending_9 = False

# Deklarieren der Charaktere
define l = Character(_("Lux Van Luchsenstein"), color="#cb7315")
define k = Character(_("Kris Kringle"), color="#1293de")
define g = Character(_("Guard"), color="#7e7e8b")
define g2 = Character(_("Other Guard"), color="#7e7e8b")
define g1 = Character(_("Guard [player_name]"), color="#7e7e8b")
define q = Character(_("???"), color="#cb7315")
define r = Character(_("RÄT"), color="#cb2115")
define s2 = Character(_("???"), color="#9c0a00")
define s = Character(_("Severus"), color="#9c0a00")


# Ganzes Statement für Python-Code
init python:
    # Import von Python-Modulen
    import json
    import random

    # Funktion um den Game State in einer JSON file zu speichern
    def save_game():
        game_state = {
            "player_name": player_name,
            "player_class": player_class
        }
        with open("game_state.json", "w") as f:
            json.dump(game_state, f)

    # Funktion zum Laden vom Game State von der JSON file
    def load_game():
        global player_name, player_class
        try:
            with open("game_state.json", "r") as f:
                game_state = json.load(f)
                player_name = game_state["player_name"]
                player_class = game_state["player_class"]
        # Wenn nichts vorhanden ist, wird nichts geladen
        except FileNotFoundError:
            pass

    def reset_persistent_endings():
        persistent.ending_1 = False
        persistent.ending_2 = False
        persistent.ending_3 = False
        persistent.ending_4 = False
        persistent.ending_5 = False
        persistent.ending_6 = False
        persistent.ending_7 = False
        persistent.ending_8 = False
        persistent.ending_9 = False

        # Speichern von persistent.
        renpy.save_persistent()

    # Funktion um den Game State zu reseten (eher zum testen)
    def reset_game():
        global player_name, player_class
        player_name = ""
        player_class = ""
        save_game()
        reset_persistent_endings()

# Alle Bilder:
# Anmerkung: Ich würde das gerne dauerhaft, auch nach Schließen des Skripts) als Einrückung festlegen, 
# habe aber keine Ahnung wie das funktioniert und das Internet hilft nicht :(

#Backgrounds
image Eiswuste: 
    "1 eiswuste.jpg"
    zoom 4.5

image Eiswuste2: 
    "1 eiswuste2.jpg"
    zoom 4.2

image Prison_Outside:
    "1 prison outside.jpg"
    zoom 1

image Prison_Entrance:
    "1 eingang.jpg"
    zoom 3.2

image Gang_zur_zelle:
    "1 gang zur zelle.jpeg"
    zoom 2.2
    ypos 1.5

image vor_der_zelle:
    "1 vor der zelle.jpeg"
    zoom 1.9

image Cell:
    "1 zelle 1.jpeg"
    zoom 2.0 
    ypos -0.5

image Ending_Cell:
    "1 abschlusszelle.jpg"
    zoom 3.8
    ypos 1.1

image Krux:
    "Krux.jpg"

# Endings
image Aretheyflirting:
    "ending areTheyFlirting.png"
    zoom 1.3

image ending death:
    "ending death.png"
    zoom 1.2

image ending nothing:
    "ending nothing.png"
    zoom 1.2

image ending nothing:
    "ending nothing.png"
    zoom 1.2

image ending biteTheBullet:
    "ending biteTheBullet.png"
    zoom 1.2

image ending dieRat:
    "ending dieRat.png"
    zoom 1.2

image ending microwave:
    "ending microwave.png"
    zoom 1.2

image ending notHarmed:
    "ending notHarmed.png"
    zoom 1.2

image ending sadPunchingBag:
    "ending sadPunchingBag.png"
    zoom 1.2

image ending smile:
    "ending smile.png"
    zoom 1.2

image ending topTipps:
    "ending topTipps.png"
    zoom 1.2



# Charaktere
#Kris Kringle:
image Kris Kringle:
    "Kris Kringle.png"
    zoom 0.9

image Kris Kringle closed_mouth:
    "Kris Kringle closed_mouth.png"
    zoom 0.9

image Kris Kringle smile:
    "Kris Kringle smile.png"
    zoom 0.9

image Kris Kringle grin:
    "Kris Kringle grin.png"
    zoom 0.9

image Kris Kringle annoyed:
    "Kris Kringle annoyed.png"
    zoom 0.9

image Kris Kringle angry:
    "Kris Kringle angry.png"
    zoom 0.9

image Kris Kringle shocked:
    "Kris Kringle shocked.png"
    zoom 0.9

image Kris Kringle thinking:
    "Kris Kringle thinking.png"
    zoom 0.9

image Kris Kringle tense:
    "Kris Kringle tense.png"
    zoom 0.9

image Kris Kringle sad:
    "Kris Kringle sad.png"
    zoom 0.9

image Kris Kringle very sad:
    "Kris Kringle very sad.png"
    zoom 0.9

#Lux:
image Lux:
    "Lux.png"
    zoom 0.9

image Lux normal_grin:
    "Lux normal_grin.png"
    zoom 0.9

image Lux squint:
    "Lux squint.png"
    zoom 0.9

image Lux squint_grin:
    "Lux squint_grin.png"
    zoom 0.9

image Lux closed_eyes:
    "Lux closed_eyes.png"
    zoom 0.9

image Lux annoyed:
    "Lux annoyed.png"
    zoom 0.9

image Lux angry:
    "Lux angry.png"
    zoom 0.9

#Guard:
image Guard:
    "Guard.png"
    zoom 2.2
    xzoom -1.0

image Guard serious:
    "Guard serious.png"
    zoom 2.2
    xzoom -1.0

image Guard happy:
    "Guard happy.png"
    zoom 2.2
    xzoom -1.0

image Guard sad:
    "Guard sad.png"
    zoom 2.2
    xzoom -1.0

#Severus:

image Severus:
    "Seelenbutler.png"
    zoom 0.9

image Severus annoyed:
    "Seelenbutler annoyed.png"
    zoom 0.9

image Severus left:
    "Seelenbutler links.png"
    zoom 0.9

image Severus left_annoyed:
    "Seelenbutler links_annoyed.png"
    zoom 0.9

image Severus dark:
    "Seelenbutler dark.png"
    zoom 0.9


#Andere Charakter/Objekte:
image Ki Kringle:
    "Ki Kringle.png"
    zoom 0.9
    xpos 0.6 
    ypos 1.7

image Rat:
    "rat.png"
    xzoom -1.0

image Baseball:
    "baseball.png"

image Microwave:
    "microwave.png"

# </Alle Bilder Ende>


# <Tests mit Transform (Ist aber eher unpraktisch, musste ich feststellen)>
transform move_left_to_right:
    xalign 0.0  # Start on the left side
    linear 0.2 xalign 1.3  # Move to the right side over 3 seconds

transform move_left_to_right_short:
    xalign 2.1  
    linear 0.2 xalign 2.5  
# </Tests mit Transform>


# ----------------------------------------------------------------------------



# Hier beginnt das Spiel
label start:
    # New Game ist nur hier für Testzwecke und wird erst ganz am Ende ausgeklammert, wenn das 
    # Projekt veröffentlichweise komplett fertig ist (mit anderen GUI und Hintergründen).

    # Es sollte immer Spiel Laden ausgewählt werden
    menu:
        "Neues Spiel":
            $ reset_game()
            jump new_game
        "Spiel laden":
            $ load_game()
            jump start_gamescene

label new_game:
    # Charaktererstellung
    scene black
    "Create your Character!"
    $ player_name = renpy.input("What's your name?")
    # Keine Beschränkung etwas Falsches einzugeben, da es sowieso nicht wirklich relevant ist
    $ player_class = renpy.input("Which class are you? (Warrior, Magician, Thief, Fairy)")
    $ save_game()
    "Welcome, [player_name], the [player_class]!"
    "It's time to go on a grand journey!"
    "Are you ready to dive into your new adventure?"
    menu:

        "Are you ready to dive into your new adventure?"

        "Yes.":
            jump main_game

        "Absolutely!":
            jump main_game

label main_game:
    "Wonderful! Then let's start!"
    "..."
    "...right?"
    "Haha."
    "You didn't think you would have a choice, did you?"
    pause 3
    "This journey isn't about you."
    "It's your decision however, where it will end."
    "Not his."
    "Choose wisely, [player_name]."
    
    jump start_gamescene

label start_gamescene:
    # Hier beginnt das Spiel, wenn man Spiel laden drückt.
    # Test mit Musik:
    # play music "Dynamite Dash - Donkey Kong Country Tropical Freeze [OST].mp3"

    # Anzeige von dem ersten Hintergrundbild. Scene macht alles andere weg.
    scene Eiswuste
    with fade
    "It's been quite a while since we left the city."
    "Where the hell are we going?"
    
    # Erste Anzeige von Charakter Kris Kringle mit Koordinaten und Animationsbewegung
    # Die meisten Animationen sind sehr konkret und deshalb ist sie meistens gleich dabei
    show Kris Kringle with dissolve:
        xpos -0.5
        ease 3.0 xpos 0.1 ypos 0.0    

    "Even with Ki I've never gone close to where I am right now."

    # Die verschiedenen Gesichtsausdrücke kamen zu verschiedenen Zeitpunkten in das Projekt
    # Deswegen ist die Bennenung auch etwas untaktisch. Eigentlich wird in Renpy der Name des Charakters 
    # genommen und dann dahinter die Kennzeichnung der Expression. Beide getrennt durch ein Leerzeichen.
    # Bei Kris Kringle aber nicht der Fall... Später bei Lux und den Guard passt es aber wieder.
    # Bennenungsfehler und Schwierigkeiten werden sich aber noch öfter zeigen.
    show Kris Kringle closed_mouth

    "Luckily the Aliens aren't bothering us."
    "If we meet one of the stronger ones out here, we're toast."    

    show Kris Kringle annoyed

    "Does that buffoon even know what he's doing?!"

    show Kris Kringle closed_mouth

    show Guard behind Kris:
        xpos  -1.0
        ease 2 xpos -0.2 ypos 0.0

    pause 2

    g "Hey! Keep on moving, criminal!"

    show Guard behind Kris:
        ease 0.2 xpos -0.1 ypos 0.0

    pause 0.2

    show Kris Kringle:
        ease 0.05 xpos 0.18 ypos 0.0 

    pause 0.05

    show Kris Kringle annoyed

    "Agh!"

    "Those damn guards never let me out of their view."

    show Kris Kringle closed_mouth

    "With them watching, flight might not be the best idea."


    q "Uuuughh..."

    show Kris Kringle annoyed

    show Lux behind Kris, Guard:
        xpos  -0.5
        ease 4 xpos 0.58 ypos 0.0

    q "It just takes sooooooo long to get to your beloved new home~? Don't you think?"

    show Lux squint_grin

    q "I'm so glad your freedom will be over soon, so I can finally watch you rott in your personal ice hell forever."

    

    show Kris Kringle closed_mouth

    "I swear when I get my hands around that fucker who put me in this mess!"
    
    show Kris Kringle annoyed

    "I'll personally throw him in an arena with this overblown bag of sass and all his little underlings..."

    show Kris Kringle closed_mouth

    k "..."

    show Lux closed_eyes

    q "What? No snarky comment this time? Naw~"
    show Lux squint_grin

    q "You lost all that power, while protecting that Sheep in Wolf's clothing sibling of yours?"

    show Kris Kringle angry:
        ease 0.05 xpos 0.22 ypos 0.0

    k "...!"

    show Lux annoyed

    q "Don't you dare think I didn't do my research properly!"

    show Lux squint

    q "With a little bit of money and charm you can achieve everything~!"

    show Kris Kringle annoyed

    q "Though I must say! You were quite an enemy~! Of course no one can beat Lux Van Luchsenstein the Great!"

    l "Never had such fun locking away someone in a looong time~!"

    show Lux normal_grin:
        ease 3 xpos 0.32 ypos 0.0

    l "How unfortunate for you..."

    show Lux squint_grin
            

    pause 2


    menu:

        "As soon as he comes closer, I'll..."

        "bite him in his ankle.":
            jump biteankle

        "fall to the ground and pretend like I'm dying (Big Brain Move!).":
            jump fallground
     
label biteankle:
    $ biteCounter += 1
    hide Kris Kringle
    with dissolve

    show Kris Kringle:
        xpos  0.4
        ease 0.1 xpos 0.5 ypos 0.2
        pause 0.2

        ease 0.8 xpos 0.4 ypos 0.0
    show Lux angry

    show Kris Kringle grin

    show Lux angry at move_left_to_right_short

    l "You MENACE!!!"

    show Lux annoyed

    l "I've done nothing, but make your arrival the most welcoming of them all!"

    l "Take him away! AT ONCE!"
    
    jump continuation

label fallground:

    hide Kris with dissolve

    show Lux annoyed

    l "What are you doing?"

    show Lux normal_grin

    l "You really think waltzing in the mud and crying like a little baby will get you anywhere? Pathetic."

    show Lux annoyed

    l "And here I am thinking you were smart. What a waste of my time."

    l "Get up and move. Don't keep me waiting."

    show Kris Kringle with dissolve:
        xpos 0.22

    jump continuation

label continuation:

    show Kris Kringle:
        ease 3.5 xpos 3.0 ypos 0.0

    show Guard:
        ease 4 xpos 3.0 ypos 0.0

    show Lux squint

    l "UGH- I can't wait for him to land in that cold, dark cell...!"

    show Lux squint:
        ease 3 xpos 3.0 ypos 0.0
    
    pause 3


    scene Prison_Outside
    with fade

    "Is that it? Wow... that thing is huge."

    "No wonder I was turned over to Lux."

    l "Naw... I'm glad that you like it already~! Want to take a peek inside?"
    l "I'm sure you'll enjoy it just the same! Hahahahaha~!"
    l "Now quit staring at your wonderful residence and swing your butt up the mountain!"

    "I wish Ki could hit me in my face with the metal pipe. Really hard." 

    scene Prison_Entrance
    with fade

    show Kris Kringle:
        xpos -0.5
        ease 3.0 xpos 0.2 ypos 0.0

    "Those freezing temperatures are slowly getting to me."

    show Kris Kringle closed_mouth

    "Even though the guards give me something to warm me up every now and then, they are specifically keeping me on edge."
    
    show Kris Kringle tense

    "Holy shit... Am I really... in danger now?"

    show Kris Kringle closed_mouth

    "There's always been some kind of exit through the backdoor."

    show Kris Kringle angry

    "This can't be it! I refuse!"

    show Kris Kringle:
        ease 1.0 xpos -0.1 ypos 0.0

    menu:

        g "Don't fall back, criminal! Keep up!"

        "Don't resist. Dying here won't get you anything.":
            jump dontResist

        "Try to break free and run for your life.":
            jump breakFree

label breakFree:

    show Kris Kringle grin
    "It's now or never! Last chance!"

    "Or what father would've said: ...No Risk, No Fun!"

    show Kris Kringle:
        ease 0.3 xpos 1.5 ypos 0.0

    k "OUT OF THE WAY, BITCHEEEEEEEEEES!!!" with vpunch

    l "What the fuck?! Don't just stand there, you idiots!! GET HIM!"

    show Guard serious:
        xpos  -1.0
        ease 0.5 xpos 1.5 ypos 0.0

    pause 0.5

    show Guard serious:
        xpos  -1.0
        ease 0.3 xpos 1.5 ypos 0.0

    pause 0.3

    show Guard serious:
        xpos  -1.0
        ease 0.7 xpos 1.5 ypos 0.0

    show Lux annoyed:
        xpos -1.0
        ease 0.8 xpos 0.2 ypos 0.0

    l "This is unacceptable! No one gets away from their looming fate!"

    show Lux annoyed:
        ease 0.8 xpos 1.4 ypos 0.0

    pause 0.8 


    scene black
    pause 3.0
    k "YOU CAN'T CATCH ME! SONIC SPEED!"

    k "HAHAHAHA!"

    pause 2

    k "Ugh..."

    pause 1

    k "Huff... huff...!"
    pause 2

    k "Did I lose them?"

    k "I hope so."

    scene Eiswuste
    with fade

    show Kris Kringle:
        xpos 1.5
        ease 2.0 xpos 0.2 ypos 0.0

    k "huff... h-huff... h-hahh-..."

    show Kris Kringle grin

    "Finally, I lost them... "

    show Kris Kringle shocked

    "Shit...!"

    "It's so cold, I can't feel my hands anymore!"

    show Kris Kringle angry

    "I need to keep moving. I can't stop."

    show Kris Kringle tense

    "If I don't get to civilization soon... I might not get out of this one."

    show Kris Kringle angry

    "Fuck! Just don't think about it! GO!"

    show Kris Kringle angry:
        ease 2.0 xpos -1.0 ypos 0.0
    
    pause 1.5

    scene Eiswuste2 with fade

    show Kris Kringle angry:
        xpos 1.0
        ease 10.0 xpos 0.3 ypos 0.0

    pause 3.0

    k "U-u-uagh... h-h-h-h-huff... h-h-hhahh-..."

    show Kris Kringle shocked:
        ease 4.0 xpos 0.27 ypos 0.5
        
    pause 2.0

    hide Kris Kringle shocked with dissolve

    pause 1.0

    k "F-F-F-Fuck...!"

    "Grrr!! My legs!!!"

    "Nononono! No!"

    "I can't die here!!"

    "I have to get up!!!"

    "Everything feels so numb..."

    "I need rest..."

    g "Over there! He's here!"

    "Is that-?"

    "He found me that quickly?!"

    "Aagh!!! I need to get up again!"

    show Kris Kringle angry with dissolve:
        xpos 0.27 ypos 0.9
        ease 4.0 xpos 0.27 ypos 0.4
        pause 4.0

    "Lux won't get me this time!"

    show Kris Kringle shocked

    "Ugh-!" with hpunch

    show Kris Kringle shocked:
        ease 1.0 xpos 0.27 ypos 0.6

    pause 0.5

    hide Kris Kringle with dissolve

    "It's useless... I can't... anymore."

    "Maybe, I should be glad…"

    show Lux:
        xpos 1.0
        ease 3.0 xpos 0.3 ypos 0.0


    "Without him finding me I would be an ice block by tomorrow."
    show Lux squint
    "As much as I hate being vulnerable in front of my enemy, at least he's the reason I don't freeze to death."
    "…"
    "…right?"

    show Guard serious behind Lux:
        xpos 1.0
        ease 3.0 xpos -0.1 ypos 0.0

    "…"
    "…Why isn't he doing anything."
    show Lux closed_eyes
    "Isn't he supposed to keep me locked up, not dying in the middle of nowhere."
    show Guard happy
    "Come on help me already!"
    "…"
    hide Guard
    show Eiswuste2:
        ypos 1.8
        zoom 2.2

    show Lux squint:
        ypos -0.23
        xpos -0.17
        zoom 3
    "He won't do anything."
    "He's just watching."
    "I'm doomed."
    "Oh no no no."
    "SO absolutely fucked."
    "What's worse? Dying from freezing in the middle of nowhere. Or Lux watching the whole thing."

    show Lux squint:
        ease 0.5 xpos -0.17 ypos -0.1
    show Lux closed_eyes with dissolve

    l "Tag your it~! Got you!"

    show Lux squint:
        ease 0.5 xpos -0.17 ypos -0.23

    l "Now move along, play time outside is over. It's time to return to the kindergarden~!"

    show Lux annoyed

    k "C-C-Can't… …m-m-m-m-move…"

    show Lux squint_grin

    l "… Ahahaha!"

    show Lux normal_grin

    l "A little fish stranded on the shore. All alone. Without any water in sight fighting for pure survival."

    l "But a fish already too weak won't get in the water by itself again."
    show Lux squint_grin
    l "Without any help, you'll not make it out alive, poor little fish."

    show Lux closed_eyes
    l "I dearly hope for you, that you learned something from this."
    show Lux annoyed
    l "You're a cold fellow, alright."
    show Lux squint_grin
    l "But the ice here… is colder."
    show Lux normal_grin

    scene Eiswuste2 with fade
    show Lux normal_grin:
        xpos 0.3 ypos 0.0
    show Guard behind Lux:
        xpos -0.1 ypos 0.0
    l "Ahahahaha!"

    show Lux
    
    l "Hmm... It's a shame... Well. The choice is yours. Should I let you live after everything you did?"

    menu:

        "F-FUCK Y-Y-YOU!!! (Insult)":
            jump death

        "...J-J-Just l-l-let m-me d-d-die i-in p-p-peace... (Give up)":
            jump dontFreezeToDeath

        "(Say nothing)":
            jump death

    return

label death:
    # Hier wird das erste Ending erreicht und deswegen auf True gesetzt.
    $ persistent.ending_1 = True

    show Lux
    l "So this is your choice, yes?"
    show Lux angry
    l "Well you picked the wrong attitude, Kris Kringle."
    show Lux annoyed
    
    l "I'm not amused by your behavior."

    l "You want to die alone in the cold?"

    show Lux squint_grin

    l "Ah yes, everything for your beloved freedom~."

    show Lux angry

    l "So YOU, oh you egoistic piece of trash don't have to accept that I won."

    show Lux squint

    l "That I am simply supreme. Your one and only lord!"

    show Lux angry

    l "YOU! ...can do NOTHING."

    l "Nothing at all."

    show Lux squint_grin
    l "Now do me a favor and wish my father a good nice rest in hell, will you~?"
    show Lux annoyed
    show Guard sad
    k "H-H-H-Hhh! N-No...!"

    show Lux squint_grin

    l "Get iced, Kris Kringle."

    scene black with fade

    pause 1.0

    k "N-N-NO! D-Don't... h-huff... l-l-l-leave... h-h-hah... m-m-me..."

    pause 1.0

    k "D-D-D-Don't-... ...hah..."

    pause 3.0

    scene black with fade
    show ending death with fade
    

    pause

    return
# Ending 1

label dontFreezeToDeath:
    show Lux closed_eyes
    l "Oh~"
    l "Well…"
    show Lux normal_grin
    l "You know…"
    l "It would be a shame to just let you rot here, if that‘s what you want."
    show Lux squint_grin
    l "Suffering in a wonderful enclosure would be of much much greater pleasure."
    l "For me,"
    show Lux closed_eyes
    l "of course~"
    "Hngh… I can‘t… Keep my eyes open anymore…"
    "It‘s… all too much…"
    show Lux normal_grin
    show Guard happy
    l "Good night, Kris Kringle~"
    show Lux squint_grin
    l "We‘ll meet again soon enough."
    scene black with fade
    "U-Ugh… no…!"
    "…!"
    jump unconcious

label dontResist:
    show Kris Kringle closed_mouth:
        ease 1.0 xpos 0.2 ypos 0.0

    "I can't die like this..."

    show Kris Kringle

    k "... Yeah, yeah, whatever."

    show Kris Kringle closed_mouth

    "This is it... When I step one foot inside this monstrosity, it's going to be hard to make my escape."

    show Kris Kringle annoyed

    "There are just too many guards to knock out! I can't take them on all at once!"

    show Kris Kringle closed_mouth

    "I'm sure there must be another way out."

    show Kris Kringle smile

    "Lux will make mistakes. And I'm going to use them for my undeniable escape!"

    show Kris Kringle smile:
        ease 3.0 xpos 1.0 ypos 0.0

    pause 1

    show Guard happy:
        xpos  -1.0
        ease 3.0 xpos 1.0 ypos 0.0

    pause 3

    scene Gang_zur_zelle
    with fade

    show Lux:
        xpos -1.0
        ease 3.0 xpos 0.5 ypos 0.0

    l "Ahahaha! And~? How does it feel to finally arrive where you belong?"

    show Kris Kringle:
        xpos -1.0
        ease 3.0 xpos 0.1 ypos 0.0

    pause 2.0

    show Lux normal_grin

    l "I'm sure you'll be here for a long time~!"

    show Kris Kringle grin

    k "Says the Guy who already spent more time in here than me."

    show Lux annoyed

    l "Don't take your mouth too full, Kris Kringle. We show no mercy here."

    show Kris Kringle annoyed

    k "Do what you want. I'm not afraid of your threats."

    show Lux normal_grin

    l "You will be."
    show Lux squint

    l "Sooner or later everyone breaks here. Don't think you'll survive this one."

    show Lux squint_grin

    l "You won't see the day of light again!" 

    show Kris Kringle

    k "If your prison is so great, why are all of these cells empty?"

    show Kris Kringle closed_mouth
    show Lux

    l "We are not even close to the inner complex. Those Cells are only for other fools who dare to disturb our protégés."
    l "The prisoners brought in here are much more skilled than every hazard from outside these walls."

    show Lux normal_grin

    l "But I'm proud to say! No one has ever escaped this stronghold."

    show Lux squint_grin

    l "And it'll stay this way."

    show Lux

    l "Now move along."

    show Kris Kringle closed_mouth:
        ease 3.0 xpos 1.0 ypos 0.0

    pause 1.0

    show Lux:
        ease 3.0 xpos 1.0 ypos 0.0

    pause 3.0

    scene black
    with fade

    "It's been a while since we got here. We must arrive at the Cell soon."

    "I wonder what Ki is doing..."

    show Ki Kringle with dissolve

    "Maybe if I didn't..."

    "No-. I couldn't do anything differently." 
    "They are fine. Ki can manage the Gang all by herself."

    hide Ki Kringle with fade

    "I miss them."

    scene vor_der_zelle with fade:
        ypos -0.6

    show Kris Kringle:
        xpos -1.0
        ease 3.0 xpos 0.1 ypos 0.0

    k "Are we finally at the Cell? This took ages, old man."

    show Kris Kringle closed_mouth

    show Lux:
        xpos -1.0
        ease 3.0 xpos 0.5 ypos 0.0

    l "The cell?"
    show Lux normal_grin

    l "Ahahaha!"

    show Lux squint

    l "Let's just go in and see, shall we~?"

    scene Cell at Transform(blur=0, alpha=1.0, zoom=0.98, ypos=-0.5)
    with fade


    show Kris Kringle closed_mouth with dissolve:
        xpos 0.0 
        ypos 0.0

    show Lux with dissolve:
        xpos 0.5
        ypos 0.0

    l "Ah there we are! The room where your dreams will come true!"

    show Kris Kringle

    k "Why are you still in here with me? Aren't I like... supposed to suffer or something?"

    show Kris Kringle closed_mouth

    show Lux squint

    l "You didn't think you could just sit this one out, did you?"

    show Kris Kringle annoyed

    k "..."

    show Lux squint_grin

    l "Oh now that's interesting."

    show Lux closed_eyes

    l "Didn't you hear anything about this famous prison and it's techniques to educate the prisoners in them?"

    show Lux squint_grin

    show Kris Kringle closed_mouth

    l "I'm amazed. Well. Let me show you~!"

    show Lux

    l "You're not afraid of loneliness. We already established that. But everyone is afraid of... something."

    show Baseball with dissolve:
        zoom 0.7
        xpos 0.55
        ypos 0.25

    show Lux squint_grin

    l "Do you remember this?"

    show Guard happy behind Kris:
        xpos -0.5
        ease 0.1 xpos -0.1 ypos 0.0

    show Kris Kringle angry:
        ease 0.1 xpos 0.15 ypos 0.0

    k "GIVE THAT BACK, YOU FUCKER!"

    l "Your trusty baseball bat..."

    show Lux normal_grin

    l "I've heard quite a lot about it... Hahaha!"

    hide Baseball with dissolve

    pause 0.5

    show Lux closed_eyes behind Kris:
        ease 2 xpos 0.3 ypos 0.0

    l "Remember this."

    show Lux annoyed

    l "Everything you say and do will be used to punish you. And you made it quite easy for me to gain information about you."
    
    show Lux squint_grin
    
    l "After all only the worst of criminals are contained here."

    menu:

        l "This is getting ridiculous. Start the procedure at once!"

        "I'm innocent! Someone else put the blame on me! (Truth)":
            jump innoccent

        "STINKY ASS BASTARD FOX! (Insult)":
            jump insult

        "(Say nothing)":
            jump nothing


label innoccent:

    show Lux annoyed
    show Guard serious
    l "You seriosly think I believe you? Hahaha! What fool do you take me for?"

    show Lux angry behind Kris:
        ease 2 xpos 0.48 ypos 0.0
    show Kris Kringle tense
    l "You've murdered hundreds of innocent people in that little stunt of yours! You'll not get away with your crimes!"
    show Guard
    show Lux annoyed
    show Kris Kringle annoyed
    l "Even worse! You harmed our most beatiful president there is!"
    
    show Kris Kringle tense
    show Lux angry
    l "For what you have done to THE Queen, Side Character herself, I will never forgive you!"
    show Lux annoyed
    show Kris Kringle angry
    k "You have to listen to me! The real culprit is still out there!"
    show Lux angry
    l "Then why was YOUR baseball bat found there, hm? I've seen the crimescene with my own eyes."
    show Kris Kringle tense
    show Lux annoyed
    l "Was not a magnificent thing to see. I can say that much."
    show Kris Kringle angry
    k "Someone stole it, duh?! I didn't do shit."
    show Kris Kringle closed_mouth
    show Lux closed_eyes
    l "Let me tell you something."
    show Lux squint_grin
    l "Something really... really important."
    show Lux angry
    show Kris Kringle annoyed
    l "I don't give a flying fox if you commited that terrorist attack or not."
    show Lux normal_grin
    l "You may be innocent..."
    show Lux closed_eyes
    l "Yes you might~..."
    show Lux squint
    l "But you're still a criminal aren't you?"
    show Lux squint_grin
    show Kris Kringle tense
    k "..."
    show Lux closed_eyes
    l "Soooo~ it doesn't matter if you did it~! At the end of the day you still belong here~!"
    show Lux angry
    l "And NOTHING is going to change that."
    show Lux annoyed
    l "Or was sneaking into the government of Terram Solis and flirting with the president to manipulate her something you also want to deny."
    show Kris Kringle angry
    k "...!"
    show Lux squint_grin
    l "That's what I thought."

    menu:

        "(Bite him like the menace I am)":
            jump innocentBite

        "(Just Apologize)":
            jump innocentApologize

label innocentBite:
    $ biteCounter += 1
    
    hide Kris Kringle
    with dissolve

    show Kris Kringle angry:
        xpos  0.32
        ease 0.2 xpos 0.4 ypos 0.3
        pause 0.2
        ease 1 xpos 0.38 ypos 0.25

    show Lux angry
    l "OUCH!!!"

    l "WHAT IN TARNATION DO YOU THINK YOU'RE DOING??"
    l "Let go off me this instantly or you WILL regret it."

    menu:

        "(Bite him harder like the absolute menace I am)":
            jump innocentBiteHarder

        "(Let go)":
            jump innocentBiteLetGo  


label innocentBiteHarder:
    $ biteCounter += 1

    show Kris Kringle angry:
        ease 0.2 xpos 0.4 ypos 0.3
    pause 0.2

    show Kris Kringle angry:
        ease 0.4 xpos 0.38 ypos 0.25
    show Lux angry:
        ease 0.1 xpos 0.47 ypos 0.03
    pause 0.2
    show Lux angry:
        ease 0.2 xpos 0.52 ypos 0.0 
    l "THIS IS ENOUGH!!!"
    show Lux angry:
        ease 0.3 xpos 0.6 ypos 0.0
    show Kris Kringle grin:
        ease 0.
    l "YOU FOOL!!!" 
    
    # Höchstanzahl hier kann 3 sein
    if biteCounter > 2:
        jump innocentBiteKill

    jump innocentBiteLetGo 

label innocentBiteKill:
    $ persistent.ending_2 = True
    l "You've reached your limit."
    show Kris Kringle angry
    l "That's it for you, Kris Kringle."
    scene black
    l "Kill him this instantly."
    pause 3.0
    scene black with fade
    show ending biteTheBullet with fade
    pause
    return
#Ending 2

label innocentBiteLetGo:
    show Lux annoyed
    show Kris Kringle angry
    l "Guards!!!"
    l "Pin him down immediately!"
    l "This one time I'll have mercy with you."
    show Lux closed_eyes
    l "But now."
    show Lux annoyed
    l "This little show is over."
    scene black with fade
    l "For now."
    "Ughh..."
    "What are they doing?!"
    "Everything is turning black..."
    "I can't keep my eyes open anymore..."
    jump unconcious

label innocentApologize:
    show Kris Kringle tense
    k "I-..."
    show Lux
    show Kris Kringle
    k "I'm sorry. I didn't mean to hurt Side."
    show Kris Kringle thinking
    k "Queen Character, I mean."

    if biteCounter > 0:
        show Lux squint
        l "..."
        show Lux angry
        show Kris Kringle annoyed
        l "After rudely biting me you expect me to have mercy?"
        show Lux annoyed
        l "I don't care."
        l "Didn't I mention this before?"
        show Kris Kringle angry
        show Lux angry
        l "Go and have fun in your own littered sea of lies."
        jump innocentBiteLetGo

    $ persistent.ending_3 = True
    show Lux annoyed
    l "You're serious?"
    show Kris Kringle
    k "Yeah."
    show Kris Kringle angry
    k "It's the truth. Do with it whatever you want."
    show Kris Kringle tense
    show Lux
    pause 2
    show Kris Kringle closed_mouth
    "It looks like he believes me."
    show Kris Kringle smile
    "Never thought he would."
    l "Hm..."
    show Lux annoyed
    l "Well."
    show Lux squint
    l "If that's it. You can go to your cell now. I do want to award your honestness."
    show Lux closed_eyes
    l "I myself am an honest man and I respect that of others."
    show Kris Kringle closed_mouth
    show Lux normal_grin
    l "Guards!"
    show Lux
    l "Ensure he makes it to his cell safe and sound."

    pause 3.0
    scene black with fade
    show ending notHarmed with fade
    pause
    return
#Ending 3

label insult: 

    show Kris Kringle grin
        
    show Lux angry

    l "Did you just call me... a FOX?!"

    l "HOW DARE YOU!"

    show Lux annoyed

    l "How could you say such a thing?! I'm a lynx, fool! Not a peasant fox!"

    show Lux angry behind Kris:
        ease 0.05 xpos 0.27 ypos 0.0

    pause 0.03

    show Kris Kringle angry:
        ease 0.05 xpos 0.09 ypos 0.0

    show Guard serious:
        ease 0.05 xpos -0.09 ypos 0.0

    pause 0.05

    "Ouch!"

    show Kris Kringle smile

    "He hits like a lady... Not that it didn't hurt."

    show Kris Kringle closed_mouth

    show Lux annoyed behind Kris:
        ease 2 xpos 0.5 ypos 0.0

    l "You'll never take my mercy for granted again!"

    show Lux

    show Kris Kringle grin

    k "My days of not taking you seriously have come to a middle."

    show Lux annoyed

    l "Say that one more time."

    menu:

        "Whatever kind of look you were aiming for, you missed. But fox would be the closest of them all. (Insult him further)":
            jump reallyRude

        "No. HA! (Let him be.)":
            jump letbe

label reallyRude:
    $ persistent.ending_4 = True

    show Lux angry
    pause 2

    show Kris Kringle annoyed
    k "What the...?"

    show Lux squint_grin
    l "..."

    show Microwave:
        zoom 0.55
        ypos 0.31
        xpos 0.44
    with dissolve

    l "Sometimes... I bring out this baby..."

    show Lux closed_eyes

    l "For the... difficult cases~"

    show Kris Kringle shocked

    "That doesn't look too good!"
    show Kris Kringle tense
    k "Hey no hard feelings, right!?"
    show Kris Kringle angry
    "I think I might have overdone it!"
    show Lux angry
    l "You don't know what's good for you, do you?!"
    scene black
    l "Let me stuff this microwave down your filthy throat."
    "Oh oh."

    pause 3.0
    scene black with fade
    show ending microwave with fade
    pause
    return
#Ending 4

label hittingSequence:
    show Lux squint_grin behind Kris:
        ease 0.08 xpos 0.36 ypos 0.0

    show Baseball:
        ease 0.13 xpos 0.41 ypos 0.25

    pause 0.13

    show Lux closed_eyes behind Kris:
        ease 0.1 xpos 0.4 ypos 0.0

    show Baseball:
        ease 0.3 xpos 0.45 ypos 0.25

    show Kris Kringle angry:
            ease 0.1 xpos 0.03 ypos 0.35
            pause 0.07
            ease timeT xpos 0.09 ypos 0.32
    return

label letbe:

    show Lux annoyed

    l "Chain him to the post this instantly. I will hit that unrespectful tone right out of his filthy throat."

    show Kris Kringle:
        ease 0.05 xpos 0.09 ypos 0.03

    pause 0.05

    show Kris Kringle angry:
        ease 0.05 xpos 0.09 ypos 0.01 

    k "Ugh!"

    show Guard happy:
        ease 0.2 xpos -0.07 ypos 0.01

    pause 0.1

    show Kris Kringle angry:
        ease 0.5 xpos 0.09 ypos 0.20

    pause 0.5

    show Kris Kringle angry:
        ease 2 xpos 0.09 ypos 0.32

    pause 1.0

   

    k "Won't you make it a little less tighter, thank you."

    show Kris Kringle annoyed

    show Lux closed_eyes

    l "Perfect... Now it's time to teach you some maners! And punish you for what you did to Side Character!"

    show Baseball with dissolve:
        zoom 0.7
        xzoom -1.0
        xpos 0.55
        ypos 0.25

    show Lux normal_grin

    l "Hahaha! Lets find out how many hits of your own bat you can take!"

    show Lux squint_grin behind Kris:
        ease 2 xpos 0.4 ypos 0.0

    show Baseball:
        ease 2 xpos 0.45 ypos 0.25

    show Kris Kringle annoyed

    "Is he really going to hit me with that?!"

    # Über der hittingSequence, wenn nötig wird timeT ersetzt wegen lustigen nicht-möglichen Zeug von ATL und Renpy
    # Habens als nicht-globale Variable probiert :,)
    # Besser auf jeden Fall als das komplette Segment zu copy-pasten im Code
    $ timeT = 0.7
    call hittingSequence

    k "AAGH!!" with vpunch

    $ timeT = 1.5
    call hittingSequence

    k "GAAH!!!" with vpunch
    $ timeT = 2.0
    call hittingSequence

    k "GRAGH!!! Stop this madness!" with vpunch

    show Kris Kringle annoyed
    
    show Lux normal_grin

    l "What madness? You've earned this all by yourself~!"

    show Kris Kringle angry:
        ease 0.07 xpos 0.09 ypos 0.29
        pause 0.07
        ease 0.1 xpos 0.09 ypos 0.32
    

    k "You just beat up the prisoners until they break down?! No wonder you-"

    $ timeT = 0.7
    call hittingSequence

    k "AGGHHH...!! huff huff..." with vpunch

    show Lux annoyed

    l "No. Only you get the extra treatment for being the nasty rebell you are."

    l "This case is... personal."

    show Kris Kringle annoyed

    show Lux

    l "It's just as you said. Threats don't mean anything to you. But maybe actions do."

    $ timeT = 1.0
    call hittingSequence

    k "UGHH... huff... huff... what do you..." with vpunch

    show Lux squint

    show Kris Kringle angry:
        ease 0.07 xpos 0.09 ypos 0.29
        pause 0.07
        ease 0.1 xpos 0.09 ypos 0.32

    k "What do you want out of this?! By constantly hitting me you won't get ANYTH-"

    $ timeT = 2.0
    call hittingSequence

    k "AAaaarghh... ugh... huff..." with vpunch

    l "Less talking. More screaming."

    show Kris Kringle annoyed
    show Lux normal_grin

    l "That is if you hold your life dear. Or there won't be a life to live left until I'm done with you."

    menu:
        "Your life seems pretty miserable for a peasant. (Start insulting again)":
            hide Baseball with dissolve
            jump reallyRude

        "(Grin at him. Seductively?)":
            jump grinSeductively

        "(Give in to the pain. There is nothing you can do anyways)":
            jump giveIn

label grinSeductively:
    $ persistent.ending_5 = True

    scene Krux with fade:
        zoom 1.2
        ypos -0.15

    k "HAH! huff... you'll never get me to give up!"

    l "Now... now... you are practically asking me for another swing?"

    l "Don't worry I'm almost 50 percent sure to keep you in one piece."

    l "So come on. Know your place in front of your everlasting monarch, you blood hungry thief."

    l "Suffocate on your own blood, dog."

    k "Only if you watch me, you fucker."

    l "Tsk Tsk! Sooner or later you WILL fall to your knees and submit to my wishes, wild wolf."

    l "Although the deepest pit of hell will not be compareable to how fully and completly I will drag you apart, it's still an adequate try of comparison."

    l "So just a quick reminder..."
    l "Don't you EVER talk shit about me, understand?"


    k "UGHhh...!" with vpunch

    l "I'm the one who keeps you alive."
    l "Be grateful."

    "What did I get myself into?!"

    scene Aretheyflirting with fade

    pause

    return
#Ending 5
label giveIn:

    $ timeT = 0.7
    call hittingSequence
    
    "Grr... It hurts so much..." with vpunch

    show Kris Kringle tense

    "But it's not like I can do anything anyways..."

    show Kris Kringle annoyed

    "I won't take many more hits until I black out cold."

    menu:   
        "Try to bite him! ... ...where it hurts... (Resist)":
            jump biteAgain

        
        "Plead for mercy in hopes to not get beaten to death by a baseball bat. (Give up)":
            jump pleadMercy

label biteAgain:
    $ biteCounter += 1
    hide Kris Kringle
    with dissolve

    show Kris Kringle:
        xpos  0.15 ypos 0.32
        ease 0.1 xpos 0.25 ypos 0.20
        pause 0.2

        ease 0.8 xpos 0.09 ypos 0.32

    show Kris Kringle grin

    show Baseball:
        easein 0.15 ypos 0.07
        pause 0.2
        easeout 0.7 ypos 1.5
        

    show Lux angry at move_left_to_right_short
    pause 1

    show Lux angry:
        ease 0.8 xpos 2.34
    
    l "EW!"

    show Lux annoyed

    if biteCounter > 0:
        l "Didn't we learn from before?"
        show Lux normal_grin
        l "We don't bite where the sun doesn't shine or teeny tiny lil' Kringle will get a muzzle."
        show Kris Kringle closed_mouth
        l "Woowzah!"
        show Lux
        l "..."
        show Lux annoyed
        show Kris Kringle grin
        l "Forget that. I never said anything."
        l "Anyways..."
    
    l "That's it, you dog!"
    show Lux squint
    l "I have endured enough of you! Now bow before me!"

    jump grinSeductively

label pleadMercy:

    show Kris Kringle thinking

    k "... ..."

    show Kris Kringle tense

    k "...Stop... ..."

    l "Giving up already~? Ahaha!"

    show Lux

    l "I'm dissapointed I must say... you looked so tough on our way here."

    show Lux normal_grin

    l "And all I see now is a miserable piece of shit!"

    show Kris Kringle angry

    k "GRRRrrr... you..."

    show Kris Kringle annoyed
    show Lux squint_grin

    l "Oooh and trust me! I didn't even get started..."

    $ timeT = 0.9
    call hittingSequence


    k "Uagh!" with vpunch

    show Lux squint
    show Kris Kringle tense
    l "Aren't you having a fun time? Because I sure do! I'm having a very good time~!"

    show Kris Kringle annoyed

    menu: 
        l "If you truly want me to stop and just lock you away... show it!"
        "(Beg for mercy)":
            jump begMercy

        "(Say nothing)":
            jump sadEnding

label begMercy:
    show Kris Kringle thinking
    k "..."
    show Kris Kringle tense
    k "...Lux..."
    show Lux normal_grin
    show Guard
    l "Yees?"
    show Lux 
    show Kris Kringle
    k "... ...Please..."
    show Lux squint
    l "Go on..."
    show Lux closed_eyes
    l "Don't let me wait too long~!"
    show Lux 
    show Kris Kringle annoyed
    k "...huff..."
    show Lux squint_grin
    l "Wait! Let me help you~!"

    $ timeT = 1.2
    call hittingSequence

    k "AAGH...!" with vpunch

    show Lux squint_grin

    l "Could I help that one brain cell of yours~? Or do you need anoth-"

    show Kris Kringle angry:
        ease 0.1 xpos 0.09 ypos 0.28
        pause 0.07
        ease 0.1 xpos 0.09 ypos 0.32

    k "NO-! ..." with vpunch

    show Lux

    l "Oh so eager, hm?"

    show Kris Kringle tense

    k "...Please don't hit me again... hah..."

    show Lux normal_grin

    l "Now look at that! Such a good boy! Didn't think you'd plead me to stop on your first day..."

    show Lux annoyed
    l "Utterly dissapointing."
    show Lux normal_grin
    l "But at the same time... better for my amusement!"
    show Lux closed_eyes
    l "Can't wait to hear you doing that tomorrow as well."
    show Lux normal_grin
    l "Although you need to be a lot more... hm... what do they say... energetic with your cries."
    show Lux closed_eyes
    l "Or else..."
    show Kris Kringle angry
    l "I might get too bored and swing this beloved baseball bat again~!"

    # lehnt sich runter
    show Lux squint:
        ease 2 xpos 0.3 ypos 0.2
    show Baseball behind Kris:
        ease 2 xpos 0.3 ypos 0.4

    l "Maybe in the gut..."
    l "Or your skull..."
    show Lux closed_eyes
    l "Your arms seem very hitable."

    k "...!"
    show Kris Kringle annoyed
    show Lux behind Kris:
        ease 0.3 xpos 0.4 ypos 0.0

    show Baseball behind Kris:
        ease 0.4 xpos 0.45 ypos 0.25

    l "For now! I've heard enough."
    l "Bring him to his cell at once! He's done for the day."
    show Lux normal_grin
    l "But wait!"
    show Kris Kringle angry
    k "W-What else now?!"
    show Lux closed_eyes
    l "This last hit will send you straight to your destination."
    show Guard happy
    show Kris Kringle shocked
    show Lux squint:
        ease 2 xpos 0.3 ypos 0.2
    show Baseball behind Kris:
        ease 2 xpos 0.3 ypos 0.4
    pause 0.2
    scene black with fade 
    k "AAGH!!!" with vpunch
    l "Sleep tight, Kris Kringle."
    k "Ughhh..."

    jump unconcious

label sadEnding:
    $ persistent.ending_6 = True
    show Kris Kringle thinking
    "I-I... I can't..."
    show Kris Kringle tense
    "I can't keep up..."

    show Kris Kringle sad
    "Everything is falling in front of me."

    "My life crumbling before my very eyes."
    show Kris Kringle tense
    "I've been so close to death a couple of times now."

    "B-But..."
    show Kris Kringle angry
    "Never like this!"
    show Kris Kringle sad
    "Why do I feel so sad out of the sudden..."

    window hide
    # Kringle & Lux wird blurry und Hintergrund auch
    show Cell:
        ease 5 blur 15
    show Kris Kringle sad:
        ease 5 blur 15
    show Baseball:
        ease 5 blur 10
    show Lux:
        ease 5 blur 15
    show Guard happy:
        ease 5 blur 15
    pause 2.0
    
    "Everything starts to get blurry..."
    

    show Cell:
        ease 5 blur 55
    show Kris Kringle tense:
        ease 5 blur 55
    show Baseball:
        ease 5 blur 55
    show Lux:
        ease 5 blur 55
    show Guard happy:
        ease 5 blur 55
    pause 2.0

    call hittingSequence

    k "UUugh..." with vpunch

    "I wonder what MatMat is doing..."

    call hittingSequence

    k "...!" with vpunch

    k "... Huff... ... Huff... ..."

    "I hope she's doing better than me."

    "At least she can be happy with her whore husband. That asshole."
    "He'd be more than happy to see me like this."
    "I bet he was the one planing that terrorist attack..."
    "Who in their right mind would do such a thing?!"
    "Now it's too late anyways..."

    show Cell:
        ease 5 blur 100
    show Kris Kringle tense:
        ease 5 blur 100
    show Baseball:
        ease 5 blur 100
    show Lux:
        ease 5 blur 100
    show Guard happy:
        ease 5 blur 100
    pause 2.0

    call hittingSequence

    k "..." with vpunch

    "I can't keep my eyes open anymore..."

    scene black with fade

    "At the end, everything I worked for was for nothing."

    "I wish I would've spent more time with Ki."

    "But it's too late for that."
    pause 3
    window show
    
    "I'm sorry, sister."

    pause 3.0
    window hide
    scene black with fade
    show ending sadPunchingBag with fade
    pause
    return
#Ending 6

label unconcious:
    pause 4
    scene black with fade
    "Uggh..."
    "Ouch... W-Where..."
    "...am I?"
    scene Ending_Cell
    show black behind Ending_Cell
    show Ending_Cell:
        # Zuerst komplett transparent und blurred
        alpha 0.0
        blur 100
        pause 0.5
        # linear sichtbar machen und blur verringern
        linear 1.0 alpha 1.0
        pause 0.9
        linear 5.0 blur 0 

    
    pause 2
    "Agghh! My head hurts..."
    "..."
    window hide  # Verbirgt den Textbalken
    pause 3
    window show  # Zeigt den Textbalken
    "No one is here...?"
    window hide  
    pause 1
    window show
    "This... looks like the cell?!"
    "How did I end up here?"
    window hide  
    show Kris Kringle angry with dissolve:
        xpos 0.2 ypos 0.9
        ease 4.0 xpos 0.2 ypos 0.0
        pause 5.0
    window show
    
    "..."
    show Kris Kringle tense
    "I'm so hungry..."
    show Kris Kringle closed_mouth
    "It's been so long since I ate something."
    show Kris Kringle thinking
    "Good news is I'm alive."
    window hide
    pause 3.0
    window show
    show Kris Kringle annoyed
    "This sucks."
    show Kris Kringle tense
    "Am I really a prisoner now?"
    show Kris Kringle
    "..."
    pause 2.0
    show Kris Kringle tense
    "Better get comfortable..."
    window hide
    pause 2.0
    show Kris Kringle thinking
    pause 1.0
    show Kris Kringle annoyed
    pause 3
    show Kris Kringle sad
    pause 2.0
    show Kris Kringle angry
    pause 1.5
    show Kris Kringle tense
    pause 2.0
    show Kris Kringle sad
    pause 1.5 
    show Kris Kringle very sad
    pause 1.0
    show Kris Kringle sad
    window show
    "Why does this suddenly get to me?"
    "All the mocking from Lux never broke me down completely, but this?!"
    "Just because I left..."
    "Left my gang..."
    "Left my grounds..."
    "Left-...!"
    show Kris Kringle very sad
    "Left... ...Ki..."
    "Sister... I feel so terrible leaving you with the burden I created..."
    show Kris Kringle angry
    "...that is why I feel so utterly... atrocious."
    show Kris Kringle sad
    "I left her with the gang I created all alone."
    "All these duties..."
    "What if she just collapses under the pressure?!"
    show Kris Kringle very sad
    "It would all be MY fault."
    "...my... ...fault..."

    "..."
    show Kris Kringle shocked
    "What's that?"
    show Kris Kringle
    "Is that-?"
    r "*RAT NOISES*"
    window hide
    show Kris Kringle shocked:
        ease 2.0 xpos 0.0 ypos 0.0
    show Rat:
        xpos 0.6
        ypos 1.0
        ease 2 xpos 0.6 ypos 0.51
    pause 3
    window show
    "What is this RÄT doing here?!"
    show Rat:
        ease 0.2 xpos 0.6 ypos 0.45
        ease 0.1 xpos 0.6 ypos 0.5
    r "*MORE RAT NOISES*"
    show Kris Kringle thinking
    "Natural Habitat, I guess."
    show Kris Kringle
    menu:
        "What should I do with this RÄT?"

        "(Pet the good lil' guy!)":
            jump PetRat1

        "(ATTACK!!!)":
            #Kampf mit der Ratte
            show Kris Kringle angry
            "I'll take it down!"
            call Fight 

        "(Ignore it.)":
            jump IgnoreRat
    
    return

#--------------------------------------------------------------
#Kampf!

label Fight:
    show Rat:
        ease 0.2 xpos 0.6 ypos 0.45
        ease 0.1 xpos 0.6 ypos 0.5    
    "The RÄT looks nervous, but determined."
    show Kris Kringle angry
    "I won't hold back!"
    $ enemy_hp = 50  # Reset enemy & player HP vor Fight
    $ player_hp = 100
    
    while player_hp > 0 and enemy_hp > 0:
        show Kris Kringle annoyed
        # Spieler wählt Aktion
        menu:
            "What should I do?"
            "(Punch)":
                call FightPlayerAttackPunch
            "(Kick)":
                call FightPlayerAttackKick
            "(Do nothing)":
                call FightNothing
            "(Spare)":
                call FightSpare1

        # Falls nach der Aktion RÄT noch lebt, greift RÄT an
        if enemy_hp > 0:
            call FightEnemyTurn
    
    return

# Spieler greift an (Punch)
label FightPlayerAttackPunch:
    show Kris Kringle angry:
        ease 0.2 xpos 0.2 ypos 0.0
        pause 0.2
        ease 0.6 xpos 0.0 ypos 0.0
    $ player_roll = random.randint(1, 20)
    if player_roll > 8:  # Erfolgschance basierend auf Wurf
        $ enemy_hp -= 10
        if enemy_hp < 0:
            $ enemy_hp = 0
        show Kris Kringle grin
        "I threw a solid punch. Take that RÄT! (Monster HP: [enemy_hp])"
    else:
        show Rat:
            ease 0.3 xpos 0.68 ypos 0.5
            pause 0.2
            ease 0.7 xpos 0.6 ypos 0.5
        "I missed! The RÄT dodged my attack with ease..."
    
    # Nach Spielerangriff kommt RÄT dran, außer RÄT ist schon tot
    if enemy_hp <= 0:
        "The RÄT is down! I won!"
        jump FightEnd
    return

# Spieler greift an (Kick)
label FightPlayerAttackKick:
    show Kris Kringle angry:
        ease 0.2 xpos 0.2 ypos 0.0
        pause 0.2
        ease 0.6 xpos 0.0 ypos 0.0
    $ player_roll = random.randint(1, 20)
    if player_roll > 10:  # Kicks haben niedrigere Trefferwahrscheinlichkeit, dafür mehr Schaden
        $ enemy_hp -= 14
        if enemy_hp < 0:
            $ enemy_hp = 0
        show Kris Kringle grin
        "I landed a powerful kick! HAHA L! (Monster HP: [enemy_hp])"
    else:
        show Rat:
            ease 0.3 xpos 0.68 ypos 0.5
            pause 0.2
            ease 0.7 xpos 0.6 ypos 0.5
        "I missed! The RÄT dodged my attack with ease..."
    
    if enemy_hp <= 0:
        "The RÄT is down! I won!"
        jump FightEnd
    return

# Spieler macht nichts
label FightNothing:
    show Kris Kringle
    "Actually. I don't want to do anything."
    show Kris Kringle smile
    "Yep!"
    "Started this fight for absolutely nothing. Great."
    show Kris Kringle angry
    "Thanks, inner conflict."
    return

# Die RÄT greift an
label FightEnemyTurn:
    $ enemy_hit_roll = random.randint(1, 20)
    if enemy_hit_roll > 17: # Relativ unwahrscheinlich, dass RÄT nichts tut
        "The RÄT watches me cautiously, waiting for my next move."
    else:
        show Rat:
            ease 0.4 xpos 0.4 ypos 0.5
            pause 0.2
            ease 0.7 xpos 0.6 ypos 0.5
        $ enemy_roll = random.randint(1, 20)
        if enemy_roll > 8:  # Die RÄT hat dafür hier höhere Wahrscheinlichkeit zu treffen
            $ player_hp -= 10
            if player_hp < 0:
                $ player_hp = 0
            show Kris Kringle angry
            "The RÄT leaps forward and scratches me! (Your HP: [player_hp])"
        else:
            show Kris Kringle angry:
                ease 0.3 xpos -0.1 ypos 0.0
                pause 0.2
                ease 0.8 xpos 0.0 ypos 0.0
            
            "The RÄT lunges at me but misses!"
    
    # Überprüfung, ob der Spieler noch lebt
    if player_hp <= 0:
        $ persistent.ending_7 = True
        scene black with fade
        "How..."
        "Could I lose to a RÄT...?"
        pause 3.0
        window hide
        scene black with fade
        show ending dieRat with fade
        pause
        return
    return
#Ending 7

# Spieler versucht, die RÄT zu verschonen
label FightSpare1:
    show Kris Kringle thinking
    "Maybe... there's no need to finish this."
    show Kris Kringle tense
    "I should lower my fists."
    show Kris Kringle smile
    "The RÄT tilting its head, confused but hopeful? Kinda cute how it does that."
    
    menu:
        "Am I sure I want to spare the RÄT?"
        
        "(Yes, I should spare it.)":
            show Kris Kringle smile
            "I can't do this. You deserve better, little one."
            show Kris Kringle sad
            "The RÄT's eyes sparkle with gratitude..."
            "I'm so glad..."
            show Kris Kringle grin
            "Bye little fella."
            show Kris Kringle smile
            "Run off into the distance! Free!"
            jump unconciousEnd

        "(No, I need to finish the fight!)":
            show Kris Kringle angry
            "No mercy! I'm ending this!"
            jump Fight

# Kampfende, wenn die RÄT besiegt wurde
label FightEnd:
    hide Rat with dissolve
    show Kris Kringle thinking
    "I defeated the RÄT."
    show Kris Kringle tense
    "I killed the lonely, hope seeking, soon-to-become-hero, always-dreaming-about-becoming-a-star-in-the-popular-TV-show-the-Ratchelor, pretty damn chill RÄT."
    "Congrats to me."
    show Kris Kringle sad
    "I won. But at what cost...?"
    "It wasn't just a RÄT. It had hopes. Dreams."
    "I feel its dreams slip away. Slowly."
    show Kris Kringle angry
    "I'm an absolute monster."
    "Shame on me."
    "Shame."
    show Kris Kringle closed_mouth
    "I hope it ends in RÄT heaven."
    show Kris Kringle smile
    "Would appreciate that as well."
    show Kris Kringle thinking
    pause 3
    jump unconciousEnd

#--------------------------------------------------------------


label IgnoreRat:
    show Kris Kringle annoyed
    "Ugh. I'm not interested."
    window hide
    pause 2
    hide Rat with dissolve
    window show
    show Kris Kringle closed_mouth
    "Well. There it goes."
    show Kris Kringle thinking
    "At least it can get out of here..."
    jump unconciousEnd

label PetRat1:
    "Not everything should be solved with violence."
    show Kris Kringle smile
    k "You're so cute!"
    show Kris Kringle grin:
        ease 3 xpos 0.2 ypos 0.1

    k "Now who's a good little RÄT!"
    k "Yes! You are!"
    show Rat:
        ease 0.05 xpos 0.6 ypos 0.45
        pause 0.05
        ease 0.1 xpos 0.6 ypos 0.5
    pause 0.1
    show Kris Kringle smile
    "It seems to enjoy this..."
    show Kris Kringle 
    k "Don't stare at me with those cute puppy eyes. I'm weak."
    menu:
        "What should I do?"
        "(More Pets!)":
            jump PetRat2
        "(Let go.)":
            jump PetLetGo

label PetRat2:
    show Kris Kringle smile
    show Rat:
        ease 0.05 xpos 0.6 ypos 0.45
        pause 0.05
        ease 0.1 xpos 0.6 ypos 0.5
    "Oh you little one!"
    "You like that?"
    menu:
        "(More Pets!!!)":
            jump PetRat3
        "(Let go.)":
            jump PetLetGo

label PetRat3:
    show Kris Kringle grin
    show Rat:
        ease 0.05 xpos 0.6 ypos 0.45
        pause 0.05
        ease 0.1 xpos 0.6 ypos 0.5
    "Awwww this cutie patootie!"
    "How much I love tiny RÄTS!"
    menu:
        "(More Pets!)":
            jump PetRat4
        "(Let go.)":
            jump PetLetGo

label PetRat4:
    show Kris Kringle closed_mouth
    "Okay I think that's enough."
    menu:
        "(More Pets.)":
            jump PetRat5
        "(Let go.)":
            jump PetLetGo

label PetRat5:
    show Kris Kringle annoyed
    "I-I can't stop!"
    menu:
        "(More Pets...)":
            jump PetRat6
        "(Let go.)":
            jump PetLetGo

label PetRat6:
    show Kris Kringle tense
    "What is this insanity?!"
    menu:
        "(More Pets.........)":
            jump PetRat7
        "(Let go.)":
            jump PetLetGo

label PetRat7:
    show Kris Kringle angry
    "PLEASE I NEED TO LET IT GO!"
    menu:
        "(More Pets..............)":
            jump PetRat8
        "(Let go.)":
            jump PetLetGo

label PetRat8:
    "STOOOOOOP!!!"
    menu:
        "(More Pets......................)":
            jump PetRatDied
        "(Let go.)":
            jump PetLetGo

label PetRatDied:
    window hide
    show Kris Kringle shocked
    pause 3
    hide Rat with dissolve
    show Kris Kringle sad
    pause 4
    window show
    "I..."
    show Kris Kringle very sad
    "I petted it to death."
    show Kris Kringle sad
    "What have I done..."
    show Kris Kringle tense
    "I will never talk about this ever again."
    window hide
    show Kris Kringle:
        ease 4 xpos 0.0 ypos 0.0
    pause 4
    window show
    jump unconciousEnd


label PetLetGo:
    show Kris Kringle smile
    k "Now off you go!"
    k "Be free!"
    show Kris Kringle tense
    k "Not like me..."
    show Rat:
        ease 0.05 xpos 0.6 ypos 0.45
        pause 0.05
        ease 0.1 xpos 0.6 ypos 0.5
    pause 0.1
    hide Rat with dissolve
    show Kris Kringle smile
    "Chase your dreams."
    "Bye bye, little one..."
    show Kris Kringle:
        ease 4 xpos 0.0 ypos 0.0
    pause 5
    jump unconciousEnd

label unconciousEnd:
    show Kris Kringle tense
    "Hopefully I can get out of here soon."
    show Kris Kringle angry
    "I just have to!"

    if persistent.ending_1 and persistent.ending_2 and persistent.ending_3 and persistent.ending_4 and persistent.ending_5 and persistent.ending_6 and persistent.ending_7 and persistent.ending_8 and persistent.ending_9:
        jump special_ending
    # Special event mit Severus beim playthrough von allen endings

    $ persistent.ending_8 = True
    pause 3.0
    window hide
    scene black with fade
    show ending topTipps with fade
    pause
    return
#Ending 8

label special_ending:
    show Kris Kringle shocked
    "...!"
    show Kris Kringle angry
    "Voices are coming closer!"
    l "If you are truly able to do it, then consider it a deal."
    show Kris Kringle annoyed
    "There's Lux!"
    show Kris Kringle thinking
    "...And?"
    show Kris Kringle
    "Another voice...?"
    l "I don't need the extra money you're paying, but I'll gladly take your lavish offer."
    l "He's all yours."
    show Kris Kringle annoyed
    l "Do your worst."
    show Kris Kringle angry
    "From what I'm hearing that doesn't sound too good."
    show Kris Kringle annoyed
    "...!"
    "Someone's coming!"
    show Severus left:
        xpos 0.52 ypos -0.05
    with dissolve
    s2 "Ah~"
    s2 "Just as Lux said. Well and every limb attached. Wonderful."
    show Kris Kringle tense
    "Who is this...?!"
    s2 "It's a pleasure to finally be meeting you, Kris Kringle~!"
    s2 "I've heard quite a lot about you and your... friends."
    show Kris Kringle
    "No wait."
    show Kris Kringle shocked
    "I know this guy!"
    show Kris Kringle angry
    "This is Severus! One of the elite members of the Körperschaft!"
    show Kris Kringle annoyed
    "What is he doing here?!"

    s "You must die to know why I am here today, right?"
    show Severus left_annoyed
    s "Let me say this."
    show Kris Kringle
    show Severus left
    s "You are the perfect candidate to work from here for us."
    s "The Körperschaft will be pleased to have you onboard."
    show Kris Kringle annoyed
    k "What if I refuse?"
    show Severus left_annoyed
    s "Refuse?"
    show Severus left
    s "Their is no room for you to refuse. Literally."
    s "I have here, my dear sir Kringle..."
    s "A full list of your gang-members and their designated addresses."
    show Kris Kringle tense
    s "What a shame that the Körperschaft now owns every single one of them. Including your sisters~!"
    show Kris Kringle angry
    k "WHAT?!"
    s "Here are copied papers if you want to see for yourself."
    k "THAT CAN'T BE! I will not let you!"
    s "You think Mr. Luchsenstein was prepared?"
    show Kris Kringle annoyed
    show Severus left_annoyed
    s "The work of an amateur."
    show Severus left
    s "You have no choice, Kris Kringle."
    s "You either help us or we will ensure to destroy everything you have left."
    show Severus left_annoyed
    s "This is a warning. Do not test me."
    show Kris Kringle angry
    k "Grrrrrr..."
    "This is absolutely useless."
    show Kris Kringle annoyed
    "I've been dragged into a corner without even getting the chance to fight!"
    show Severus left
    s "Now. Will you comply to everything the Körperschaft tells you to do?"

    menu:
        "Yes.":
            jump special_endingYes
        "No.":
            jump special_ending2

label special_ending2:
    show Severus left_annoyed
    s "Oh no no no no no~!"
    s "Let's not do that."
    show Severus left
    s "Just let me get rid of that annoying choice you love so much and change it to something much more lovely."
    s "After all."
    show Kris Kringle angry
    s "You're not in charge here, Kris Kringle."
    show Severus annoyed
    window hide
    pause 5
    window show
    show Severus left
    s "Now be good and continue."
    s "I will ask one more time."
    show Kris Kringle tense
    s "Will you comply to everything the Körperschaft tells you to do?"


    menu:
        "Yes.":
            jump special_endingYes
        "Yes.":
            jump special_endingYes

label special_endingYes:
    show Kris Kringle shocked
    show Severus
    s "Oh what a great CHOICE you made!"
    s "I‘m happy to give you just the little paperwork to forever bound your body and will to our glorious cause!"
    show Kris Kringle tense
    s "Sign right here!"
    s "…"
    show Severus annoyed
    s "What is it now?"
    show Severus
    s "You want to progress, right?"
    show Kris Kringle sad
    s "Who cares if Kris Kringle suffers a fate much worse than all the other endings you played out so far? All the wicked choices you made don‘t matter after all, right?"
    show Severus annoyed
    s "You shouldn’t care."
    s "I don’t care."
    show Kris Kringle very sad
    show Severus
    s "It‘s your fault where Kris Kringle will end up. You can end it anytime. So why do you keep him here?"
    s "I wouldn’t know. But I do know, that I will benefit from your wrongdoings."
    s "Even if it‘s just for a little bit."
    show Severus dark with dissolve
    s "And everything will return to normal. No matter how often you reset, I will never leave."
    s "Enjoy your precious THE END, [player_name]."

    scene black with fade
    window hide
    pause 3.0
    show ending smile with fade
    pause
    return
#Ending 10 ":D"



# --------------------------------------------------------------

label nothing:

    show Kris Kringle closed_mouth

    show Lux squint

    k "..."

    show Kris Kringle tense

    l "You know where we are right, prisoner?"

    menu:

        "YES. But know that I didn't do it! It was someone else! (Truth)":
            jump innoccent

        "Poopy Baby Fox! WHO STINKS! (Insult)":
            jump insult

        "(Keep quiet)":
            jump nothing2

label nothing2:
    show Kris Kringle thinking

    k "..."

    show Lux

    l "Still got nothing to say huh? Well let me change that."

    show Lux squint_grin

    l "We're in the one and only... hm... ...education room~! And my patience is slowly breaking with you."

    menu:

        "You got the wrong man! I didn't commit this crime! (Truth)":
            jump innoccent

        "Apocalyptic Foxshit! (Insult)":
            jump insult

        "(Silence.)":
            jump nothing3

label nothing3:

    show Kris Kringle annoyed

    k "..."

    show Lux annoyed

    l "Is that all you do?!"

    show Guard

    l "Come on! Say something!"

    menu:

        "It wasn't me! The terrorist attack was laid by someone else! (Truth)":
            jump innoccent

        "Orange Scavenger Fox-Pest! (Insult)":
            jump insult

        "(Nothing.)":
            jump nothing4

label nothing4:

    show Kris Kringle thinking

    k "..."

    pause 3

    show Lux angry

    pause 2

    l "..."

    show Lux annoyed

    l "You're just as boring as you were to capture."
    l "I didn't enjoy anything of this special bond we have here at all."
    show Lux angry
    l "Nothing! Nop! Not at all!"
    show Lux annoyed
    l "Would rather torture jealous Jerry all day all night instead of you!"
    show Kris Kringle closed_mouth
    l "Oh so much fun! I can't even wait to let him suffer."
    l "Jealous Jerry ALWAYS screams and never puts up a fight!"
    show Lux angry
    l "It's SUCH a joy, you know!"
    show Lux annoyed
    l "But you won't get a single taste of that! HAH! Who's jealous now?!"
    show Kris Kringle closed_mouth
    k "..."
    show Lux angry
    l "Fine! If you want to play the long game, fine!"
    show Lux annoyed

    l "You can have that!"

    menu:

        "...":
            jump nothing5

label nothing5:
    show Lux angry

    l "OH SO FINE WITH ME!"

    show Lux annoyed

    l "Guards!"

    l "Do your worst. The whole day till midnight. If I don't hear him scream to my office, you're not doing it right."
    l "I'm not going to waste my time with a clammed up oyster."

    show Lux squint_grin

    l "But do show me the inside if you manage to break his shell. I'll be more than happy to enjoy his tears afterwards."

    menu:

        "...":
            jump nothing6

label nothing6:
    show Kris Kringle smile
    show Lux angry
    pause 0.5
    show Lux angry:
        ease 0.9 xpos -1.0 ypos 0.0

    l "HMPF!"

    show Guard:
        ease 2 xpos 0.0

    show Kris Kringle closed_mouth:
        ease 2 xpos 0.4

    g "Oh... ...man..."

    show Guard sad

    show Kris Kringle grin

    g "...No one got boss that angry in a long time..."

    show Guard happy
    show Kris Kringle annoyed

    g "My boss always says no scream, not clean!"
    show Guard sad
    g "And you didn't scream or say anything at all..."
    show Kris Kringle tense
    g "That makes me sad..."
    show Guard serious
    g "And boss always says 'Don't get sad from the ones who are supposed to be the sad ones'."
    show Kris Kringle
    show Guard happy
    g "Don't worry though! I will do 1 backflip for every word you say!"

    menu:

        "...":
            jump nothing7

label nothing7:

    g "Go on! You can do it!"

    show Kris Kringle closed_mouth


    menu:
        "There are no other options...?"

        "...":
            jump nothing7_1

label nothing7_1:
    
    g "I believe in you! And as a reward you will see me do 1 or more backflips! Yeah yeah yeah!"
    show Guard serious
    show Kris Kringle smile
    g "I can do AT LEAST 3! 3 Backflips!"
    show Guard happy
    g "Doesn't that sound cool?! 3 Backflips!!!"
    g "I always dreamed to be the most backflippy [player_class] there is!"
    g "Just like 'boing! boing! boing!' And 'bim! bam! boom!' Done!"

    menu:
        "That... hm... doesn't help much."

        "...":
            jump nothing8
        "...":
            jump nothing8

label nothing8:
    show Kris Kringle closed_mouth

    k ". . . . . . . ....!"

    g "YES! You can make it!!! Go go go! Yippie yippie yippie!"

    show Kris Kringle angry

    k "...Grrr... ..."

    show Guard

    g "That's not a word, but we're getting there!"

    show Kris Kringle tense

    g "Say One, Two, Three, you can do it, YIPPIE!"

    menu:

        "...":
            jump nothing9
        "...":
            jump nothing9
        "...":
            jump nothing9

label nothing9:
    g "Say Four, Five, Six, I'm gonna show you the bestest tricks!"

    menu:

        "...":
            jump nothing10
        "...":
            jump nothing10
        "...":
            jump nothing10
        "...":
            jump nothing10

label nothing10:
    g "Say Seven, Eight, Nine, it's time the words shine!"

    menu:

        "...":
            jump nothing11
        "...":
            jump nothing11
        "...":
            jump nothing11
        "...":
            jump nothing11
        "...":
            jump nothing11
        "...":
            jump nothing11
        "...":
            jump nothing11
        "...":
            jump nothing11
        "...":
            jump nothing11

label nothing11:
    $ persistent.ending_9 = True
    g "Say Ten, Eleven, Twelve-!"

    show Guard

    g2 "[player_name]... that's not working."

    show Kris Kringle thinking

    g2 "Give up already. You won't get to him by encouragement and reward."

    show Guard sad

    g1 "B-But :( ..."

    g2 "Let's return to the Routine, [player_name]. You did your very best. Tomorrow is another day."

    g2 "You can try again there."

    show Kris Kringle tense

    g1 "Yes..."
    g1 "*Sniffle*"
    show Kris Kringle thinking
    g1 "...You're right..."
    g1 "*Sniffle sniffle*"
    g1 "Please hand me the not so backflippy knife..."

    scene black  with fade
    show ending nothing with fade

    pause
 
    return
#Ending 9