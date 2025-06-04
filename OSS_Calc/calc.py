import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 키보드 입력 바인딩
        root.bind("<Key>", self.key_input)         # 일반 키
        root.bind("<BackSpace>", self.backspace)   # 백스페이스 키

        # 버튼 배열
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
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
        else:
            self.expression += str(char)

        self.update_display()

    def key_input(self, event):
        key = event.char
        if key in '0123456789+-*/.':
            self.expression += key
        elif event.keysym == 'Return':  # Enter 키
            self.evaluate()
        self.update_display()

    def backspace(self, event):
        self.expression = self.expression[:-1]
        self.update_display()

    def evaluate(self):
        try:
            self.expression = str(eval(self.expression))
        except Exception:
            self.expression = "에러"

    def update_display(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

# 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
