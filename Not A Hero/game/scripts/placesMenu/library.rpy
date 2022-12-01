label lib:
    scene normingtonLibrary
    "As Ellis enters the library, the smells of cedar and academia immediately fills his lungs, taking him back to his middle school days."
    jump choicesLib

label choicesLib:
    if day<3:
        call volunteeringLib
        return
    else:
        menu:
            "Volunteer at the Library":
                call volunteeringLib
            "Read a book":
                call readBook
        return
    return