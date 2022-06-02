import tkinter as tk
from tkinter import ttk
import trafo

class InputGui:

    def __init__(self):
                
        root = tk.Tk()
        self.gp = []
        self.lp = []
        self.is_axis_selected = [tk.BooleanVar(value=True) for _ in range(7)]

        # Config rows
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)
        root.rowconfigure(3, weight=1)
        root.rowconfigure(4, weight=1)
        root.rowconfigure(5, weight=1)
        root.rowconfigure(6, weight=1)
        root.rowconfigure(7, weight=1)
        root.rowconfigure(8, weight=1)
        root.rowconfigure(9, weight=1)
        root.rowconfigure(10, weight=1)

        # Config columns
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        root.columnconfigure(3, weight=1)
        root.columnconfigure(4, weight=1)
        root.columnconfigure(5, weight=1)
        root.columnconfigure(6, weight=1)

        # Grabber point properties
        self.create_labeled_entry(root, 0, 0, "Grabber point", columnspan=6, is_entry=False)
        self.gp.append(self.create_labeled_entry(root, 1, 0, "x"))
        self.gp.append(self.create_labeled_entry(root, 2, 0, "y"))
        self.gp.append(self.create_labeled_entry(root, 3, 0, "z"))

        self.gp.append(self.create_labeled_entry(root, 1, 2, "o"))
        self.gp.append(self.create_labeled_entry(root, 2, 2, "a"))
        self.gp.append(self.create_labeled_entry(root, 3, 2, "t"))

        self.gp.append(self.create_labeled_entry(root, 1, 4, "gv"))

        # Laser point properties
        self.create_labeled_entry(root, 4, 0, "Laser point",columnspan=6, is_entry=False)
        self.lp.append(self.create_labeled_entry(root, 5, 0, "x"))
        self.lp.append(self.create_labeled_entry(root, 6, 0, "y"))
        self.lp.append(self.create_labeled_entry(root, 7, 0, "z"))

        self.lp.append(self.create_labeled_entry(root, 5, 4, "lf"))

        axis_checkbutton_list = [ttk.Checkbutton(root, text=(_+1), variable=self.is_axis_selected[_], onvalue=True, offvalue=False) for _ in range(7)]
        
        index = 0
        for axis_checkbutton in axis_checkbutton_list:
            axis_checkbutton.grid(row=9, column=index)
            index += 1

        """
        for i in range(7):
            self.cb_list.append(tk.Checkbutton(root, text=str(i+1))) 
            self.cb_list[i].grid(row=9, column=i, sticky='nsew')
        """
        # Calculation button
        calculate_btn = ttk.Button(root, text="Calculate", command=self.calculation)
        calculate_btn.grid(row=10, column=0, columnspan=7, sticky='nsew')


        root.mainloop()

    def create_labeled_entry(self, root, row, column, name, columnspan=1, rowspan=1, is_entry = True):
        label = tk.Label(root, text=str(name))
        label.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky='nsew')
        if is_entry:
            entry = tk.Entry(root)
            entry.grid(row=row, column=column+columnspan, sticky='nsew')
            entry.insert(tk.END, '0.0')
            return entry

    def calculation(self):
        grabble_data = []
        laser_data = []
        selected_list = []
        for entry in self.gp:
            grabble_data.append(entry.get())

        for entry in self.lp:
            laser_data.append(entry.get())

        for selected in self.is_axis_selected:
            selected_list.append(selected.get())

        trafo.check_inputs(grabble_data, laser_data)
        trafo.coordinate_transformation(grabble_data, laser_data, selected_list)

InputGui()