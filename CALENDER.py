import calendar

def show_calendar():
    try:
        year = int(year_entry.get())
        cal_content = calendar.calendar(year)
        print(cal_content) # Print to console instead of updating a label
    except ValueError:
        print("Please enter a valid year.")

# This part of the code is removed as GUI is not supported
# root = tk.Tk()
# root.title("Calendar GUI")

# year_label = tk.Label(root, text="Enter Year:")
# year_label.pack()

# year_entry = tk.Entry(root)
# year_entry.pack()

# show_button = tk.Button(root, text="Show Calendar", command=show_calendar)
# show_button.pack()

# cal_label = tk.Label(root, text="", font=("Courier", 10))
# cal_label.pack()

# root.mainloop()

# To make it runnable in Colab, you can directly ask for input and print
year_input = input("Enter Year: ")
year = int(year_input)
cal_content = calendar.calendar(year)
print(cal_content)
