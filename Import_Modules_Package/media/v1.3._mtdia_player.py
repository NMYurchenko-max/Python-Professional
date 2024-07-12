import vlc
import tkinter as tk
from tkinter import (
    Frame, Canvas, BOTH, Button, Entry, Toplevel, Listbox)
from pathlib import Path
from PIL import Image, ImageTk

# Определяем абсолютный путь к корню проекта
project_root = Path('D:/Python Professional_git').resolve()
# Определяем путь к директории 'media' относительно корня проекта
media_path = project_root / 'Import_Modules_Package/media'

# Получаем список всех файлов в директории 'media'
file_names = [x for x in media_path.iterdir() if x.is_file()]


class App(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.canvas = Canvas(self.parent, bg='black')
        self.canvas.pack(fill=BOTH, expand=True)
        self.player = None
        self.media_path = ""
        self.is_video_mode = True
        self.init_ui()
        self.load_image()

    def init_ui(self):
        self.entry_path = Entry(self, width=50)
        self.entry_path.pack(fill=tk.X, padx=10, pady=10)
        button_play = Button(self, text="Play", command=self.play_media)
        button_play.pack(pady=5)
        button_switch_mode = Button(
            self, text="Switch Mode", command=self.switch_mode)
        button_switch_mode.pack(pady=5)
        button_browse = Button(self, text="Browse", command=self.browse_file)
        button_browse.pack(pady=5)

    def load_image(self):
        image_path = media_path / 'image.jpg'
        try:
            jpg = Image.open(image_path)
            self.photo_jmage = ImageTk.PhotoImage(jpg)
            self.canvas.create_image(
                0, 0, anchor=tk.NW, image=self.photo_jmage)
            self.update_idletasks()
            print("Image loaded successfully")  # Для отладки
        except Exception as e:
            print(f"Failed to load image: {e}")  # Для отладки
           
    def browse_file(self):
        top = Toplevel(self)
        top.title("Выберите файл")
        listbox = Listbox(top)
        listbox.pack()
        for file in file_names:
            listbox.insert(tk.END, file.name)
        listbox.bind('<<ListboxSelect>>', self.on_select)
        listbox.activate(listbox.nearest(0))
        top.mainloop()

    def on_select(self, event):
        selected_file = event.widget.get(event.widget.curselection())
        self.media_path = str(media_path / selected_file)
        print(f"Selected file: {self.media_path}")
        self.play_media()

    def play_media(self):
        if not self.media_path.strip():
            print("No media path provided. Opening file dialog...")
            self.browse_file()
            return
        if self.player is not None:
            self.player.stop()
        instance = vlc.Instance()
        self.player = instance.media_player_new()
        if self.is_video_mode:
            self.player.set_hwnd(self.canvas.winfo_id())
        else:
            self.player.set_fullscreen(True)
        media = instance.media_new(self.media_path)
        self.player.set_media(media)
        self.player.play()
        print(f"Playing {self.media_path}")

    def switch_mode(self):
        self.is_video_mode = not self.is_video_mode
        print(f"Switched to {'video' if self.is_video_mode else 'audio'} mode")
        if self.player is not None:
            if self.is_video_mode:
                self.player.set_fullscreen(False)
            else:
                self.player.set_fullscreen(True)
            self.player.set_mrl(self.media_path)
            self.player.play()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.pack(fill=BOTH, expand=True)
    root.mainloop()
