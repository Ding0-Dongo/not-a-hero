### going to try and figure out the tutorial here.

### this might take a bit while I figure out renpy.

label tutorial:

    scene bg room

    "Howdy there."

    "If you're seeing this then this is where the tutorial goes."

    "If not then... uh....."

    "Uh oh."

    show screen StatUI

    "Hopefully you should see some sort of stat UI"

    ". . ."

    $ energy -= 3

    "Get energy drained"

    "See that?"

    $ stress += 1

    "Now become stressed"

    "Back to day one."

    jump testStart