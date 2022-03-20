init offset = 0
default persistent.endingsCgOpen = False
default persistent.endingsDict = []

init python:
    class endingCg:
        allEndings = persistent.endingsDict
        def __init__(self,name,img):
            tmp = {"img":img,"name":name,"Open":False}
            if tmp not in endingCg.allEndings:
                endingCg.allEndings.append(tmp)
                persistent.endingsDict = endingCg.allEndings
                renpy.save_persistent()
            self.indOfThisCg = endingCg.allEndings.index(tmp)
        def open(self):
            endingCg.allEndings[self.indOfThisCg]["Open"] = True
            persistent.endingsDict = endingCg.allEndings
            persistent.endingsCgOpen = True
            renpy.save_persistent()


screen endings_achivment_meenu(title="Концовки", scroll=None, yinitial=0.0):
    tag menu
    style_prefix "game_menu"
    use game_menu(title):
            default cgPageNow = 0
            fixed:
                order_reverse True
                button:
                    style "page_label"
                    key_events True
                    xalign 0.5
                ## Таблица слотов.
                grid gui.gallary_slot_rows  gui.gallary_slot_rows:
                    style_prefix "slot"
                    xalign 0.5
                    yalign 0.5
                    spacing gui.slot_spacing
                    for i in range(gui.gallary_slot_cols * gui.gallary_slot_rows):
                        $ slot = i + 1
                        button:
                            has vbox
                            if len(persistent.endingsDict) > (i+(gui.gallary_slot_cols * gui.gallary_slot_rows * cgPageNow)):
                                if persistent.endingsDict[i+(gui.gallary_slot_cols * gui.gallary_slot_rows * cgPageNow)]["Open"]:
                                    add persistent.endingsDict[i+(gui.gallary_slot_cols * gui.gallary_slot_rows * cgPageNow)]["img"] fit "cover" xalign 0.5 
                                    text persistent.endingsDict[i+(gui.gallary_slot_cols * gui.gallary_slot_rows * cgPageNow)]["name"]
                                else:
                                    text "".join(["?" for x in persistent.endingsDict[i+(gui.gallary_slot_cols * gui.gallary_slot_rows * cgPageNow)]["name"]])
                ## Кнопки для доступа к другим страницам.
                hbox:
                    style_prefix "page"
                    xalign 0.5
                    yalign 1.0
                    spacing gui.page_spacing
                    textbutton _("<") action SetLocalVariable("cgPageNow", max(0,cgPageNow - 1))
                    for page in range(1,int(round(len(persistent.endingsDict)/ (gui.gallary_slot_cols * gui.gallary_slot_rows) ))+1):
                        textbutton "[page]" action SetLocalVariable("cgPageNow", page - 1)
                    textbutton _(">") action SetLocalVariable("cgPageNow",min(int(round(len(persistent.endingsDict)/ (gui.gallary_slot_cols * gui.gallary_slot_rows) )), cgPageNow))