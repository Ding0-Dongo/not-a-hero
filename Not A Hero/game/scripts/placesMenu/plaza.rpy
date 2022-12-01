label plaza:
    scene normingtonPlaza
    "Ellis sees some cool boards."
    jump choicesPlaza

label choicesPlaza:
    if day<3:
        return
    else if day<4:
        menu:
            "Fundraising":
                call fundraising
                return
    else:
        menu:
            "Fundraising":
                call fundraising
                return
            "Josephine's First Aid Lesson"
                call josephineFirstAid
                return
            "PSA"
                call psaTeam
                return
        return