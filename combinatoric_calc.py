import tkinter as tk
from math import factorial as fact


class CombinatoricsCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Combinatorics Calculator")

        self.model_var = tk.StringVar()
        self.model_var.set("Select Model")

        self.model_options = ["Placements (No Repetitions)", "Placements (With Repetitions)",
                              "Permutations (No Repetitions)", "Permutations (With Repetitions)",
                              "Combinations (No Repetitions)", "Combinations (With Repetitions)",
                              "Urn Model (First Variant)", "Urn Model (Second Variant)"]

        self.model_menu = tk.OptionMenu(master, self.model_var, *self.model_options)
        self.model_menu.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_input = tk.Label(master, text="input:")
        self.label_input.grid(row=1, column=0, pady=5)
        self.entry_input = tk.Entry(master)
        self.entry_input.grid(row=1, column=1, pady=5)

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

        self.model_var.trace('w', self.on_option_change)
        self.hide_all_widgets()

    def calculate(self):
        model = self.model_var.get()
        n = int(self.entry_n.get())
        k = int(self.entry_k.get())
        m = int(self.entry_m.get())
        r = int(self.entry_r.get())
        n_lst = list(map(int, self.entry_input.get().split()))

        result = ""
        if k > n:
            result = "n must be greater, than k"
        else:
            if model == "Placements (No Repetitions)":
                result = fact(n) // fact(n - k)
            elif model == "Placements (With Repetitions)":
                result = n ** k
            elif model == "Permutations (No Repetitions)":
                result = fact(n)
            elif model == "Permutations (With Repetitions)":
                if sum(n_lst) != n:
                    result = "sum of input must be equals n"
                if sum(n_lst) == n:
                    p = 1
                    for i in n_lst:
                        p *= fact(i)
                    result = fact(n) // p
            elif model == "Combinations (No Repetitions)":
                result = fact(n) // (fact(k) * fact(n - k))
            elif model == "Combinations (With Repetitions)":
                result = fact(n + k - 1) // (fact(k) * fact(n - 1))
            elif model == "Urn Model (First Variant)":
                result = fact(m) // fact(n)
            elif model == "Urn Model (Second Variant)":
                result = (fact(m) // (fact(r) * fact(m - r))) * (fact(n - m) // fact(k - r)) // (fact(n) // fact(k))

        self.result_label.config(text=f"Result: {result}")

    def show_widgets_for_option(self, option):
        # Показываем виджеты в зависимости от выбранной опции
        if option == "Placements (No Repetitions)" or option == "Combinations (No Repetitions)":
            self.label_n.grid(row=1, column=0, pady=5)
            self.entry_n.grid(row=1, column=1, pady=5)
            self.label_k.grid(row=2, column=0, pady=5)
            self.entry_k.grid(row=2, column=1, pady=5)
        elif option == "Placements (With Repetitions)" or option == "Combinations (With Repetitions)":
            self.label_n.grid(row=1, column=0, pady=5)
            self.entry_n.grid(row=1, column=1, pady=5)
            self.label_k.grid(row=2, column=0, pady=5)
            self.entry_k.grid(row=2, column=1, pady=5)
        elif option == "Permutations (No Repetitions)":
            self.label_n.grid(row=1, column=0, pady=5)
            self.entry_n.grid(row=1, column=1, pady=5)
        elif option == "Permutations (With Repetitions)":
            self.label_n.grid(row=1, column=0)
            self.entry_n.grid(row=1, column=1)
            self.label_input.grid(row=2, column=0)
            self.entry_input.grid(row=2, column=1)
        elif option == "Urn Model (First Variant)":
            self.label_n.grid(row=1, column=0, pady=5)
            self.entry_n.grid(row=1, column=1, pady=5)
            self.label_m.grid(row=2, column=0, pady=5)
            self.entry_m.grid(row=2, column=1, pady=5)
        elif option == "Urn Model (Second Variant)":
            self.label_n.grid(row=1, column=0, pady=5)
            self.entry_n.grid(row=1, column=1, pady=5)
            self.label_k.grid(row=2, column=0, pady=5)
            self.entry_k.grid(row=2, column=1, pady=5)
            self.label_m.grid(row=3, column=0, pady=5)
            self.entry_m.grid(row=3, column=1, pady=5)
            self.label_r.grid(row=4, column=0, pady=5)
            self.entry_r.grid(row=4, column=1, pady=5)

    def on_option_change(self, *args):
        selected_option = self.model_var.get()
        self.hide_all_widgets()  # Скрываем все виджеты перед показом нужных
        self.show_widgets_for_option(selected_option)

    def hide_all_widgets(self):
        self.label_input.grid_forget()
        self.entry_input.grid_forget()
        self.label_n.grid_forget()
        self.entry_n.grid_forget()
        self.label_k.grid_forget()
        self.entry_k.grid_forget()
        self.label_m.grid_forget()
        self.entry_m.grid_forget()
        self.label_r.grid_forget()
        self.entry_r.grid_forget()


if __name__ == "__main__":
    root = tk.Tk()
    app = CombinatoricsCalculator(root)
    root.mainloop()
