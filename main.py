  self.window = tk.Tk() 

    # Title of the window 
    self.window.title("Calculator") 

    # StringVar() is the variable  
    # class of tkinter 
    self.string = tk.StringVar() 

    # Frame for the Textbox 
    self.frame = tk.Frame(self.window) 

    # Inserting the entry 
    self.textf = tk.Entry(self.frame,  
                          textvariable = self.string) 
    self.textf.grid(row = 0, column = 0) 
    self.frame.pack() 

    # Create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed. 
    self.butt1 = tk.Button(self.window, text = "1", 
                           command = lambda: self.ins("1")) 
    self.butt1.grid(row = 2, column = 0) 

    self.butt2 = tk.Button(self.window, text = "2", 
                           command = lambda: self.ins("2")) 
    self.butt2.grid(row = 2, column = 1) 

    self.butt3 = tk.Button(self.window, text = "3", 
                           command = lambda: self.ins("3")) 
    self.butt3.grid(row = 2, column = 2) 

    self.butt4 = tk.Button(self.window, text = "4", 
                           command = lambda: self.ins("4")) 
    self.butt4.grid(row = 3,