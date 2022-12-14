# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
### ^ ok so these. these are character definitions, I've gone and chucked them all
### into definitions.rpy
### ALTERNATIVELY, we can define a character as:
### define e = Character('Eluna', color='#ff94c1', image = "eluna")
### name, color (of like their little text box), character sprite


#ok so you may be wondering why there are so many green text
#these are comments; I've left them in just in case y'all needed some guides
#renpy pre-generated for you
#if you decide you no longer need these comments, simply remove them.



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.


    # Just putting this here because I am dumb and want to test a tutorial.
    # jump dayZero
    # return

    menu:

        "Go to tutorial.":
            jump tutorial
        "Skip tutorial":
            jump meetTheTeamStart
        "Actually start The Game":
            jump dayZero
        "Go to Day 7":
            jump daySeven
        "Go make an Accident":
            "criteria?"
            menu:
                "succeed 1st check":
                    $ stamina = 7
                "succeed 2nd check":
                    $ stamina = 7
                    $ speed = 7
                "succeed all checks":
                    $ stamina = 7
                    $ speed = 7
                    $ strength = 7
            jump theAccident
        "Test ending":
            "criteria?"
            menu:
                "fulfill standing":
                    $ standing = 4
                "fulfill social":
                    $ social = 4
                "fulfill both":
                    $ standing = 4
                    $ social = 4
                "neither":
                    $ standing = 1
                    $ social = 1
            jump theEnding
        "Tests Your Quests Here":
            menu:
                "Test 'Talk Things Out'":
                    jump talkThingsOut
                "Test 'Bullies'":
                    jump bullies
                "Test 'Petty Thievery'":
                    jump ptStart
                "Test 'Josephine's Second...'":
                    jump jshrStart
                "Test 'Pursenapper'":
                    jump Pursenapper
                "clinic delivery":
                    jump clinicDelivery
                "PSA":
                    jump psa
                "coffee w/ friends":
                    jump coffeeWithFriends
                "fundraising":
                    jump fundraising
                "shelter volunteering":
                    jump volunteerShelter
                "clinic volunteering":
                    jump volunteerClinic
                "socialize":
                    jump socializeFirst
        "Test Your Maps Here":
            menu:
                "MapUI0":
                    $ day = 0
                    show cityMap
                    jump call_mapUI
                "Map UI1":
                    show cityMap
                    $ day = 1
                    jump call_mapUI
                "Map UI2":
                    show cityMap
                    $ day = 2
                    jump call_mapUI
                "Map UI3":
                    show cityMap
                    $ day = 3
                    jump call_mapUI
                "Map UI4":
                    show cityMap
                    $ day = 4
                    jump call_mapUI
                "Map UI5":
                    show cityMap
                    $ day = 5
                    jump call_mapUI
                "Map UI6":
                    show cityMap
                    $ day = 6
                    jump call_mapUI
        "Test Your Places Here":
            menu:
                "Visit Shifty":
                    jump shiftyShop
                "Park":
                    $ day = 3
                    jump park

        "Test your interactions":
            menu:
                "Day 1":
                    jump interactionsDayOne
                "Day 2":
                    jump interactionsDayTwo
                "Day 3":
                    jump interactionsDayThree
                "Day 4":
                    jump interactionsDayFour
                "Day 5":
                    jump interactionsDayFive
                "Day 6":
                    jump interactionsDaySix
                "Day 7":
                    jump interactionsDaySeven
    
    ### Added label testStart to jump to at the end of the tutorial. 

    label meetTheTeamStart:
    menu: 
        "test Meet the Team story quest":
            call meetTheTeam 
            jump testStart
        "no":
            jump testStart
        "Test Day Zero Main Story":
            jump dayZero

    label testStart:

    # Resetting energy and stress after tutorial. Might need to do this at the beginning of every day?
    $ energy = energyMax
    $ stress = 0

    scene whiteRoom

    show screen StatUI

    show ellis Neutral with fade

    e Neutral "H-Hey..."

    e Terrified "So I heard you were going to be my... android?"

    e Neutral "Or not since I'm talking to a camera... aha ahaaa..."

    e "..."

    e "*introverted noises*"

    e "pls stop talking to me aaaaaaaaa-"

    show potato

    e "DSKLAJFLKS;AJFL"

    scene whiteRoom

    e "w-where did everyone go?"


    show screen NormingtonCityMap

    #show screen NormingtonCityMap
    show city

    "this is normington city."

    "what would you like to do?"

    menu:
        "Visit Normington City":
            hide screen StatUI
            jump testingMap
        "Visit Shifty Shop (DELETE LATER)":
            jump shiftyShop
        "PurseSnatch Quest (delete this before demo)":
            hide screen NormingtonCityMap
            jump Pursenapper
        "Visit Normington Coffee":
            hide screen NormingtonCityMap
            jump NormingtonCoffee

label testingMap:
    #hide screen NormingtonCityMap
    #"whoah this works"
    #jump goodEnd
    jump call_mapUI
    return

label testingMap2:
    #hide screen NormingtonCityMap
    "ok so the second one works too"
    jump goodEnd
    "time to visit shifty"
    call shiftyShop

#label goodEnd:
    #"good end"
    #return
    #"time to visit shifty"

    #call shiftyShop

label goodEnd:
    "good end"
    return
