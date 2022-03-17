default persistent.endingsCgOpen = False
default persistent.endingsDict = [("endigTerapevt.jpg","Fast ending",False),
                                  ("endigPsycho.jpg","Psycho ending",False),
                                  ("endigTueEnding.jpg","True ending",False)]


screen endings_achivment_meenu(title="Концовки", scroll=None, yinitial=0.0):

    tag menu

    use game_menu(title):
            default cgPageNow = 0

            fixed:

                ## Это гарантирует, что ввод будет принимать enter перед остальными
                ## кнопками.
                order_reverse True

                ## Номер страницы, который может быть изменён посредством клика на
                ## кнопку.
                button:
                    style "page_label"

                    key_events True
                    xalign 0.5
                    # action page_name_value.Toggle()

                    # input:
                    #     style "page_label_text"
                    #     value page_name_value

                ## Таблица слотов.
                grid gui.gallary_slot_rows  gui.gallary_slot_rows:
                    style_prefix "slot"

                    xalign 0.5
                    yalign 0.5

                    spacing gui.slot_spacing

                    for i in range(gui.gallary_slot_cols * gui.gallary_slot_rows):

                        $ slot = i + 1

                        button:
                            # action FileAction(slot)

                            has vbox

                            if  len(persistent.endingsDict) > (i+(gui.gallary_slot_cols * gui.gallary_slot_rows * cgPageNow)):
                                if persistent.endingsDict[i+(gui.gallary_slot_cols * gui.gallary_slot_rows * cgPageNow)][2]:
                                    add persistent.endingsDict[i+(gui.gallary_slot_cols * gui.gallary_slot_rows * cgPageNow)][0] xalign 0.5 zoom .2
                                    text persistent.endingsDict[i+(gui.gallary_slot_cols * gui.gallary_slot_rows * cgPageNow)][1]
                                else:
                                    text "".join(["?" for x in persistent.endingsDict[i+(gui.gallary_slot_cols * gui.gallary_slot_rows * cgPageNow)][1]])

                           # key "save_delete" action FileDelete(slot)

                ## Кнопки для доступа к другим страницам.
                hbox:
                    style_prefix "page"

                    xalign 0.5
                    yalign 1.0

                    spacing gui.page_spacing

                    textbutton _("<") action SetLocalVariable("cgPageNow", max(0,cgPageNow - 1))

                    for page in range(1,int(round(len(persistent.endingsDict)/ (gui.gallary_slot_cols * gui.gallary_slot_rows) ))+2):
                    # for page in range(1,2):
                        textbutton "[page]" action SetLocalVariable("cgPageNow", page - 1)

                    textbutton _(">") action SetLocalVariable("cgPageNow",min(int(round(len(persistent.endingsDict)/ (gui.gallary_slot_cols * gui.gallary_slot_rows) )), cgPageNow + 1))
