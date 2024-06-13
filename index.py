import tkinter as tk
from tkinter import filedialog

class todolistApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("400x400")
        self.title("TO DO LIST")
        self.configure(bg="red")
        self.create_widget()
        
    def create_widget(self):
        self.task_input=tk.Entry(self,width=30)
        self.task_input.pack(pady=10)
        
        self.add_task_butn=tk.Button(self,text="ADD TASK",bg="yellow",command=self.add_task)
        self.add_task_butn.pack(pady=5)
        
        self.task_lb=tk.Listbox(self,selectmode=tk.SINGLE)
        self.task_lb.pack(pady=5)
        
        self.butn_frame=tk.Frame(self,bg="red")
        self.butn_frame.pack(pady=5)
        
        self.edit_butn=tk.Button(self.butn_frame,text="EDIT TASK",bg="yellow",command=self.edit_task)
        self.edit_butn.grid(row=0,column=0,padx=5)
        
        self.delete_butn=tk.Button(self.butn_frame,text="DELETE TASK",bg="yellow",command=self.delete_task)
        self.delete_butn.grid(row=0,column=1,padx=5)
        
        self.save_butn=tk.Button(self,text="SAVE",bg="yellow",command=self.save_task)
        self.save_butn.pack(pady=5)
        
        self.load_butn=tk.Button(self,text="LOAD",bg="yellow",command=self.load_task)
        self.load_butn.pack(pady=5)
        
    def add_task(self):
        task=self.task_input.get()
        if task:
            self.task_lb.insert(tk.END,task)
            self.task_input.delete(0,tk.END)
    
    def edit_task(self):
        task_index=self.task_lb.curselection()
        if task_index:
            new_task=self.task_input.get()
            if new_task:
                self.task_lb.delete(task_index)
                self.task_lb.insert(task_index,new_task)
    def delete_task(self):
        task_index=self.task_lb.curselection()
        if task_index:
            self.task_lb.delete(task_index)
            
    def save_task(self):
        tasks=self.task_lb.get(0,tk.END)
        file_path=filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path,'w') as file:
                for task in tasks:
                    file.write(task+"\n")
                    
    def load_task(self):
        file_path=filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        
        if file_path:
            with open(file_path,'r') as file:
                tasks=[line.strip() for line in file.readlines()]
                self.task_lb.delete(0,tk.END)
                
                for task in tasks:
                    self.task_lb.insert(tk.END,task)
app=todolistApp()

app.mainloop()