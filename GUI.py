from main import *
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("581x358+419+131")
        top.minsize(120, 1)
        top.maxsize(2394, 749)
        top.resizable(1, 1)
        top.title("Port Scanner")
        top.configure(background="#d9d9d9")

        #Scan Button
        self.Button1 = ttk.Button(top, command=lambda: self.startscan())
        self.Button1.place(relx=0.034, rely=0.028, height=54, width=137)
        self.Button1.configure(takefocus="")
        # self.Button1 .configure(cursor="fleur")
        self.Button1.configure(text='''Scan''')
        #Cancel Button
        self.Button2 = ttk.Button(top, command=lambda: self.cancel_btn())
        self.Button2.place(relx=0.293, rely=0.028, height=54, width=77)
        self.Button2.configure(takefocus="")
        # self.Button2.configure(cursor="fleur")
        self.Button2.configure(text='''Cancel''')
        #Host Entry
        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.138, rely=0.223,height=20, relwidth=0.282)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.034, rely=0.223, height=21, width=31)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Host''')
        
        self.vsb = tk.Scrollbar(orient="vertical", command=self.OnVsb)

        #Port list
        self.Listbox1 = tk.Listbox(top, yscrollcommand=self.vsb.set)
        self.Listbox1.place(relx=0.017, rely=0.391, relheight=0.592
                , relwidth=0.454)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        #Status list
        self.Listbox1_1 = tk.Listbox(top, yscrollcommand=self.vsb.set)
        self.Listbox1_1.place(relx=0.465, rely=0.391, relheight=0.592
                , relwidth=0.472)
        self.Listbox1_1.configure(background="white")
        self.Listbox1_1.configure(disabledforeground="#a3a3a3")
        self.Listbox1_1.configure(font="TkFixedFont")
        self.Listbox1_1.configure(foreground="#000000")
        self.Listbox1_1.configure(highlightbackground="#d9d9d9")
        self.Listbox1_1.configure(highlightcolor="black")
        self.Listbox1_1.configure(selectbackground="#c4c4c4")
        self.Listbox1_1.configure(selectforeground="black")
        self.vsb.pack(side="right",fill="y")
        self.Listbox1.bind("<MouseWheel>", self.OnMouseWheel)
        self.Listbox1_1.bind("<MouseWheel>", self.OnMouseWheel)

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.706, rely=0.300, relheight=0.07
                , relwidth=0.300)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(width=74)

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.499, rely=0.300, height=21, width=76)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Time Elapsed''')



        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.482, rely=0.028, relheight=0.209
                , relwidth=0.465)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Port Range''')
        self.Labelframe1.configure(background="#d9d9d9")

        self.Entry2 = tk.Entry(self.Labelframe1)
        self.Entry2.place(relx=0.037, rely=0.533, height=20, relwidth=0.348
                , bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Entry2_1 = tk.Entry(self.Labelframe1)
        self.Entry2_1.place(relx=0.556, rely=0.533, height=20, relwidth=0.348
                , bordermode='ignore')
        self.Entry2_1.configure(background="white")
        self.Entry2_1.configure(disabledforeground="#a3a3a3")
        self.Entry2_1.configure(font="TkFixedFont")
        self.Entry2_1.configure(foreground="#000000")
        self.Entry2_1.configure(highlightbackground="#d9d9d9")
        self.Entry2_1.configure(highlightcolor="black")
        self.Entry2_1.configure(insertbackground="black")
        self.Entry2_1.configure(selectbackground="#c4c4c4")
        self.Entry2_1.configure(selectforeground="black")

        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(relx=0.037, rely=0.260, height=21, width=34
                , bordermode='ignore')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''From:''')

        self.Label2_2 = tk.Label(self.Labelframe1)
        self.Label2_2.place(relx=0.556, rely=0.260, height=21, width=34
                , bordermode='ignore')
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#d9d9d9")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''To:''')

    #Get host from Entry
    def gethost(self):
        self.hostname = self.Entry1.get()
        self.Rfrom = self.Entry2.get()
        self.Rto = self.Entry2_1.get()
        return self.hostname, self.Rfrom, self.Rto 
    #Start scan button action
    def startscan(self):
        self.gh = self.gethost()
        self.scanner = Scanner(self.gh[0], self.gh[1],self.gh[2])
        self.results = self.scanner.scan()
        #Change Time Elapsed Text to total time
        self.Message1.configure(text=self.results[0])
        for x,y in self.results[1].items():
            self.Listbox1.insert(tk.END, x)
            self.Listbox1_1.insert(tk.END, y)
    def cancel_btn(self):
        sys.exit()

    def OnVsb(self, *args):
        self.Listbox1.yview(*args)
        self.Listbox1_1.yview(*args)

    def OnMouseWheel(self, event):
        self.Listbox1.yview("scroll", event.delta,"units")
        self.Listbox1_1.yview("scroll",event.delta,"units")
        return ("break")



if __name__ == '__main__':
    vp_start_gui()





