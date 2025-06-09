import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 키보드 입력 처리
        self.root.bind("<Key>", self.key_input)
        self.root.bind("<BackSpace>", self.backspace)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', '₩→¥']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            self.evaluate()
        elif char == '₩→¥':
            self.convert_to_yen()
        else:
            self.expression += str(char)
        self.update_display()

    def evaluate(self):
        try:
            self.expression = str(eval(self.expression))
        except:
            self.expression = "에러"

    def convert_to_yen(self):
        try:
            won = float(eval(self.expression))
            rate = 9  # 환율: 1엔 = 9원
            yen = won / rate
            self.expression = f"{yen:.2f} ¥"
        except:
            self.expression = "변환오류"

    def update_display(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def key_input(self, event):
        key = event.char
        if key in '0123456789+-*/.':
            self.expression += key
        elif event.keysym == 'Return':
            self.evaluate()
        self.update_display()

    def backspace(self, event):
        self.expression = self.expression[:-1]
        self.update_display()

# 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
