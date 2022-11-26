label Pursenapper:
    #Day 6 (Pursenapper & Thiefstopper)
    #scene city
    stop music
    play music ChaseMusic volume 0.5
    hide city
    hide blackScreen
    show alleyway
    "Downtown Normington"
    "(Ellis is in the middle of a stroll in Downtown Normington.)"
    play sound ScreamAudio
    "Help, thief!"
    play sound "<from 15 to 21>audio/runconcrete.mp3"
    "(A man wearing a ski mask and comically-oversized prison pinstripes runs past Ellis.)"
    jump Purse_options

label Purse_options:
    menu:
        "Oh well.":
            jump OhWell_Option
        "Tackle him (Requires 5 Strength)":
            jump TackleHim_Option
        "Chase him (Requires 5 Speed)":
            jump ChaseHim_Option
        "Add 5 Strength":
            jump FiveStrength_Option
        "Add 5 Speed":
            jump FiveSpeed_Option

label OhWell_Option:
    "(Before Ellis realizes what's happening, the thief's already disappeared around the street corner.)"
    play sound SirenAudio
    "(He hears sirens wail in the distance, and nervously crosses the street, continuing on his walk.)"
    stop sound
    stop music
    show blackScreen
    with  dissolve
    "" #fade to black
    "(He wishes he'd done something to help, but it's too late now.)"
    hide blackScreen
    show city
    play music MainMusic
    jump testingMap

label TackleHim_Option:
        if strength < 5:
            "Elis needs a strength of 5 to tackle him!"
            jump Purse_options
        else:
            play sound TackleAudio
            "(Without thinking, Ellis jumps at the man and tackles him to the ground.)"
            "(Carefully, of course. He makes sure the perpretrator's head doesn't hit the sidewalk.)"
            "(The robber seems surprised.) What the ... get offa me!"
            "(Ellis doesn't notice the man, instead looking up at the slowly-forming crowd.)"
            show ellis Neutral
            e "Um... could someone call the police?"
            hide ellis Neutral
            "(The person who was almost robbed runs up to him.) Oh, thank you so much!"
            play sound PhoneAudio
            "(They take the bag, pull a phone out of it, and quickly make the call.)"
            stop sound
            play sound SirenAudio
            "(The police arrive not long after, and take away the would-be burglar.)"
            stop music
            play music AwardMusic 
            play sound Cheer
            "(The crowd claps.)"
            "(Ellis smiles and waves nervously, and quickly ducks out of the crowd, resuming his stroll.)"
            stop sound 
            show blackScreen
            with  dissolve
            "" #fade to black
            play sound ChaChingAudio
            "The association awards Ellis $10 for his deeds."
            stop sound
            $ money += 10
            play sound AchievementAudio
            "(Thiefstopper commission unlocked.)"
            hide blackscreen
            stop music
            stop sound
            show city
            play music MainMusic
            # unlock commision: thiefstopper
            #end story quest (COMPLETE)
            jump testingMap

label ChaseHim_Option:
        if speed < 5:
            "Elis needs a speed of 5 to chase him!"
            jump Purse_options
        else:
            stop sound
            play sound "<from 15 to 21>audio/runconcrete.mp3"
            "(Ellis quickly bolts after the man.)"
            "(They run down a few blocks - thanks to Ellis's training, he's only slightly winded.)"
            stop sound
            play sound GaspAudio
            "(The intersection up ahead is familiar - he takes a side route and surprises the burglar as he cuts him off on a side street.)"
            "(Ellis takes the bag from the burglar and begins heading back to the waiting owner.)"
            "(The burglar calls after him.) Hey! Kid, that's not yours!"
            "(Ellis turns around.)"
            show ellis Neutral
            e "It's not yours either."
            hide ellis Neutral
            "(Ellis walks back to the scene of the crime.)"
            show ellis Neutral
            e "I think this is yours... sorry it took so long."
            hide ellis Neutral
            "(The owner looks at him, starry-eyed) Wow, you're like a hero..."
            "(Ellis gets flustered)"
            show ellis Neutral
            e "What-? No, I'm... well, not yet. I'm still in... in training..."
            hide ellis Neutral
            "(The owner hugs their bag closer to themselves, eyes almost shining.) Thank you!"
            show ellis Neutral
            e "You're... you're welcome..."
            hide ellis Neutral
            stop music
            play music AwardMusic 
            show blackScreen
            with  dissolve
            "" #fade to black
            play sound ChaChingAudio
            "The association awards Ellis $10 for his deeds"
            stop sound
            $ money += 10
            play sound AchievementAudio
            "(Thiefstopper commission unlocked.)"
            hide blackscreen
            stop music
            stop sound
            show city
            play music MainMusic
            #unlock comission: thiefstopper
            #end story quest (COMPLETE)
            jump testingMap

label FiveStrength_Option:
    $ strength += 5
    jump Purse_options

label FiveSpeed_Option:
    $ speed += 5
    jump Purse_options