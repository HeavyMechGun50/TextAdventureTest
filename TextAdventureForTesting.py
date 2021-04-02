#Importing necessary modules
import time as tm
import random as rd
import sys
import os

xp = 0
act = ""
actBackup = ""

#Clear Screen Func
def cs():
    os.system('clear')
    print("A reminder for you to not press any buttons while the text is typing itself. \nYou may cause bugs, make reading it harder for yourself and potentially crash the game. \nSo, don't do it, alright?")
    print("\n_____________________________________________________________________________________________________________\n\n",)
#Typing Func
def print1by1(text, delay=0.025):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        tm.sleep(delay)
    print

#Entrance
cs()
print1by1("Unknown: Hello fellow wanderer! Welcome to \"The Escape from the Underworld\", a text adventure programmed on Python by HeavyMechGun50!")
print1by1("\nUnknown: What shall we call you?\n")
playerName = str(input(""))
playerName = playerName.capitalize()
print(playerName + "...")
tm.sleep(0.3)
print1by1("Unknown: That is an interesting name...\n")
print1by1("Unknown: And what about, the creator (your own name)?\n")
creatorName = input("")
creatorName = creatorName.capitalize()
if creatorName == playerName:
    print1by1("Unknown: Well, well. Of course. They are the same...\n")
tm.sleep(1.5)  
print1by1("\n________________________________________________________________________________\n", 0.015)

print1by1("\nUnknown: Haha...\n")
tm.sleep(0.35)
print1by1("Unknown: Didja really think I'd let you choose your own name?\n")
tm.sleep(0.35)
print1by1("Unknown: You ended up in the worst place in all 9 worlds!\n")
tm.sleep(0.35)
print1by1("Unknown: This, my friend, is where the unworthy go upon death.\n")
tm.sleep(0.35)
print1by1("Unknown: You don't get to change who you are!\n")
tm.sleep(0.35)
print1by1("Unknown: Your name is Sven and it always shall be Sven, you nitwit.\n")
tm.sleep(0.8)
print1by1("\n________________________________________________________________________________\n", 0.015)

print1by1("\nUnknown: Well, enuff chitchat. Let us begin, m'kay?.\n")
tm.sleep(0.5)
print1by1("Unknown: Oh. Sorry, where are my manners?\n")
tm.sleep(0.35)
print1by1("Unknown: I forgot to introduce myself! How stupid of me?\n")
tm.sleep(0.35)
print1by1("Unknown: The name's Gard, and I am an imp from Hel.\n")
tm.sleep(0.35)

print1by1("\nGard: I will be your mentor and ally throughout your journey through the depths of Helheim for judgement and redemption.\n")
tm.sleep(0.35)
print1by1("Gard: Cause thing is, I know that you died in battle.\n")
tm.sleep(0.35)
print1by1("Gard: It is strange to see a worthy man like you end up in Helheim...\n")
tm.sleep(0.35)
print1by1("Gard: However... I also know that the Valkyries who sort the worthy dead from the unworthy haven't been doing their job lately...\n")
tm.sleep(0.35)
print1by1("Gard: Helheim's been flooded to the brim with the dead for the past month..?\n")
tm.sleep(0.35)
print1by1("Gard: Never mind the time, it gets hard to tell the time difference between the land of the dead and the lands of the living\n")
tm.sleep(0.35)
print1by1("Gard: Thing is, I'll help you get to Valhalla.\n")
tm.sleep(0.35)
print1by1("Gard: Perhaps we'll also help to discover what the heck is up with the Valkyries..?\n")
tm.sleep(0.35)
print1by1("Gard: Maybe Odin'll deem me worthy for helping a noble warrior ascend to Asgard and help him solving the Valkyrie problems(?) on his journey..?\n")
tm.sleep(0.35)
print1by1("Gard: Who knows..?\n")
tm.sleep(0.45)

print1by1("Gard: But let me stop talking and let us focus on your backstory, shall we?!\n")
tm.sleep(1)
cs()
print1by1("Do you want to read the backstory or skip it? (s/r)\n")
storyChoice = input("")
storyChoice = storyChoice.lower()
choiceOptionsList1 = ["skip", "s", "read", "r"]
while storyChoice not in choiceOptionsList1:
    print1by1("It appears that you have entered something besides Skip, S, Read or R. Make sure to make your answer clearer next time!\n")
    storyChoice = input("")
    storyChoice = storyChoice.lower()


#Backstory
if storyChoice in choiceOptionsList1 and storyChoice == "read" or storyChoice == "r" :
    print1by1("________________________________________________________________________________\n", 0.015)
  
    print1by1("\n15 hours ago...\n")
    tm.sleep(1)

    print1by1("\nA battle is raging...\n")
    tm.sleep(0.5)

    print1by1("\nTwo enemy sides, Nilvaard and Mundahaar, are battling for more land.\n"
    )
    tm.sleep(0.5)

    print1by1("\nYou, Sven the Thunderer of Mundahaar, are holding a bronze sword in your hands that is dripping with blood.\n")
    tm.sleep(0.5)

    print1by1("\nRight by you are two of your comrades, Hughin and Munginn, each equipped with chainmail armor and each carrying a bronze tipped spear\n")
    tm.sleep(0.5)

    print1by1("\nAn iron straightened longbow is hanging from all your backs.\n")
    tm.sleep(0.5)

    print1by1("\nThe three of you charge straight into battle against a small crowd of five enemies.\n") 
    tm.sleep(0.5)

    print1by1("\nTheir armor appears to be better than yours: chainmail worn over hardened leather with ironclad shoulders and helmet.\n")
    tm.sleep(0.5)

    print1by1("\nHowever, you expect to do good in these odds and still go for an attack.\n") 
    tm.sleep(0.5)

    print1by1("\nYou parry their attacks and wait for the perfect moment to strike.\n") 
    tm.sleep(0.5)

    print1by1("\nAfter a series of difficult blocks, you finally gain the ability to swipe your sword straight through their abdomen.\n") 
    tm.sleep(0.5)

    print1by1("\nYour blade faces no resistance through the flesh and armor, and you effortlessly break through the spine as well. \n") 
    tm.sleep(0.5)

    print1by1("\nYour comrades are also fighting against the soldiers of the opposing nation, Nilvaard. \n")
    tm.sleep(0.5)

    print1by1("\nHowever, the Nilvaardians have them two to one and your friends are being overpowered by the enemies\' strength.\n") 
    tm.sleep(0.5)

    print1by1("\nThey cannot find the time to attack from blocking too much. \n")
    tm.sleep(0.5)

    print1by1("\nYou can see that their bronze bucklers are severely damaged and that soon enough it won't serve any more protection. \n")
    tm.sleep(0.5)

    print1by1("\nTo save your friends from the inevitable, you charge in with a bloodcurling battlecry and swing your sword around in a semicircle, drawing blood with the swipe. \n") 
    tm.sleep(0.5)

    print1by1("\nHughin, seizing this opportunity, counters the incoming enemy with a shield bash and sinks their spear deep into their chest, crunshing their ribs into sharp daggers of death. \n") 
    tm.sleep(0.5)

    print1by1("\nWith blood building up in his throat, the Nilvaardian collapses on the ground. \n") 
    tm.sleep(0.5)

    print1by1("\nNow that the odds have turned in your favor, you relax a bit. \n") 
    tm.sleep(0.5)

    print1by1("\nHowever, that was a mistake that would soon cost you your life. \n") 
    tm.sleep(0.5)

    print1by1("\nThe remaining three Nilvaardians shout behind them amid the conquest and a brute Nilvaardian marches for backup, carrying a massive battle axe as well as two more Nilvaardian soldiers. \n")
    tm.sleep(0.5) 

    print1by1("\nYou instantly feel a chill run down your spine and grasp your shield firmly. The brute quickly brings down his battle axe and blocking it takes a fair bit of your stamina. \n") 
    tm.sleep(0.5)

    print1by1("\nSeizing this opportunity, the nimble Nirvaardian swoops in to swing his sword in a wide arc, cutting your left cheek. You feel the warm blood gently descent down to your dark orange sideburns. \n") 
    tm.sleep(0.5)

    print1by1("\nYour friends are unable to help for they are busy battling against others.\n") 
    tm.sleep(0.5)

    print1by1("\nYou're by yourself. \n") 
    tm.sleep(0.5)

    print1by1("\nAnother blow from the brute hits your shield, breaking the bronze cover around the top and the front, cutting deep into the wood of your shield. \n") 
    tm.sleep(0.5)

    print1by1("\nHowever, your buckler still persists and although your main source of defense is damaged significantly, you still continue to battle for your country needs to defeat these vermin. \n") 
    tm.sleep(0.5)

    print1by1("\nAnother blow rains from the brute, cutting deep into your buckler. \n") 
    tm.sleep(0.5)

    print1by1("\nThe shield is almost destroyed and soon, it won't serve any more protection. \n") 
    tm.sleep(0.5)

    print1by1("\nThis may be your last battle but you still persist. \n") 
    tm.sleep(0.5)

    print1by1("\nYou glance at your shield and see that it is almost split in half. \n") 
    tm.sleep(0.5)

    print1by1("\nThere's a high chance that it will shatter into pieces with the next attack from the brute. \n") 
    tm.sleep(0.5)

    print1by1("\nWhile thinking, the nimble Nirvaardian decides to attack and you instictively counter his blow with a parry from your sword. \n") 
    tm.sleep(0.5)

    print1by1("\nSeeing your enemy stunned, you don't hesitate for a single second before slicing your blade through his neck, chopping his head off. \n") 
    tm.sleep(0.5)

    print1by1("\nHowever, while you were busy with killing that soldier, the brute draws his sword and slices towards you. \n") 
    tm.sleep(0.5)

    print1by1("\nYou attempt to parry but the brute's force overpowers your own.\n") 
    tm.sleep(0.5)

    print1by1("\nYour sword flies out of your hands and you pull a short dagger from your waistbelt. \n") 
    tm.sleep(0.5)

    print1by1("\nThe brute attacks again and you dodge underneath the sword and swipe your dagger to his wrist. \n") 
    tm.sleep(0.5)

    print1by1("\nYou feel an urge of satisfaction when you see the wrist starting to bleed. \n") 
    tm.sleep(0.5)

    print1by1("\nBut that doesn't seem to distract the brute: he gazes at you with red rimmed eyes. \n") 
    tm.sleep(0.5)

    print1by1("\nYou can tell that the attack angered him and the Nilvaardian brute once again strikes with a sword arc. \n") 
    tm.sleep(0.5)

    print1by1("\nYou attempt to dodge but just as you dodge, the brute brings the sword's hilt down to your temples by predicting your direction. \n") 
    tm.sleep(0.5)

    print1by1("\nYou collapse to one knee, stunned.\n") 
    tm.sleep(0.5)

    print1by1("\nThe brute takes a step back and you feel an excruciating pain from your stomach only to see your insides falling out of it. \n") 
    tm.sleep(0.5)

    print1by1("\nYou groan with anger, pain and determination and slowly bring your hand towards your head to aim directly at the face of the laughing Nilvaardian and throw it with all remaining force inside you. \n") 
    tm.sleep(0.5)

    print1by1("\nThe brute, taken by surprise sees the incoming blade a second too late and he also collapses on the ground with an impaled forehead. \n") 
    tm.sleep(0.5)
    
    print1by1("\nWith all your life force fading away from your body, you collapse to the ground and close your eyes for the incoming hands of the Valkyries to collect your soul and bring it to Asgard... \n")
    tm.sleep(1)

    print1by1("\nHowever, the hands of the underworld grasp your soul and they quickly pull you underground towards your new home, the City of Helheim.\n")
tm.sleep(1.5)
cs()


#___________________________________Game - Part 1_____________________________________________________________________________


tm.sleep(0.5)
print1by1("10 hours after landing in Helheim\n")  
tm.sleep(0.5)
print1by1("...\n", 0.3)
tm.sleep(0.35)
print1by1("You hear a thumping sound and a call...\n")
tm.sleep(0.35)
print1by1("\n\"Sven? Where on Helheim are ya at?\"\n")
tm.sleep(0.35)
print1by1("You recognize the voice. It's Garm. What will you do?\n")
tm.sleep(0.35)
print1by1("Your options are: \nA) Call Gard \nB) Do nothing \nC) Insult him\n")
tm.sleep(0.35)
act = input("")
act = act.lower()
choiceOptionsList2 = ["a", "b", "c"]
while act not in choiceOptionsList2:
    print1by1("\nWhat you've entered is not valid! Re-enter it! Your options should be right above this message, in case you forgot.\n")
    storyChoice = input("")
    storyChoice = storyChoice.lower()
    if act in choiceOptionsList2:
        break

if act == "a":
    print1by1("Sven: \"I'm here, just lying down. Needed to rest for a sec.\n")
elif act == "b": 
    print1by1("You do nothing.\n")
    tm.sleep(1.5)
    print1by1("Your hear him call again and again.\n")
    tm.sleep(0.5)
    print1by1("You eventually get sick of him calling you.\n")
    tm.sleep(0.35)
    print1by1("Sven: Shut up! I'm here, alright! Follow my voice!\n")
elif act == "c":
    print1by1("Sven: God damn it! Can't I rest for a friggin' second, you li'l idiot? Jeez. You nearly woke up the entire world!\n")

tm.sleep(0.35)
print1by1("Gard follows your voice and soon finds you.\n")
if act == "a":
    print1by1("A grin is on his face.")
elif act == "b":
    print1by1("He's looking at you with a straight face.\n")
elif act == "c":
    print1by1("His feelings look hurt and a sad expression is on his face\n")
    tm.sleep(0.35)
    print1by1("Gard: What was that for? You mad at me? I didn't do nothin'!\n")
    tm.sleep(0.35)
    print1by1("What will you do? Your options are: \n A) Apologize \n B) Felt like it\n")
    actBackup = input()
    actBackup = actBackup.lower()
    if actBackup == "a":
        print1by1("Sven: I'm sorry. I've been in a bad mood ever since I ended up in this place. It's colder than anything I've experienced!\n")
        tm.sleep(0.35)
        print1by1("Garm looks at you undertstandingly and lowers his voice.\n")
        tm.sleep(0.35)
        print1by1("Garm: I get ya. If I was a noble warrior living in the cold of Hel, I'd be pissed too.\n")
        tm.sleep(0.35)
        print1by1("Garm: Unfortunately, that ain't the case. I died of old age. S'pose it's a sin to die of old age.\n")
        tm.sleep(0.35)
        print1by1("Garm: Never mind. I've gotten used to the icyness of this place.\n")
        tm.sleep(0.35)
        print1by1("Garm looks at you with a forgiving gaze. A smile forms on his face {} \n You've gained an experience point! Collect more to unlock a happy ending!\n".format(tm.sleep(0.35)))
        xp += 1
    elif actBackup == "b":
        print1by1("Sven: Felt like insulting someone. I'm grumpy. It's cold here, goddammit. Cold pisses me off.\n")
        tm.sleep(0.35)
        print1by1("Garm looks sad but looks at you with an understanding gaze.\n")
        tm.sleep(0.35)
        print1by1("Garm: I know what you mean, pal.\n")
        tm.sleep(0.35)
        print1by1("Garm: I was in a bad mood when I landed here but now, everything seems normal.\n")
        tm.sleep(0.35)
        print1by1("Garm: It takes time to adapt here, though.\n")
        tm.sleep(0.35)
        print1by1("Garm: 'specially, the chills of this place...\n")
        tm.sleep(0.35)
    else:
        while actBackup != "a" or actBackup != "b":
            print1by1("Invalid input. Re-enter your answer as a multiple choice, with your choices being A or B")
            actBackup = input()
            actBackup = act.lower()
            if actBackup == "a" or actBackup == "b":
                break


if act == "a" or act == "b":
    print1by1("\nGarm: So, you're probably wondering why I've been searching for you, don't ya?\n")
    print1by1("Garm: I got some news for you. Good ones, in case you were wonderin'.")
else:
    print1by1("\nAnyway, I got some news for you. Good ones too.")    
    