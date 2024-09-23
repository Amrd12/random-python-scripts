import tkinter as tk

class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")
        
        # Conversion rates as a list of dictionaries
        self.conversion_rates = [
                {"from": "EGP", "to": "USD", "rate": 0.063},
                {"from": "USD", "to": "EGP", "rate": 15.91},
                {"from": "USD", "to": "EUR", "rate": 0.85},
                {"from": "USD", "to": "GBP", "rate": 0.73},
                {"from": "EUR", "to": "USD", "rate": 1.18},
                {"from": "EUR", "to": "GBP", "rate": 0.86},
                {"from": "GBP", "to": "USD", "rate": 1.37},
                {"from": "GBP", "to": "EUR", "rate": 1.16},
                {"from": "EGP", "to": "USD", "rate": 0.063},
                {"from": "EGP", "to": "EUR", "rate": 0.052},
                {"from": "EGP", "to": "GBP", "rate": 0.046},
                {"from": "EGP", "to": "JPY", "rate": 6.98},
                {"from": "EGP", "to": "CAD", "rate": 0.079},
                {"from": "EGP", "to": "AUD", "rate": 0.081}
        ]
        
        self.from_currency_label = tk.Label(master, text="From Currency:")
        self.from_currency_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.from_currency_var = tk.StringVar(master)
        self.from_currency_var.set("EGP")  # Default currency
        self.from_currency_option = tk.OptionMenu(master, self.from_currency_var, *[rate["from"] for rate in self.conversion_rates])
        self.from_currency_option.grid(row=0, column=1, padx=10, pady=10)
        
        self.to_currency_label = tk.Label(master, text="To Currency:")
        self.to_currency_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.to_currency_var = tk.StringVar(master)
        self.to_currency_var.set("USD")  # Default currency
        self.to_currency_option = tk.OptionMenu(master, self.to_currency_var, *[rate["to"] for rate in self.conversion_rates])
        self.to_currency_option.grid(row=1, column=1, padx=10, pady=10)
        
        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, columnspan=2, padx=10, pady=10)
        
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=4, columnspan=2, padx=10, pady=10)
        
    def convert(self):
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        amount = self.amount_entry.get()
        
        try:
            amount = float(amount)
        except ValueError:
            self.result_label.config(text="Please enter a valid amount.")
            return
        
        rate = None
        for conversion in self.conversion_rates:
            if conversion["from"] == from_currency and conversion["to"] == to_currency:
                rate = conversion["rate"]
                break
        
        if rate is None:
            self.result_label.config(text="Conversion not available.")
            return
        
        result = amount * rate
        self.result_label.config(text=f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")

def main():
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
