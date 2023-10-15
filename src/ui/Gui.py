from tkinter import *
from tkinter import filedialog, messagebox


class Gui:
    def __init__(self, run_command: callable) -> None:
        # The files path, to be defined by user
        self.customer_file_path = ""
        self.purchase_file_path = ""

        # General window parameters
        self.window = Tk()
        self.window.title("In flight Customer & Purchase updater")
        self.window.geometry("450x90")

        # Customer section
        self.customer_btn = Button(
            self.window, text="Select Customer file", command=self.customer_btn_click
        )
        self.customer_btn.grid(column=0, row=0)
        self.customer_file_label = Label(self.window, text="")
        self.customer_file_label.grid(column=1, row=0)

        # Purchase section
        self.purchase_btn = Button(
            self.window, text="Select Purchase file", command=self.purchase_btn_click
        )
        self.purchase_btn.grid(column=0, row=1)
        self.purchase_file_label = Label(self.window, text="")
        self.purchase_file_label.grid(column=1, row=1)

        # Run section
        # The function ran when clicked this button is the one given as a paramater to this class
        self.original_run_command = run_command
        self.run_btn = Button(
            self.window, text="Run", command=lambda: self.run_command()
        )
        self.run_btn.grid(column=0, row=2)
        self.success_label = Label(self.window, text="")
        self.success_label.grid(column=1, row=2)

    def run_command(self):
        self.original_run_command(self.customer_file_path, self.purchase_file_path)
        self.success_label.configure(
            text="Process successfully completed, check logs for more details"
        )

    def customer_btn_click(self) -> None:
        file_path = filedialog.askopenfilename()
        self.customer_file_label.configure(text=file_path)
        self.customer_file_path = file_path

    def purchase_btn_click(self) -> None:
        file_path = filedialog.askopenfilename()
        self.purchase_file_label.configure(text=file_path)
        self.purchase_file_path = file_path

    def run(self) -> None:
        self.window.mainloop()
