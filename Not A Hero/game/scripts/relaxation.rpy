default restLines=["(Ellis relaxes in his apartment.)","(Ellis takes some time off in his apartment.)","(Ellis lounges around in his apartment.)"]
default bookLines=["(Ellis starts a new book. It's about a reluctant hero.)","(Ellis starts a new book. The storyline follows a cast of characters that get into fun shenanigans.)","(Ellis starts a new book. In it, the protagonist is a raccoon pretending to be a man.)"]
default walkLines=["(Ellis goes for a leisurely stroll around the block.)","(Ellis walks down to the park and back.)","(Ellis ambles along to the bus stop, turns around, and heads home.)"]
default restEndLines=["Ellis calmed down.","Ellis felt more relaxed.","Ellis felt better."]


label rest:
    $ restLine = renpy.random.choice(restLines)
    $ restEndLine = renpy.random.choice(restEndLines)
    "[restLine]"
    "([restEndLine] -1 stress.)"

    $ stress -= 1
    return

label readBook:
    $ bookLine = renpy.random.choice(bookLines)
    $ restEndLine = renpy.random.choice(restEndLines)
    "[bookLine]"

    if bookLine == bookLines[0]:
        "(That's pretty meta.)"
    elif bookLine == bookLines[1]:
        "(Hits close to home.)"
    else:
        "(Sounds familiar.)"

    "([restEndLine] -2 stress.)"

    $ stress -= 2
    return

label takeWalk:
    $ walkLine = renpy.random.choice(walkLines)
    $ restEndLine = renpy.random.choice(restEndLines)
    "[walkLine]"

    "([restEndLine] -3 stress.)"

    $ stress -= 3
    return