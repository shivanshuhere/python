from tkinter import *

class LoanCalculator:

    def __init__(self):
        window = Tk()  
        window.title("Loan Calculator")  
        window.geometry("600x700")  
        window.config(bg="black", padx=20, pady=40)
        frame = Frame(window, bg="black", padx=20, pady=40,border=10, borderwidth=2, relief=SUNKEN).place(anchor=CENTER)
        input_font = ('Arial', 15, 'bold')

        Label(frame, text="Annual Interest Rate", font=input_font, fg="white", bg="black").grid(row=1, column=1, sticky=W)
        Label(frame, text="Number of Years", font=input_font , fg="white", bg="black").grid(row=2, column=1, sticky=W)
        Label(frame, text="Loan Amount", font=input_font , fg="white", bg="black").grid(row=3, column=1, sticky=W)
        Label(frame, text="Monthly Payment", font=input_font , fg="white", bg="black").grid(row=4, column=1, sticky=W)
        Label(frame, text="Total Payment", font=input_font , fg="white", bg="black").grid(row=5, column=1, sticky=W)

        self.annualInterestRateVar = StringVar()
        Entry(frame, textvariable=self.annualInterestRateVar, justify=RIGHT, font=input_font , fg="white", bg="black", width=15, ).grid(row=1, column=2,pady=10)
        self.numberOfYearsVar = StringVar()

        Entry(frame, textvariable=self.numberOfYearsVar, justify=RIGHT, font=input_font , fg="white", bg="black", width=15).grid(row=2, column=2, pady=10 )
        self.loanAmountVar = StringVar()

        Entry(frame, textvariable=self.loanAmountVar, justify=RIGHT, font=input_font , fg="white", bg="black", width=15).grid(row=3, column=2, pady=10)
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(frame, textvariable=self.monthlyPaymentVar, font=input_font , fg="white", bg="black").grid(row=4, column=2, sticky=E, pady=10)

        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(frame, textvariable=self.totalPaymentVar, font=input_font , fg="white", bg="black").grid(row=5, column=2, sticky=E ,pady=10)

        # create the button
        btComputePayment = Button(frame, text="Compute Payment", command=self.computePayment, font=input_font , fg="white", bg="black").grid(
            row=6, column=2, sticky=E)
        window.mainloop()  # Create an event loop

    # compute the total payment.
    def computePayment(self):

        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberOfYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment

LoanCalculator()
