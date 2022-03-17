# default persistent.endingsCgOpen = False
# default persistent.endingsDict = [("0","gnou",False),
#                                   ("1","gla",False),
#                                   ("2","pa1",False),
#                                   ("3","pa2",False),
#                                   ("4","gh",False),
#                                   ("5","sol",False),
#                                   ("6","mir",False),
#                                   ("7","fac",False),
#                                   ("8","fi",False),
#                                   ("9","buc",False)]
# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#0007FF")
define ee = Character('Нилэй', color="#FF0096")

label start:

    scene bg room

    show eileen happy with dissolve

    e "Ну я эйлин"

    ee "А я... Нилэй? чё за Странное имя?"

    show eileen happy at left with dissolve

    e "Это эйлин но перевёрнутое. И с большой буквы"

    ee "А я... Нилэй? чё за Странное имя?"

    menu:
        "Прям совсем":
            jump w1
        "Очень":
            jump w2
    return

label w1:

    $ persistent.endingsCgOpen = True
    $ persistent.endingsDict[3] = (persistent.endingsDict[3][0],persistent.endingsDict[3][1],True)

    e "Eue"
    
    return

label w2:
    $ persistent.endingsCgOpen = True
    $ persistent.endingsDict[5] = (persistent.endingsDict[5][0],persistent.endingsDict[5][1],True)

    ee "...Мдааааа..."
    
    return