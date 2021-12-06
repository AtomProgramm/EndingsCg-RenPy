# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#0007FF")
define ee = Character('Нилэй', color="#FF0096")

label start:

    scene bg room

    show eileen happy with dissolve

    e "Ну я эйлин"

    ee "А я... Нилэй? чё за Уебанское имя?"

    show eileen happy at left with dissolve

    e "Это эйлин но перевёрнутое. И с большой буквы"

    ee "А я... Нилэй? чё за Уебанское имя?"

    menu:
        "Заебись":
            jump w1
        "Очень":
            jump w2
    return

label w1:

    e "Eue"
    
    return

label w2:

    ee "...Мдааааа..."
    
    return