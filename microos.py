from machine import Pin, PWM
import utime

led = Pin(2, Pin.OUT)
buzzer = PWM(Pin(15))  # бузер підключений до GPIO15

# --- Таблиця нот ---
NOTES = {
    "до": 261,
    "ре": 294,
    "мі": 329,
    "фа": 349,
    "соль": 392,
    "ля": 440,
    "сі": 494,
    "до2": 523
}

# --- Мелодії ---
melody1 = ["до", "ре", "мі", "фа", "соль", "ля", "сі", "до2"]
melody2 = ["до", "до", "соль", "соль", "ля", "ля", "соль"]
melody3 = ["мі", "мі", "фа", "соль", "соль", "фа", "мі", "ре", "до"]

jukebox = {
    1: melody1,
    2: melody2,
    3: melody3
}

def play_melody(melody, speed=0.4):
    for note in melody:
        if note not in NOTES:
            continue
        buzzer.freq(NOTES[note])
        buzzer.duty(512)
        utime.sleep(speed)
        buzzer.duty(0)
        utime.sleep(0.05)

def jukebox_menu():
    print("🎵 Jukebox 🎵")
    print("1: Гамма До-До")
    print("2: Twinkle Twinkle")
    print("3: Коротка мелодія")
    print("--------------------")
    choice = input("Оберіть мелодію (1-3): ").strip()
    if choice in ["1", "2", "3"]:
        print(f"▶ Відтворення мелодії {choice}...")
        play_melody(jukebox[int(choice)])
    else:
        print("❌ Невірний вибір!")

def main():
    print("MicroOS v1.1")
    print("Введіть 'help' щоб побачити команди.\n")

    while True:
        cmd = input(">>> ").strip().lower()

        if cmd == "help":
            print("Команди:")
            print("  help     - показати команди")
            print("  time     - показати час")
            print("  ledon    - увімкнути LED")
            print("  ledoff   - вимкнути LED")
            print("  clear    - очистити екран")
            print("  jukebox  - музичне меню 🎶")
            print("  exit     - вийти")

        elif cmd == "ledon":
            led.on()

        elif cmd == "ledoff":
            led.off()
    
        elif cmd == "time":
            t = utime.localtime()
            print("Час: {:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5]))

        elif cmd == "clear":
            print("\n" * 20)

        elif cmd == "jukebox":
            jukebox_menu()

        elif cmd == "exit":
            print("Вихід...")
            break

        elif cmd == "":
            continue

        else:
            print(f"Невідома команда: {cmd}")

if __name__ == "__main__":
    main()
