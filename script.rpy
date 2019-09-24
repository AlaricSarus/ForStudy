


#    $ xp += 90
#    if xp>=100:
#        call screen level_up

#define eil = Character("Eileen")
define miy = Character("Asakura Miyuki")
define min = Character("Asakura Minori")

label start:

    $ level = 0
    $ next_level = level + 1
    $ xp = 0

    stop music fadeout 1
    with Pause(3)
    scene bg010c1 with dissolve
    "{k=-.5}Отрицательный{/k} Нормальный {k=.5}Положительный{/k}"
    miy "Hi` fellows"
    show screen simple_screen with dissolve
    miy "Привет йоба-кун"
    "Text"
    "пробуев добавить опіта"
    "ше опита добавить"
    return
