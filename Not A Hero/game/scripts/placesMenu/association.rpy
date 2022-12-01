label association:
    if day<6:
        call socialize
        return
    else:
        menu:
            "Talk Things Out":
                call talkThingsOut
            "Socialize":
                call socialize
        return