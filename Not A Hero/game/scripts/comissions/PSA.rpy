label psa:
    if energy < 2:
        "Ellis is too tired to do that right now."
        return
    else:
        scene plaza with fade

        show ellisNeutral at ellis_std:
            xalign 0.2
        show joClosed at jo_std:
            xalign 0.8
        
        "(Josephine and Ellis spend a few hours teaching the importance and basics of first aid.)"
        "(For their efforts, the commission awards each of them $10.)"

        show blackScreen with fade

        $ money += 10
        $ energy -= 2

        return