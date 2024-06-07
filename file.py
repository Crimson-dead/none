def main() -> None:
    global a, b, c, d, e, f
    e += f
    a += c*2
    b += d*3
    if b > 255:
        b = 255
        d *= -1
    if a > 255:
        c *= -1
        a = 255
    if e > 255:
        f *= -1  # A comment
        e = 255
    if b <= 0:
        b = 0
        d *= -1
    if a <= 0:
        c *= -1
        a = 0
    if e <= 0:
        f *= -1
        e = 0
    try: root.config(bg=to_hex((a, b, e)))
    except: pass
    root.after(50, main)


a = b = c = d = e = f = 1
to_hex = lambda rgb: "#%02x%02x%02x" % rgb
import tkinter as tk

root: tk.Tk = tk.Tk()
root.title(" ")
root.config(width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="red")
root.attributes("-alpha", .5)
root.after(50, main)
root.mainloop()
