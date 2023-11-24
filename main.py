Toucher = crickit.signal3.analog_read()
pause(200)
crickit.servo1.set_angle(90)

def on_forever():
    console.log_value("touch", Toucher)
    pause(5000)
    if Toucher < 700:
        crickit.servo1.set_angle(0)
    else:
        crickit.servo1.set_angle(180)
forever(on_forever)

def on_forever2():
    console.log_value("touch", Toucher)
    pause(200)
forever(on_forever2)
