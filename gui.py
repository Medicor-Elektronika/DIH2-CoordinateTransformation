from email import message
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import trafo

"""
Creates the GUI for transformation input data
"""


class InputGui:

    def __init__(self):

        root = tk.Tk()
        root.title("Coordinate Transformation")
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
        root.rowconfigure(11, weight=1)

        # Config columns
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        root.columnconfigure(3, weight=1)
        root.columnconfigure(4, weight=1)
        root.columnconfigure(5, weight=1)
        root.columnconfigure(6, weight=1)
        root.columnconfigure(7, weight=6)

        # Grabber point properties
        self.create_labeled_entry(
            root, 0, 0, "Grabber point", columnspan=6, is_entry=False)
        self.gp.append(self.create_labeled_entry(root, 1, 0, "x"))
        self.gp.append(self.create_labeled_entry(root, 2, 0, "y"))
        self.gp.append(self.create_labeled_entry(root, 3, 0, "z"))

        self.gp.append(self.create_labeled_entry(root, 1, 2, "o"))
        self.gp.append(self.create_labeled_entry(root, 2, 2, "a"))
        self.gp.append(self.create_labeled_entry(root, 3, 2, "t"))

        self.gp.append(self.create_labeled_entry(root, 1, 4, "Grabber width"))

        # Laser point properties
        self.create_labeled_entry(
            root, 4, 0, "Laser point", columnspan=6, is_entry=False)
        self.lp.append(self.create_labeled_entry(root, 5, 0, "x"))
        self.lp.append(self.create_labeled_entry(root, 6, 0, "y"))
        self.lp.append(self.create_labeled_entry(root, 7, 0, "z"))

        self.lp.append(self.create_labeled_entry(root, 5, 4, "Focus length"))

        # Side selection
        self.create_labeled_entry(
            root, 9, 0, "Select sides", columnspan=6, is_entry=False)
        axis_checkbutton_list = [ttk.Checkbutton(root, text=(
            _+1), variable=self.is_axis_selected[_], onvalue=True, offvalue=False) for _ in range(7)]

        index = 0
        for axis_checkbutton in axis_checkbutton_list:
            axis_checkbutton.grid(row=10, column=index)
            index += 1

        # Calculation button
        calculate_btn = ttk.Button(
            root, text="Calculate", command=self.calculation)
        calculate_btn.grid(row=11, column=0, columnspan=7, sticky='nsew')


        # Create an object of tkinter ImageTk
        img = ImageTk.PhotoImage(Image.open("bura.jpg"))
        label = tk.Label(image = img)
        label.grid(row=0, column=7, rowspan=11)
        root.mainloop()

    # Creates a labeled entry
    def create_labeled_entry(self, root, row, column, name, columnspan=1, rowspan=1, is_entry=True):
        label = tk.Label(root, text=str(name))
        label.grid(row=row, column=column, columnspan=columnspan,
                   rowspan=rowspan, sticky='nsew')
        if is_entry:
            entry = tk.Entry(root)
            entry.grid(row=row, column=column+columnspan, sticky='nsew')
            entry.insert(tk.END, '0.0')
            return entry

    """
    Calculation button callback function

    Checks inputs, handle errors, runs the coordinate transformation and display results
    """

    def calculation(self):
        grabble_data = []
        laser_data = []
        selected_list = []

        # Get input values from entries
        for entry in self.gp:
            grabble_data.append(entry.get())
        for entry in self.lp:
            laser_data.append(entry.get())
        for selected in self.is_axis_selected:
            selected_list.append(selected.get())

        # Check inputs
        is_correct_inputs = trafo.check_inputs(grabble_data, laser_data)
        if is_correct_inputs == True:
            # Runs coordinate transformation
            result_outputs = trafo.coordinate_transformation(
                grabble_data, laser_data, selected_list)

            # Display result in another window
            OutputGui(selected_list.count(True), result_outputs)
        else:
            messagebox.showerror("Error", message=is_correct_inputs)


"""
Creates the GUI for transformation result data
"""


class OutputGui:
    def __init__(self, n_sides, output_list):

        root = tk.Tk()
        root.title("Results")
        # Config rows
        for i in range(5*n_sides):
            root.rowconfigure(i, weight=2)

        # Config columns
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)

        for output in output_list:
            self.create_side_element(root, output[1], output[0])

        root.mainloop()

    """
    Creates a side element
    """

    def create_side_element(self, master, data, index):
        # Creates title label
        label = tk.Label(master, text="#" + str(index + 1) +
                         " side coordinates data", font=("Arial Bold", 16))
        label.grid(row=index*5, column=0, columnspan=2)

        # Creates description labels
        label = tk.Label(master, text="xyz [mm]")
        label.grid(row=index*5 + 1, column=0)
        label = tk.Label(master, text="oat [deg]")
        label.grid(row=index*5 + 1, column=1)

        # Creates data labels
        for i in range(3):
            for j in range(2):
                label = tk.Label(master, text="{:.2f}".format(data[i, j]))
                label.grid(row=index*5 + 2 + i, column=j)
