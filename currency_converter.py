import tkinter as tk

currencyTemplates = [("USD",1,"United States Dollar"),("EUR",0.86,"Euro"),("SEK",9.28,"Swedish Krona"),("RUB",72.2,"Russian Ruble") ,("ZLO",0.86,"Polish Zloty")]


lang_en = {
    "cur_PLN": "Polish Zloty",
    "cur_EUR": "Euro",
    "cur_USD": "United States Dollar",
    "cur_RUB": "Russian Ruble",
    "cur_SEK": "Swedish Krona",
    "convertFrom": "Convert from",
    "convertTo": "Convert to",
    "convert": "Convert",
    "curConvert": "Currency Converter",
    "otherLang": "DE"
}

lang_de = {
    "cur_PLN": "Polnische Zloty",
    "cur_EUR": "Euro",
    "cur_USD": "US-Dollar",
    "cur_RUB": "Russische Rubel",
    "cur_SEK": "Swedische Kronen",
    "convertFrom": "Kovertieren von",
    "convertTo": "Kovertieren zu",
    "convert": "Kovertieren",
    "curConvert": "Währungsrechner",
    "otherLang": "EN"
}

cur_lang = lang_en

class Currency:
    def __init__(self, shortName, usdEquivavlent, longName):
        self.shortName = shortName
        self.usdEquivavlent = usdEquivavlent
        self.longName = longName

currency = [Currency(c[0],c[1],c[2]) for c in currencyTemplates]

class CurrencyConverter:
    def __init__(self, root):
        global currency
        self.root = root
        self.root.title(cur_lang["curConvert"])

        # LangButton
        self.langButton = tk.Button(root, text=cur_lang["otherLang"], command=self.switchlang)
        self.langButton.pack(pady=10)

        # Label
        self.convertLabel = tk.Label(root, text=cur_lang["convertFrom"])
        self.convertLabel.pack(pady=10)

        # Entry-Feld
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.strvar = tk.StringVar(root)
        self.strvar.set(cur_lang["cur_USD"])

        self.strvar2 = tk.StringVar(root)
        self.strvar2.set(cur_lang["cur_EUR"])

        currencyNames = {c.longName for c in currency}

        # Convert from
        self.dropdown = tk.OptionMenu(root,self.strvar,*currencyNames)
        self.dropdown.pack(pady=5)

        # Label für Ausgabe
        self.toLabel = tk.Label(root, text=cur_lang["convertTo"])
        self.toLabel.pack(pady=10)

        #Convert to
        self.dropdown2 = tk.OptionMenu(root,self.strvar2,*currencyNames)
        self.dropdown2.pack(pady=5)

        # Button
        self.button = tk.Button(root, text=cur_lang["convert"], command=self.convert)
        self.button.pack(pady=10)

        # Label für Ausgabe
        self.outputLabel = tk.Label(root, text="")
        self.outputLabel.pack(pady=10)

    def convert(self):
        which = self.strvar.get()
        to = self.strvar2.get()
        whichdol = todol = 0
        for c in currency:
            if c.longName == which:
                whichdol = c.usdEquivavlent
            if c.longName == to:
                todol = c.usdEquivavlent 
        val = self.entry.get()

        dol = float(val) / float(whichdol)
        res = dol * float(todol)

        self.output_label.config(text=f"{res} {to}")

    def switchlang(self):
        global cur_lang
        if cur_lang == lang_de:
            cur_lang = lang_en
        else:
            cur_lang = lang_de

        self.langButton["text"] = cur_lang["otherLang"]
        self.convertLabel["text"] = cur_lang["convertFrom"]
        self.toLabel["text"] = cur_lang["convertTo"]
        self.button["text"] = cur_lang["convert"]


if __name__ == "__main__":
    root = tk.Tk()
    gui = CurrencyConverter(root)
    root.mainloop()

