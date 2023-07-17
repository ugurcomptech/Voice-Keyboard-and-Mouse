import pygame
import tkinter as tk
from pynput import keyboard, mouse

def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def get_key_label_text(key):
    try:
        return f"Basmış olduğunuz tuş: {key.char}"
    except AttributeError:
        return f"Basmış olduğunuz tuş: {key}"

def get_mouse_button_label_text(button):
    return f"Basmış olduğunuz fare tuşu: {button.name}"

def on_press(key):
    if hasattr(key, 'char'):
        play_sound(sound_file)
    key_label.config(text=get_key_label_text(key))

def on_click(x, y, button, pressed):
    if pressed:
        play_sound(sound_file)
        mouse_button_label.config(text=get_mouse_button_label_text(button))

def close_program():
    root.quit()

def main():
    pygame.init()
    global sound_file, key_label, mouse_button_label, root
    sound_file = "kadir.wav"  # Ses dosyasının yolunu buraya girin

    # Tkinter GUI oluşturma
    root = tk.Tk()
    root.title("Klavye ve Mouse Ses Çalma")
    root.geometry("400x300")

    # Klavye önizlemesi için etiket
    key_label = tk.Label(root, text="Basmış olduğunuz tuş: ")
    key_label.pack(pady=10)

    # Fare tuşu önizlemesi için etiket
    mouse_button_label = tk.Label(root, text="Basmış olduğunuz fare tuşu: ")
    mouse_button_label.pack(pady=10)

    # Programı sonlandırmak için düğme
    close_button = tk.Button(root, text="Programı Sonlandır", command=close_program)
    close_button.pack(pady=10)

    # Pencere kapanırken programı sonlandır
    root.protocol("WM_DELETE_WINDOW", close_program)

    # Uğur tarafından yapılmıştır etiketi
    ugur_label = tk.Label(root, text="Uğur tarafından yapılmıştır")
    ugur_label.pack(side="bottom", pady=10)

    # Klavye ve fare olaylarını dinleme
    with keyboard.Listener(on_press=on_press) as key_listener:
        with mouse.Listener(on_click=on_click) as mouse_listener:
            # Tkinter ana döngüsünü çalıştırma
            root.mainloop()

            # Program sonlandığında dinleyicileri durdurma
            key_listener.stop()
            mouse_listener.stop()

if __name__ == '__main__':
    main()
