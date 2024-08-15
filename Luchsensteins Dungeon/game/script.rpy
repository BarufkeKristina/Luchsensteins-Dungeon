# Sie können das Skript Ihres Spiels in dieser Datei platzieren.
# Code markieren, f1 und dann: Create Manual Folding Range from Selection -> richtig swag um code zusammenzufassen

# Deklarieren der Charaktere
define l = Character(_("Lux Van Luchsenstein"), color="#cb7315")
define k = Character(_("Kris Kringle"), color="#1293de")
define g = Character(_("Guard"), color="#7e7e8b")
define g2 = Character(_("Other Guard"), color="#7e7e8b")
define g1 = Character(_("Guard Bulli"), color="#7e7e8b")
define q = Character(_("???"), color="#cb7315")


$ biteCounter = 0

# Alle Bilder:

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

#Other Character:
image Ki Kringle:
    "Ki Kringle.png"
    zoom 0.9
    xpos 0.6 
    ypos 1.7

image Baseball:
    "baseball.png"

# </Alle Bilder Ende>

transform move_left_to_right:
    xalign 0.0  # Start on the left side
    linear 0.2 xalign 1.3  # Move to the right side over 3 seconds

transform move_left_to_right_short:
    xalign 2.1  
    linear 0.2 xalign 2.5  





# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False

# Hier beginnt das Spiel.
label start:
    $ biteCounter = 0
    # play music "Dynamite Dash - Donkey Kong Country Tropical Freeze [OST].mp3"
    scene Eiswuste
    with fade
    "It's been quite a while since we left the city."
    "Where the hell are we going?" 
    
    show Kris Kringle with dissolve:
        xpos -0.5
        ease 3.0 xpos 0.1 ypos 0.0    

    "Even with Ki I've never gone close to where I am right now."

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
#ab hier fertig!


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
            jump unconcious

        "(Say nothing)":
            jump death

    return
#fertig!

label death:

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
# fertig!

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

    scene Cell:
        ypos -0.5
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
#fertig!

label innoccent:

    show Lux annoyed
    l "You seriosly think I believe you? Hahaha! What fool do you take me for?"

    l "You've murdered hundreds of innocent people in that little stunt of yours! You'll not get away with your crimes!"

    l "Even worse! You harmed our most beatiful president there is!"

    l "For what you have done to THE Queen, Side Character herself, I will never forgive you!"

    k "You have to listen to me! The real culprit is still out there!"

    l "Then why was YOUR baseball bat found there, hm? I've seen the crimescene with my own eyes."

    l "Was not a magnificent thing to see. I can say that much."

    k "Someone stole it, duh?! I didn't do shit."

    l "Let me tell you something."

    l "Something really... really important."

    l "I don't give a flying fox if you commited that terrorist attack or not."

    l "You may be innocent..."
    
    l "Yes you might~..."

    l "But you're still a criminal aren't you?"

    k "..."

    l "Soooo~ it doesn't matter if you did it~! At the end of the day you still belong here~!"

    l "And NOTHING is going to change that."

    l "Or was sneaking into the government of Terram Solis and flirting with the president to manipulate her something you also want to deny."

    k "...!"

    l "That's what I thought."


    return
#unvollständig

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
            jump unconcious

        "No. HA! (Let him be.)":
            jump letbe
#fertig!

#Versuch von Funktion bezüglich Animation von Schlägen:
"""
label KrisKringlebeatUp(timeT=0.7):
        $ renpy.log("KrisKringlebeatUp called with timeT: {}".format(timeT))
        show Kris Kringle angry:
            ease 0.1 xpos 0.03 ypos 0.35
            pause 0.07
            ease timeT xpos 0.09 ypos 0.32
        return
call KrisKringlebeatUp()
"""

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

    #<Hitting>:
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
            ease 0.7 xpos 0.09 ypos 0.32
    #</hitting>

    k "AAGH!!" with vpunch

    #<Hitting>:
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
            ease 1.5 xpos 0.09 ypos 0.32
    #</hitting>

    k "GAAH!!!" with vpunch

    #<Hitting>:
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
            ease 2.0 xpos 0.09 ypos 0.32
    #</hitting>

    k "GRAGH!!! Stop this madness!" with vpunch

    show Kris Kringle annoyed
    
    show Lux normal_grin

    l "What madness? You've earned this all by yourself~!"

    show Kris Kringle angry:
        ease 0.07 xpos 0.09 ypos 0.29
        pause 0.07
        ease 0.1 xpos 0.09 ypos 0.32
    

    k "You just beat up the prisoners until they break down?! No wonder you-"

    #<Hitting>:
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
            ease 0.7 xpos 0.09 ypos 0.32
    #</hitting>

    k "AGGHHH...!! huff huff..." with vpunch

    show Lux annoyed

    l "No. Only you get the extra treatment for being the nasty rebell you are."

    l "This case is... personal."

    show Kris Kringle annoyed

    show Lux

    l "It's just as you said. Threats don't mean anything to you. But maybe actions do."

    #<Hitting>:
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
            ease 1.0 xpos 0.09 ypos 0.32
    #</hitting>

    k "UGHH... huff... huff... what do you..." with vpunch

    show Lux squint

    show Kris Kringle angry:
        ease 0.07 xpos 0.09 ypos 0.29
        pause 0.07
        ease 0.1 xpos 0.09 ypos 0.32

    k "What do you want out of this?! By constantly hitting me you won't get ANYTH-"

    #<Hitting>:
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
            ease 2.0 xpos 0.09 ypos 0.32
    #</hitting>


    k "AAaaarghh... ugh... huff..." with vpunch

    l "Less talking. More screaming."

    show Kris Kringle annoyed
    show Lux normal_grin

    l "That is if you hold your life dear. Or there won't be a life to live left until I'm done with you."

    menu:
        "Your life seems pretty miserable for a peasant. (Start insulting again)":
            jump unconcious

        "(Grin at him. Seductively?)":
            jump grinSeductively

        "(Give in to the pain. There is nothing you can do anyways)":
            jump giveIn
#fertig!
label grinSeductively:

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
#fertig! Ending

label giveIn:

    #<Hitting>:
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
            ease 0.7 xpos 0.09 ypos 0.32
    #</hitting>
    
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
#fertig

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
#fertig

label pleadMercy:

    k "... ..."

    k "...Stop... ..."

    l "Giving up already~? Ahaha!"

    l "I'm dissapointed I must say... you looked so tough on our way here."

    l "And all I see now is a miserable piece of shit!"

    k "GRRRrrr... you..."

    l "Oooh and trust me! I didn't even get started..."

    k "Uagh!" with vpunch

    l "Aren't you having a fun time? Because I sure do! I'm having a very good time~!"

    menu: 
        l "If you truly want me to stop and just lock you away... show it!"
        "(Beg for mercy)":
            jump begMercy

        "(Say nothing)":
            jump sadEnding
#unvollständig

label sadEnding:

    "I-I... I can't..."

    "I can't keep up..."

    "Everything is falling in front of me."

    "My life crumbling before my very eyes."

    "I've been so close to death a couple of times now."

    "B-But..."

    "Never like this!"

    "Why do I feel so sad out of the sudden..."

    # Kris Kringles Perspektive Nox wird blurry und hintergrund auch

    "Everything starts to get blurry..."

    k "UUugh..." with vpunch

    "I wonder what MatMat is doing..."

    k "...!" with vpunch

    k "... Huff... ... Huff... ..."

    "I hope she's doing better than me."

    "At least she can be happy with her whore husband. That asshole."
    "He'd be more than happy to see me like this."

    k "..." with vpunch

    "I can't keep my eyes open anymore..."

    scene black with fade

    "At the end, everything I worked for was for nothing."

    "I wish I would've spent more time with Ki."

    "But it's too late for that."

    "I'm sorry, sister."

    return
# unvollständig

label begMercy:
    k "..."
    k "...Lux..."

    l "Yees?"

    k "... ...Please..."

    l "Go on..."
    l "Don't let me wait too long~!"

    k "...huff..."

    l "Wait! Let me help you~!"

    k "AAGH...!" with vpunch

    l "Could I help that one brain cell of yours~? Or do you need anoth-"

    k "NO-! ..." with vpunch

    l "Oh so eager, hm?"

    k "...Please don't hit me again... hah..."

    l "Now look at that! Such a good boy! Didn't think you'd plead me to stop on your first day..."

    l "Utterly dissapointing."

    l "But at the same time... better for my amusement!"

    l "Can't wait to hear you doing that tomorrow as well."

    l "Although you need to be a lot more... hm... what do they say... energetic with your cries."

    l "Or else..."

    l "I might get too bored and swing this beloved baseball bat again~!"

    #goes closer leaning down

    l "Maybe in the gut..."
    l "Or your skull..."
    l "Your arms seem very hitable."

    k "...!"
    l "For now! I've heard enough."
    l "Bring him to his cell at once! He's done for the day."

    return
#unvollständig

label unconcious:

    k "What's with the rope...?"

    show Lux squint_grin

    l "..."

    "That doesn't look too good!"

    k "H-Hey no hard feelings, right!?"

    

    return
#unvollständig


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
#fertig
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
#fertig
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
#fertig
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
#fertig
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
#fertig
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
#fertig
label nothing7:

    g "Go on! You can do it!"

    show Kris Kringle closed_mouth


    menu:
        "There are no other options...?"

        "...":
            jump nothing7_1
#fertig
label nothing7_1:
    
    g "I believe in you! And as a reward you will see me do 1 or more backflips! Yeah yeah yeah!"
    show Guard serious
    show Kris Kringle smile
    g "I can do AT LEAST 3! 3 Backflips!"
    show Guard happy
    g "Doesn't that sound cool?! 3 Backflips!!!"
    g "Just like 'boing! boing! boing!' And 'bim! bam! boom!' Done!"

    menu:
        "That... hm... doesn't help much."

        "...":
            jump nothing8
        "...":
            jump nothing8
#fertig
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
#fertig
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
#fertig
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
#fertig
label nothing11:
    g "Say Ten, Eleven, Twelve-!"

    show Guard

    g2 "Bulli... that's not working."

    show Kris Kringle thinking

    g2 "Give up already. You won't get to him by encouragement and reward."

    show Guard sad

    g1 "B-But :( ..."

    g2 "Let's return to the Routine, Bulli. You did your very best. Tomorrow is another day."

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

    # "If you do nothing, you're not doing anything wrong" ending.
    # Bro did you not see all the cool dialogue options :O Backflipcounter = 0 :P
 
    return
#fertig Ending