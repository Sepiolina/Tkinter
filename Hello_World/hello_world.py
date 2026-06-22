import tkinter as tk

def main():
    root = tk.Tk()
    root.title("CI Hello World Test")
    root.geometry("300x200")

    label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
    label.pack(expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
