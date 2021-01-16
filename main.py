from win10toast import ToastNotifier
from psutil import sensors_battery

class Main:
    
    def __init__(self) -> None:
        self.notif = ToastNotifier()
    
    def main(self):
        battery = sensors_battery()
        while battery.power_plugged:
            if battery.percent >= 80:
                self.notif.show_toast(title="Battery Checker", msg="You're battery is at {battery.percent}. I recommend unplugging now", duration=30)
        
        while not battery.power_plugged:
            if battery.percent <= 40:
                self.notif.show_toast("Battery Checker", "Your battery is at {battery.percent}. I recommend charging now", duration=30)


main = Main()

while True:
    try:
        print("Press ctrl + c at any time to quit")
        main.main()
    except KeyboardInterrupt:
        print("Hope you enjoyed. Bye bye now. Press enter to leave")
        input()