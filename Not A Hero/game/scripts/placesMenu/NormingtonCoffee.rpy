label NormingtonCoffee:
<<<<<<< Updated upstream
=======
    image deltaNeutral = "images/Delta/delta neutral.png"
    image ellisNeutral = "images/Ellis/Tilt.Neutral.png"
    image ellisHappy = "images/Ellis/Up.Confident.png"
    image phiNeutral = "images/Phi/phi neutral.png"

    hide screen NormingtonCityMap
    hide screen continueNextDay
>>>>>>> Stashed changes
    scene coffeeshop_inside

    show screen StatUI

    show shifty with fade

    play music CoffeeShopMusic
    play sound CafeChatterAudio volume 0.5

    sc "Welcome to Normington Coffee."

    sc "Normington City's premiere high-end coffee shop."

    jump CoffeeMenu


label CoffeeMenu:
    sc "What can I get for you today?"
    menu:
        #add josephine second hangout request here
        #add coffee with friends here
<<<<<<< Updated upstream
=======
        "Get Coffee with Friends" if (day >= 3):
            call coffeeWithFriends
            jump mapScreen
>>>>>>> Stashed changes
        "One Coffee":
            if coffeeamount < 2:
                sc "Very good! That will be $15 please."
                menu:
                    "Okay!":
                        if money >= 15:
                            sc "One Normington coffee coming right up!"
                            $ money -= 15
                            play sound drinkpour
                            "You can hear coffee being poured in the background."
                            "Please enjoy."
                            $ coffeeamount += 1
                            $ energy += coffee
                            jump CoffeeMenu
                        else:
                            sc "I'm sorry. You do not have enough funds to purchase this coffee."
                            jump CoffeeMenu
                    "Nevermind.":
                        jump CoffeeMenu
            else:
                sc "I'm sorry, each customer is limited to two coffees per day. Please come back tomorrow if you wish to purchase more coffee."
                jump CoffeeMenu
        "You seem familiar...":
            sc "Oh me? You've probably seen my sibling at shifty shop."
            sc "Shifty shop sells low quality drinks like 'energy drinks', HA."
            sc "Normington Coffee sells premiere high-end LUXURY beverages like our famous 'Normington Coffee' to our esteemed guests."
            sc "Anyways, feel free to look around."
            jump CoffeeMenu
        #"Josephine's Second Hangout Request" if (day == 3)
        "That is all":
            jump testStart


                
