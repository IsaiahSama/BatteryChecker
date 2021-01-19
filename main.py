from win10toast import ToastNotifier
from psutil import sensors_battery
from time import sleep
class Main:
    
    def __init__(self) -> None:
        self.notif = ToastNotifier()
    
    def main(self):
        battery = sensors_battery()
        if battery.power_plugged:
            print("Battery Charging")
            if battery.percent >= 80:
                self.notif.show_toast(title="Battery Checker", msg=f"You're battery is at {battery.percent}%. I recommend unplugging now", duration=30)

        if not battery.power_plugged:
            print("Battery is Not Charging")
            if battery.percent <= 40:
                self.notif.show_toast("Battery Checker", f"Your battery is at {battery.percent}%. I recommend charging now", duration=30)

        sleep(60)

main = Main()

print("Press ctrl + c at any time to quit")

while True:
    try:
        main.main()
    except KeyboardInterrupt:
        print("Hope you enjoyed. Bye bye now. Press enter to leave")
        input()
        raise SystemExit