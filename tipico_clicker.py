import pyautogui
import time
import keyboard

def get_position():
    print("Bewege den Mauszeiger über den Start/Spin-Button und drücke 'p' um die Position zu speichern")
    while True:
        if keyboard.is_pressed('p'):
            x, y = pyautogui.position()
            print(f"Position gespeichert")
            return x, y

def auto_clicker(x, y):
    print("Drücke 's' um den Auto-Clicker zu starten und drücke 'q' um zu beenden.")
    while True:
        if keyboard.is_pressed('s'):
            print("Auto-Clicker gestartet")
            while True:
                pyautogui.click(x, y)
                for _ in range(54):
                    if keyboard.is_pressed('q'):
                        print("Auto-Clicker gestoppt")
                        return
                    time.sleep(0.1)
        elif keyboard.is_pressed('q'):
            print("Programm beendet")
            break

if __name__ == "__main__":
    x, y = get_position()
    auto_clicker(x, y)
