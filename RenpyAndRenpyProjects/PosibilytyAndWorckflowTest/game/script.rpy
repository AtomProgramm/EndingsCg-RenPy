# Вы можете расположить сценарий своей игры в этом файле.
image bg empty = './images/whiteBg.jpg'
image bg noDoc = './images/bgInHunt.jpg'
image bg whithDoc = './images/bgHuntWichDoctors.jpg'
image bg birdsUp = './images/bgBirdsUp.jpg'
image bg psychoScope = './images/bgPsuchoScope.jpg'
image bg terapevtScope = './images/bgTerapevtScope.jpg'
image bg hirugScope = './images/bgHirugScope.jpg'

image ending terapevtEndingImage = "./images/endigTerapevt.jpg"
image ending psychoEndingImage = "./images/endigPsycho.jpg"
image ending tueEndingImage = "./images/endigTueEnding.jpg"


image side hirurg = './images/chHirurg.jpg'
image side psycho = './images/chPsycho.jpg'
image side terapevt = './images/ChTerapevt.jpg'
define ChHirurg = Character('Хирург', color="#ff3929")
define ChPsycho = Character('Психолог', color="#0faa0f")
define ChTerapevt = Character('Терапевт', color="#0f39f9")

define audio.bushTouch = "audio/Bush.mp3"
define audio.crackOfDuck = "audio/CrackVa.mp3"
define audio.shot = "audio/Shot.mp3"

label start:
    scene bg empty
    "Однажды в больнице, решили съездить на охоту."
    scene bg noDoc
    "За добычей в виде уток, поехали Терапевт, Психолог, Хирург и Патологоанатом."
    show bg whithDoc with dissolve
    "Стрелять они решили по очереди."
    "Первым был Терапевт."
    play sound bushTouch
    "Нашли."
    play sound crackOfDuck
    show bg birdsUp with Dissolve(1)
    "Терапевт прицелился."
    show bg terapevtScope with dissolve
    menu:
        "Произойдёт"
    
        "Путь оригинала":
            ChTerapevt "Так, вроде это утки."
            ChTerapevt "Вижу перья."
            ChTerapevt "А если это пингвин?"
            ChTerapevt "Ну это надо проверить где мы."
            ChTerapevt "Ну мы не в антарктиде."
            ChTerapevt "А если это, синичка? Не для синичек слишком большие"
            show bg whithDoc with dissolve
            ChTerapevt "Эх, улетели."
            "..."
            "*Гул* ну что ж такое, ну как так-то."
            jump trueWayPsychoOrder
    
        "Попал":
    
            pass
label terapevtEnding:
    pause 0.1
    play sound shot
    pause 0.2
    show bg whithDoc with dissolve
    ChTerapevt "Попал."
    pause 0.2
    $ persistent.endingsCgOpen = True
    $ persistent.endingsDict[0] = (persistent.endingsDict[0][0],persistent.endingsDict[0][1],True)
    show ending terapevtEndingImage with Fade(0.1, 0.0, 0.5, color="#fff")
    "Терапевт попал."
    "Концовка: Fast ending."
    pause 1
    return

label trueWayPsychoOrder:
    "Идут все ещё, идут, идут"
    play sound bushTouch
    "Нашли опять."
    play sound crackOfDuck
    show bg birdsUp with Dissolve(1)
    "Теперь очередь психолога."
    show bg psychoScope with dissolve
    menu:
        "Произойдёт"
    
        "Путь оригинала":
            ChPsycho "Так птица."
            ChPsycho "Родилась скорее всего в этом лесу."
            ChPsycho "Родители не известно где. Но скорее всго тоже утки."
            ChPsycho "Ну значит утка, или нет? Может она снаружи как утка а чуствует себя голубем."
            ChPsycho "Ну наверное всё равно всеми считается уткой."
            show bg whithDoc with dissolve
            ChPsycho "Эх, улетели."
            "..."
            "*Гул*Как так-то, эээх"
            jump trueWayHirurgOrder
    
        "Попал":
            jump psychoEnding
label psychoEnding:
    pause 0.1
    play sound shot
    pause 0.2
    show bg whithDoc with dissolve
    ChPsycho "Попал."
    pause 0.2
    $ persistent.endingsCgOpen = True
    $ persistent.endingsDict[1] = (persistent.endingsDict[1][0],persistent.endingsDict[1][1],True)
    show ending psychoEndingImage with Fade(0.1, 0.0, 0.5, color="#fff")
    "Психолог попал."
    "Концовка: Psycho ending."
    pause 1
    return

label trueWayHirurgOrder:
    "Идут, идут"
    play sound bushTouch
    play sound crackOfDuck
    show bg birdsUp with Dissolve(0.1)
    "Хирург вскинул ружьё."
    show bg bgHirugScope
    pause 0.1
    play sound shot
    pause 0.2
    show bg whithDoc with dissolve
    ChHirurg "Попал."
    pause 0.2
    ChHirurg "Эй, Патологоанатом. Глянь утка не утка."
    $ persistent.endingsCgOpen = True
    $ persistent.endingsDict[2] = (persistent.endingsDict[2][0],persistent.endingsDict[2][1],True)
    show ending tueEndingImage with Fade(0.1, 0.0, 0.5, color="#fff")
    "Настоящий конец анекдота."
    "Концовка: True ending."
    scene ending tueEndingImage
    pause 1
    return

