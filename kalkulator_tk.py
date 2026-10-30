import tkinter as tk
from tkinter import messagebox


def calculate_discount():
    try:
        price = float(entry_price.get())
        discount = float(entry_discount.get())

        final_price = price - (price * (discount / 100.0))
        label_result.config(text=f"Final Price: Rp. {final_price:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


# Window setup
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("400x300")

# Widgets
label_price = tk.Label(root, text="Original Price:", font=("Arial", 11))
label_price.pack(pady=(25, 5))

entry_price = tk.Entry(root, font=("Arial", 11), width=22)
entry_price.pack(pady=(0, 15))

label_discount = tk.Label(root, text="Discount (%):", font=("Arial", 11))
label_discount.pack(pady=(0, 5))

entry_discount = tk.Entry(root, font=("Arial", 11), width=22)
entry_discount.pack(pady=(0, 20))

button_calc = tk.Button(root, text="Calculate", font=("Arial", 10), command=calculate_discount)
button_calc.pack(pady=(0, 20))

label_result = tk.Label(root, text="Final Price: Rp. 50000.00", font=("Arial", 11, "bold"))
label_result.pack(pady=(0, 20))

root.mainloop()
