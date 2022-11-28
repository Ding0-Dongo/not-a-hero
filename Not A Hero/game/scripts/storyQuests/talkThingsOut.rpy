# requires josephine's apology to be completed first!

label talkThingsOut:
    # black screen (i don't know how to do this AAA)
    show blackScreen
    "(After a lot of deliberation, Ellis makes up his mind to go talk to Desmond.)"
    "(It takes him a while, but after a bit of nervously asking around, he finds where Desmond is.)"
    "(Seems like Desmond has been pretty busy all of yesterday and today... but he agreed to meet in the park for a while.)"
    # scene park
    scene plaza with fade # totally a park

    "(Ellis gets there first. He nervously waits in the park by the fountain.)"
    "(A couple other people are walking around in the park too, passing him by.)"
    e "(... I kinda wish I wasn't just standing around here by myself. It feels so awkward...)"
    d "Ellis, there you are. You wanted to talk about something?"
    e "*quickly turns around* Oh-! Desmond, yeah, I... I did."
    "(He notices Desmond looks more tired than usual.)"
    e "Um... you alright?"
    d "Huh?"
    e "It's just... you look like you didn't sleep well?"
    d "*waves a hand dismissively* Ellis, I'm busy. If you want to talk to me, make it quick."
    e "Right... sorry. I just... wanted to talk about yesterday. At... at the café."
    d "*brow furrows* ...what about it?"
    "(Before Ellis can speak, Desmond continues.)"
    d "It's fine if you don't want to do the commission. Josephine already talked to me about it. We won't make you join us."
    e "No, I- please, let me explain. I just... I panicked yesterday. I should have... should have talked to you guys instead of just running away."
    d "Well, you're talking to us now. Water under the bridge."
    e "I want to join you guys, really, but... I'm just not ready yet. Maybe- maybe another week."
    d "*folds his arms* It's only one week, but I guess we could always do a different one next month."
    e "Oh, I... I'm sorry... (I'm going to delay his initiation as a full-fledged hero...)"
    e "(... I feel terrible. I might be sick.)"
    d "(nonchalant) It's whatever. *shrugs*"
    d "Was that all we had to talk about? If we're done here, I have to get back to my commissions."
    "(Ellis can only manage a nod in response. Desmond turns to leave.)"
    e "Desmond, you... you really throw yourself into your work when you're stressed, huh...?"
    d "..."
    d "I'll see you later, Ellis."
    "(Desmond leaves.)"
    e "(I thought talking things out would make me feel better... so why do I feel so awful?)"
    # fade to black
    show blackScreen with fade
    "(Ellis was stressed out by the encounter. +2 stress)"
    $ stress += 2
