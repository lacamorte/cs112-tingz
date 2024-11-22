import tkinter as tk
from datetime import datetime, timedelta

root = tk.Tk()
root.geometry("800x500")
root.title("Water Bill Calculator")

label = tk.Label(root, text="Fontaine Water District", font=('Consolas', 12))
label.pack(padx=20, pady=20)

detailFrame = tk.Frame(root)
detailFrame.columnconfigure(0, weight=1)
detailFrame.columnconfigure(1, weight=1)
detailFrame.columnconfigure(2, weight=1)
detailFrame.columnconfigure(3, weight=1)

detailFrame.rowconfigure(0, weight=0)
detailFrame.rowconfigure(1, weight=1)
# ROW 0 (labels)
readingDate = tk.Label(detailFrame, text="READING DATE", font=('Consolas', 12))
readingDate.grid(row=0, column=0, sticky=tk.W + tk.E)
dateDue = tk.Label(detailFrame, text="DATE DUE", font=('Consolas', 12))
dateDue.grid(row=0, column=1, sticky=tk.W + tk.E, padx=5)
amountDueLate = tk.Label(detailFrame, text="AMOUNT DUE AFTER DUE DATE", font=('Consolas', 12))
amountDueLate.grid(row=0, column=2, sticky=tk.W + tk.E, padx=5)
month = tk.Label(detailFrame, text="FOR THE MONTH OF", font=('Consolas', 12))
month.grid(row=0, column=3, sticky=tk.W + tk.E, padx=5)

# ROW 1 (results)
#reading date
dateNow = datetime.now()
dateRN = dateNow.strftime("%m-%d")
dateNow2 = tk.Label(detailFrame, text=f"{dateRN}", font=('Consolas', 12))
dateNow2.grid(row=1, column=0, sticky=tk.W + tk.E, padx=5)
#date due
oneweeklater = dateNow + timedelta(days = 7)
dateDue2 = oneweeklater.strftime("%m-%d")
dateDue3 = tk.Label(detailFrame, text=f"{dateDue2}", font=('Consolas', 12))
dateDue3.grid(row=1, column=1, sticky=tk.W + tk.E, padx=5)
#rough draft of late fee charge
def charge(amtdue, floatrate):
    latefee = amtdue + (amtdue * floatrate)
    return latefee 
amtdue = 1268.39
lateAmtdue = charge(1268.39, 0.01)
lateAmtdue_Label = tk.Label(detailFrame, text=f"₱{lateAmtdue:.2f}", font=('Consolas', 12))
lateAmtdue_Label.grid(row=1, column=2, sticky=tk.W + tk.E, padx=5)
# for the month of
monthOf = datetime.now().strftime("%b %Y")
monthOf2 = tk.Label(detailFrame, text=f"{monthOf}", font=('Consolas', 12))
monthOf2.grid(row=1, column=3, sticky=tk.W + tk.E, padx=5)

detailFrame.pack()

root.mainloop()