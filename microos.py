from machine import Pin
import utime

led = Pin(2, Pin.OUT)

def main():
    print("PyShell OS v0.1")
    print("Введіть 'help' щоб побачити команди.\n")

    while True:
        cmd = input(">>> ").strip().lower()

        if cmd == "help":
            print("Команди:")
            print("  help   - показати команди")
            print("  time   - показати час")
            print("  ledon  - увімкнути LED")
            print("  ledoff - вимкнути LED")
            print("  clear  - очистити екран")
            print("  exit   - вийти")

        elif cmd == "ledon":
            led.on()
            print("LED увімкнено")

        elif cmd == "ledoff":
            led.off()
            print("LED вимкнено")

        elif cmd == "time":
            t = utime.localtime()
            print("Час: {:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5]))

        elif cmd == "clear":
            print("\n" * 20)

        elif cmd == "exit":
            print("Вихід...")
            break

        elif cmd == "":
            continue

        else:
            print(f"Невідома команда: {cmd}")

if __name__ == "__main__":
    main()
