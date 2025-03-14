basic.show_leds("""
    . . # . .
    . . # . .
    # # # # #
    . . # . .
    . . # . .
    """)
basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    """)
basic.pause(1000)

def on_forever():
    while input.button_is_pressed(Button.B):
        if input.button_is_pressed(Button.A):
            basic.show_number(randint(1, 6))
            basic.pause(1000)
            basic.show_number(6)
            basic.pause(1000)
            basic.show_number(7)
        else:
            basic.show_string("Stopp")
basic.forever(on_forever)
