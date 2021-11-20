
import tkinter as tk

from sidebar import SideBar
from main_app import MainApp
from messenger import messenger

from constants import WINDOW_HEIGHT,WINDOW_WIDTH, BAR_WIDTH, MESSENGER_CLOCK

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.main_app = MainApp(self,height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
        self.main_app.grid(column=0, row=0)

        self.sidebar = SideBar(self,height=WINDOW_HEIGHT, width=BAR_WIDTH,bg='yellow')
        self.sidebar.grid(column=1,row=0)

    def messenger_wrapper(self):
        msg = messenger.recv()

        if msg['target'] == 'main_app':
            target = self.main_app
        elif msg['target'] == 'sidebar':
            target = self.sidebar
        else:
            target = None

        if target:
            # Execute message
            final_cmd = f'target.{msg["cmd"]}'

            #print(final_cmd)
            eval(final_cmd)

        # Infinitely check for this function
        self.after(MESSENGER_CLOCK, self.messenger_wrapper)


if __name__ == '__main__':
    root = Application()
    root.title("Simulasi Turunan Benzena")

    root.after(0, root.messenger_wrapper)
    root.mainloop()
