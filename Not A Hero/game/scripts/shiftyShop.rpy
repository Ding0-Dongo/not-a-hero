default entryLines=["Hm? Oh, it's you again...","Yes, yes, buy something!","Shifty has wares if you have coin","Show me the money first", "An animal control man was in the neighborhood just a moment ago, so forgive me if I'm a bit... jumpy...","Leave your trash can lid open tonight, alright, kid?", "I saw something shiny on the street today. Turned out it was just a gum wrapper. Can you believe it?","An alley cat hissed at me today. I'm gonna have nightmares for a week..."]
default boughtLines=["Buy another. You never know when you might need it.","No refunds, no exchanges!","I'll give you a discount if you buy in bulk next time.(He won't.)","You want a bag for that?","Ah, you've got taste!","Good eye for quality you've got there.","Great choice."]

label shiftyShop:
    #remove before demo
    $ energy = 3
    $ dollars = 10

    stop music
    play sound ShopBellRingAudio
    play music ShopBackgroundMusic volume 0.5

    scene shopRoom

    show screen StatUI

    show shifty with fade

    $ shiftyGreeting = renpy.random.choice(entryLines)


    s "[shiftyGreeting]"


label shiftyTransition:
    menu:
        "Talk about Shifty":
            s "Hm? You want to know about me? You're not a cop, are you?"
            e "A cop? No, I'm... I'm just a HERO."
            s "A HERO?! Bah, that's even worse! Well, listen up. All you need to know is that I am most definitely NOT a raccoon in a trenchcoat."
            e "Huh? (Where'd that come from?)"
            jump shiftyTransition
        "Talk about Downtown":
            s "Downtown? Bah, it's as filthy as it gets around here. Hmph, just the way I love it!"
            e "You... you love it?"
            s "What's not to love? Valuable trash everywhere for the taking.... ah, but the fleas. I don't like the fleas."
            e "(He's kind of strange...)"
            jump shiftyTransition
        "Talk about the Hero Association":
            s "The Hero Association? Don't even talk to me about them."
            e "What do you have against them?"
            s "Bah! Always chasing me away from trash cans and such. Something something 'private property'. Don't they know it's a free country?!"
            e "(???)"
            jump shiftyTransition
        "Look at Shifty's goods":
            s "Take a look at what I got..."
            jump shopMenu 



label shopMenu:
    
    $ boughtItemPhrase = renpy.random.choice(boughtLines)

    menu: 
        "1 Energy Drink":
            if energy < 10 and dollars >= 5:
                $ energy += energyDrink
                $ dollars -= 5
                s "[boughtItemPhrase]"
                jump shopMenu
            elif energy == 10:
                s "Don't go biting more than you can chew bud."
                jump shopMenu 
            elif dollars < 5:
                s "Hey, hey! Hands off what you can't afford, pal!"
                jump shopMenu
        "1 Energy Drink Plus":
            if energy < 8 and dollars >= 10: 
                s "[boughtItemPhrase]"
                $ energy += energyDrinkPlus
                $ dollars -= 10
                jump shopMenu
            elif energy >=8:
                s "Don't go biting more than you can chew bud."
                jump shopMenu
            elif dollars < 10:
                s "Hey, hey! Hands off what you can't afford, pal!"
                jump shopMenu
        "1 Energy Drink Max":
            if energy < 6 and dollars >= 15:
                s "[boughtItemPhrase]"
                $ energy += energyDrinkMax
                jump shopMenu
            elif energy >= 6:
                s "Don't go biting more than you can chew bud."
                jump shopMenu
            elif dollars < 15:
                s "Hey, hey! Hands off what you can't afford, pal!"
                jump shopMenu
        "I've gotta go!": 
            s "Come back soon!"
            stop music
            play music MainMusic
            call testStart
