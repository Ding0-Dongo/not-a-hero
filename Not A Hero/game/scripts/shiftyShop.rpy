label shiftyShop:
    $ energy = 3
    scene shopRoom

    show screen StatUI

    show shifty with fade


    s "ay im a little racoon guy hehe look at me"

    s "so do you wanna buy some wares off of me?"

    s "lemme show you what i gotta offer"

    jump shopMenu 



label shopMenu:
    s "what can i do for ya?"
    menu: 
        "1 energy drink":
            $ energy += energyDrink
            s "enjoy the soder"
            jump shopMenu 
        "some stupid other drink":
            s "well this won't help ya much but here ya go"
            $ energy += 1
            jump shopMenu
        "im done shopping": 
            s "come back soon :)"
            call goodEnd
