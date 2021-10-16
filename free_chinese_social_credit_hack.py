import tkinter as tk
import time

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.frame = tk.Frame(self)
        self.frame.pack(side="top", fill = "both", expand=True)

        self.label = tk.Label(self, text = "press start to get 100000 social credit")
        button1 = tk.Button(self, text = "Start",
                                  command = self.do_something)
        self.label.pack(in_=self.frame)
        button1.pack(in_=self.frame)

    def do_something(self):
        self.label.config(text = "getting social credit...")
        self.label.update_idletasks()
        time.sleep(2)
        self.label.config(text = "installing social credit...")
        self.label.update_idletasks()
        time.sleep(2)
    
        self.label.config(text = "social credit installed successfully.")

def main():
    app = SampleApp()
    app.title('Chinese social credit hacker REV 1.0')
    app.geometry('400x100')
    app.mainloop()

    return 0
    
if __name__ == '__main__':
    main()