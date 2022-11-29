label association:
    if day==1:
        if story1Done == False:
            menu:
                "Meet Your TEAM":
                    call meetTheTeam
                "Socialize":
                    call socialize
            return
        else:
            call socialize
            return
    elif day<6:
        call socialize
        return
    else:
        menu:
            "Talk Things Out":
                call talkThingsOut
            "Socialize":
                call socialize
        return