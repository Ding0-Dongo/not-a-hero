label graffiNo:
    if commission3Done:
        e "Here I come!"
        thug "NOT YOU AGAIN-"
        $ money += 10
        return
    else:
        "Downtown Normington, random time afternoon"
        "*sketchy noises*"
        D "We've received reports of rampant gang activity around this part of Normington."
        D "Including but not limited to: thievery, shoplifting, obscene graffiti-"
        e "Like the one right in front of us."
        gangster "WACHU SAY ABOUT MY WORK OF ART; MY MASTERPIECE?!"
        D "We kindly request you take down your \"work of art\" before we resort to filing your case under the Normington Association of-"
        gangster "YEAH YEAH, BLAB ALL YOU WANT, YOU AINT GETTING ANYTHING OUTTA ME, ANDROID-BOY!"
        D "...Interrupt me once more and I'll-"
        ultraMobBoss "Well well well... what do we have here?"
        ultraMobBoss "Roaming into my territory and threatening my boys..."
        ultraMobBoss "Tsk... Tsk... Tsk..."
        ultraMobBoss "You heroes are all the same."
        e "But you're committing crimes which is bad!"
        ultraMobBoss "Yap any more, and I'll have to put you down, dog."
        gangster "YEAH YOU TELL 'EM BOSSMAN!"
        "Arid winds blows through the quiet alleyway, DELTA locking eyes with both the thug and the Godfather simultaneously."
        D "Ellis, I'll defend you. Do what you must to resolve this."
        "What should I do...?"
        menu:
            "Attempt to help DELTA by attacking the goon.":
                "Without thinking, Ellis charges straight towards the goon."
                "Roll for initiative!"
                "..."
                "Let's just say Ellis is no longer allowed to roll die!"
                "Thankfully, DELTA rolled a 20 and the thug is put down. Very forcibly."
                gangster "OW"
                ultraMobBoss "AAAAAAAA"
                "The boss starts booking it down the road; far, far down the road."
                gangster "BOSS WHERE ARE YOU GOING-"
            "Attempt to help DELTA by attacking the boss.":
                "Without thinking, Ellis charges straight towards the godfather."
                ultraMobBoss "AAAAAAAAAAAAAAAAAAAAAAAAAA DKFLSAJF;LSJADFLS;KA"
                "Startled, and quite frankly terrified, the godfather starts to sprint away."
                gangster "WHY ARE YOU RUNNING AREN'T YOU SUPPOSED TO BE LIKE THE TOP DOG, THE MOST POWERFUL DUDE MAN???"
                ultraMobBoss "I DUNNO USUALLY THE HERO TAKES DOWN THE GOONS FIRST."
                gangster "WHAT."
                "The two take off into a very conspicuous dark alleyway, never to be seen for the rest of the day."
            "Start erasing the graffiti.":
                gangster "STOOOOOOOOOOOOOP!!!!11!"
                gangster "I-I was serious when I said this is my work of art..."
                gangster "So it all started when I was 5 years old when I first saw Leonardo Da Vinci's Mona Lisa."
                "The thug starts relaying his entire life story up until this point."
                "Every single hardship, trauma, disappointment, failure, embarrassment. By the end of his monologue, Ellis understands the thug more than anyone else he had up until this point."
                "Enlightening, really."
                gangster "...and then I got rejected from art school and that's how I got to where I am now."                
                gangster "..."
                gangster "...I need a moment-"
                "The thug says before promptly dashing off, the mob boss having gone off ever since he started monologuing."
                e "Well then."
        "After dealing with whatever else that remained, DELTA and Ellis spent the next half hour scrubbing off some quite amazingly sprayed graffiti."
        $ money += 10
        $ commission3Done = True
        return