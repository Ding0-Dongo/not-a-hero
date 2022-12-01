label elementary:
    scene normingtonElementary
    "Ellis hears the shrills and fun-filled shrieks of the kids, running and laughing about."
    jump choicesElementary

label choicesElementary:
    if day<5:
        return
    else:
        call mediation
        return