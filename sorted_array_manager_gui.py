import tkinter as tk
from tkinter import messagebox

class SortedArrayManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorted Array Manager")
        self.root.geometry("500x400")
        self.root.configure(bg="#f4f4f4")

        self.arr = []

        # Array input
        tk.Label(root, text="Enter Sorted Array (space-separated):", bg="#f4f4f4", font=("Helvetica", 11)).pack(pady=(15, 5))
        self.entry_array = tk.Entry(root, width=50, font=("Helvetica", 11))
        self.entry_array.pack(pady=5)

        self.set_button = tk.Button(root, text="Set Array", command=self.set_array, width=20, bg="#007acc", fg="white")
        self.set_button.pack(pady=10)

        self.array_display = tk.Label(root, text="Current Array: []", bg="#f4f4f4", font=("Helvetica", 12, "bold"))
        self.array_display.pack(pady=10)

        # Element input
        tk.Label(root, text="Enter Element:", bg="#f4f4f4", font=("Helvetica", 11)).pack()
        self.entry_element = tk.Entry(root, width=20, font=("Helvetica", 11))
        self.entry_element.pack(pady=5)

        # Horizontal button row
        button_frame = tk.Frame(root, bg="#f4f4f4")
        button_frame.pack(pady=15)

        self.search_button = tk.Button(button_frame, text="Search", command=self.search_element, width=10, bg="#28a745", fg="white")
        self.search_button.grid(row=0, column=0, padx=10)

        self.insert_button = tk.Button(button_frame, text="Insert", command=self.insert_element, width=10, bg="#17a2b8", fg="white")
        self.insert_button.grid(row=0, column=1, padx=10)

        self.delete_button = tk.Button(button_frame, text="Delete", command=self.delete_element, width=10, bg="#dc3545", fg="white")
        self.delete_button.grid(row=0, column=2, padx=10)

    def set_array(self):
        try:
            input_data = self.entry_array.get().strip()
            if input_data == "":
                self.arr = []
            else:
                self.arr = sorted([int(x) for x in input_data.split()])
            self.update_display()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter space-separated integers.")

    def update_display(self):
        self.array_display.config(text=f"Current Array: {self.arr}")

    def search_element(self):
        try:
            target = int(self.entry_element.get())
            index = self.binary_search(target)
            if index != -1:
                messagebox.showinfo("Found", f"Element {target} found at position {index + 1}.")
            else:
                messagebox.showinfo("Not Found", f"Element {target} not found.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def insert_element(self):
        try:
            num = int(self.entry_element.get())
            self.arr.append(num)
            self.arr.sort()
            self.update_display()
            messagebox.showinfo("Inserted", f"Element {num} inserted.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def delete_element(self):
        try:
            num = int(self.entry_element.get())
            index = self.binary_search(num)
            if index != -1:
                self.arr.pop(index)
                self.update_display()
                messagebox.showinfo("Deleted", f"Element {num} deleted.")
            else:
                messagebox.showinfo("Not Found", f"Element {num} not found.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def binary_search(self, target):
        low, high = 0, len(self.arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SortedArrayManager(root)
    root.mainloop()
