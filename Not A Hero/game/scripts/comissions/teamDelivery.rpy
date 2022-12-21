label teamDeliveryComm:
    if energy < 2:
        "Ellis is too tired to do that right now."
        return
    else:
        scene plaza with fade

        show desChuckle at ellis_std with dissolve:
            xalign 0.8
        show ellisHappy at ellis_std with dissolve:
            xalign 0.2
        "(Ellis and Desmond spend a good while delivering packages. It's tiring, but rewarding work.)"
        "(For his efforts, Ellis gains $10 from the association.)"

        show blackScreen with fade

        $ money += 10
        $ energy -= 2
        $ social += 1
        return