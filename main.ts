basic.forever(function () {
    while (input.buttonIsPressed(Button.B)) {
        if (input.buttonIsPressed(Button.A)) {
            basic.showNumber(randint(1, 6))
            basic.pause(1000)
            basic.showNumber(6)
            basic.pause(1000)
            basic.showNumber(7)
        } else {
            basic.showString("Stopp")
        }
    }
})
