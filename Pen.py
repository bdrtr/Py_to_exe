from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os, time

class Base(tk.Tk):
    def __init__(self):
        super().__init__()
        self.base_settings()


    def base_settings(self):
        self.title('Py to Exe')
        self.geometry('200x300')


class Main_Win(ttk.Frame):
    def __init__ (self, container, options = {'padx':5, 'pady':5}, font='Helvetica', size=14):
        
        super().__init__(container)
        self.container = container
        self.options = options
        self.set_comp()
        self.pack(fill='both')
        self.path = None

    def find_selection(self):
        self.path = str(filedialog.askopenfilename())
        
        if self.path.endswith('.py'):
            self.label1.configure(text=f'yol: '+self.path)
            self.update()
            self.start_py_to_exe()

    def set_comp(self):
        self.label1 = ttk.Label(text='exe ye çevrilcek dosyayi seciniz. ')
        self.label1.pack(anchor='center',**self.options)

        self.but1 = ttk.Button(text='dosya sec', command=self.find_selection)
        self.but1.pack(anchor='s', **self.options)

        self.but2 = ttk.Button(text='kapat',command=self.ext)
        self.but2.pack(anchor='s', **self.options)

    def start_py_to_exe(self):
        try:
            os.system("echo 'islem basliyo...'")
            time.sleep(1)
            os.system(f'pyinstaller {self.path}')
        except OSError as e:
            self.label1.configure(text='error'+e)
            exit(0)

        self.label1.configure(text='basarili bir sekilde exe olusuturuldu')
        self.update()



    def ext(self):
        self.container.destroy()
            

if __name__ == '__main__':
    base_app = Base()
    app = Main_Win(base_app)
    app.mainloop()

