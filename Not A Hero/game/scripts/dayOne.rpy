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

    scene whiteRoom

    show ellis with fade

    e "H-Hey..."

    e "So I heard you were going to be my... android?"

    e "Or not since I'm talking to a camera... aha ahaaa..."

    e "..."

    e "*introverted noises*"

    e "pls stop talking to me aaaaaaaaa-"

    show potato

    e "DSKLAJFLKS;AJFL"

    scene whiteRoom

    e "w-where did everyone go?"

    show screen NormingtonCityMap

    "this is normington city."

label testingMap:
    hide screen NormingtonCityMap
    "woah this works"
    jump goodEnd

label testingMap2:
    hide screen NormingtonCityMap
    "ok so the second one works too"
    jump goodEnd

label goodEnd:
    "good end"
    return