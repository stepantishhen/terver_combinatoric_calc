import tkinter as tk
from math import factorial as fact


class CombinatoricsCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Combinatorics Calculator")

        self.model_var = tk.StringVar()
        self.model_var.set("Select Model")

        self.model_options = ["Permutations (No Repetitions)", "Permutations (With Repetitions)",
                              "Combinations (No Repetitions)", "Combinations (With Repetitions)",
                              "Urn Model (First Variant)", "Urn Model (Second Variant)"]

        self.model_menu = tk.OptionMenu(master, self.model_var, *self.model_options)
        self.model_menu.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_n = tk.Label(master, text="n:")
        self.label_n.grid(row=1, column=0, pady=5)

        self.entry_n = tk.Spinbox(master, from_=0, to=100)
        self.entry_n.grid(row=1, column=1, pady=5)

        self.label_k = tk.Label(master, text="k:")
        self.label_k.grid(row=2, column=0, pady=5)

        self.entry_k = tk.Spinbox(master, from_=0, to=100)
        self.entry_k.grid(row=2, column=1, pady=5)

        self.label_m = tk.Label(master, text="m:")
        self.label_m.grid(row=3, column=0, pady=5)

        self.entry_m = tk.Spinbox(master, from_=0, to=100)
        self.entry_m.grid(row=3, column=1, pady=5)

        self.label_r = tk.Label(master, text="r:")
        self.label_r.grid(row=4, column=0, pady=5)

        self.entry_r = tk.Spinbox(master, from_=0, to=100)
        self.entry_r.grid(row=4, column=1, pady=5)

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def calculate(self):
        model = self.model_var.get()
        n = int(self.entry_n.get())
        k = int(self.entry_k.get())
        m = int(self.entry_m.get())
        r = int(self.entry_r.get())

        result = ""

        if model == "Permutations (No Repetitions)":
            result = fact(n)
        elif model == "Permutations (With Repetitions)":
            result = n ** k
        elif model == "Combinations (No Repetitions)":
            result = fact(n) // (fact(k) * fact(n - k))
        elif model == "Combinations (With Repetitions)":
            result = fact(n + k - 1) // (fact(k) * fact(n - 1))
        elif model == "Urn Model (First Variant)":
            result = fact(m) // fact(n)
        elif model == "Urn Model (Second Variant)":
            result = (fact(m) // (fact(r) * fact(m - r))) * (fact(n - m) // fact(k - r)) // (fact(n) // fact(k))

        self.result_label.config(text=f"Result: {result}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CombinatoricsCalculator(root)
    root.mainloop()
