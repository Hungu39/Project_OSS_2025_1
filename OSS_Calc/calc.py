import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', 'BMR']
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
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == 'BMR':
            self.open_bmr_window()
            return
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def open_bmr_window(self):
        # 새 창 생성
        bmr_win = tk.Toplevel(self.root)
        bmr_win.title("기초대사량 계산기")
        bmr_win.geometry("300x300")

        # 성별
        tk.Label(bmr_win, text="성별:").pack()
        gender_var = tk.StringVar(value="male")
        ttk.Combobox(bmr_win, textvariable=gender_var, values=["male", "female"]).pack()

        # 체중
        tk.Label(bmr_win, text="체중(kg):").pack()
        weight_entry = tk.Entry(bmr_win)
        weight_entry.pack()

        # 키
        tk.Label(bmr_win, text="키(cm):").pack()
        height_entry = tk.Entry(bmr_win)
        height_entry.pack()

        # 나이
        tk.Label(bmr_win, text="나이:").pack()
        age_entry = tk.Entry(bmr_win)
        age_entry.pack()

        result_label = tk.Label(bmr_win, text="", font=("Arial", 12))
        result_label.pack(pady=10)

        def calculate_bmr():
            try:
                weight = float(weight_entry.get())
                height = float(height_entry.get())
                age = int(age_entry.get())
                gender = gender_var.get()

                if gender == "male":
                    bmr = 10 * weight + 6.25 * height - 5 * age + 5
                else:
                    bmr = 10 * weight + 6.25 * height - 5 * age - 161

                result_label.config(text=f"BMR: {bmr:.2f} kcal/day")
            except:
                result_label.config(text="입력 오류!")

        tk.Button(bmr_win, text="계산하기", command=calculate_bmr).pack(pady=5)


