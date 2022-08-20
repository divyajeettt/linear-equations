import matplotlib.pyplot as plt
import logging
from tkinter import *
from tkinter.messagebox import *
from linear_equations import *


def callback(string: str) -> bool:
    """validates the Entry boxes"""

    try:
        float(string)
        return True
    except ValueError :
        if string.startswith("-") and string.count("-") < 2:
            return callback(string[1:])
        return not string


def is_complete() -> bool:
    """checks if the user has entered all the values"""

    global eqn1, eqn2

    for i in range(len(coeffs)):
        if not coeffs[i].get().strip():
            showwarning("Empty Field", "All coefficients are required.")
            logger.warning("One or more coefficients found empty")
            return False

        if not float(coeffs[i].get()):
            if i not in {2, 5}:
                showerror("Invalid Input", "Coefficient of x or y cannot be 0")
                logger.error("Attempt to input coefficient of x or y = 0")
                coeffs[i].delete(0, END)
                return False

    a1, b1, c1, a2, b2, c2 = [float(box.get()) for box in coeffs]
    eqn1 = LinearEquation2D(a1, b1, c1)
    eqn2 = LinearEquation2D(a2, b2, c2)
    return True


def check_consistency() -> None:
    """displays the consistency of the entered linear equations"""

    if not is_complete():
        return
    else:
        answer = "Consistent" if consistency(eqn1, eqn2) else "Inconsistent"

    is_consistent.config(state=NORMAL)
    is_consistent.delete(0, END)
    is_consistent.insert(0, answer)
    is_consistent.config(state="readonly")

    logger.info(f"Checked Consistency: {eqn1} and {eqn2} -> {answer}")


def solution() -> tuple[float, float]|None:
    """displays the solution to the entered equations"""

    if not is_complete():
        return
    else:
        check_consistency()
        for i in range(2):
            solutions[i].config(state=NORMAL)
            solutions[i].delete(0, END)

    if not consistency(eqn1, eqn2):
        soln = None, None
        for i in range(2):
            solutions[i].insert(0, "No Solution")
            solutions[i].config(state="readonly")
    else:
        soln = solve2D(eqn1, eqn2)
        for i in range(2):
            solutions[i].insert(0,
                "Infinite Solutions" if float("inf") in soln else str(soln[i])
            )
            solutions[i].config(state="readonly")

    logger.info(f"Solved equations: {eqn1} and {eqn2} -> {soln}")
    return soln


def display() -> None:
    """plots the two linear equations on a graph"""

    if not is_complete():
        return
    else:
        X, Y = solution()

    plt.close("all")
    graph(eqn1, eqn2)
    logger.info(f"Plotting equations: {eqn1} and {eqn2}")


LOG_FORMAT: str = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(
    filename="linear_equations_gui.log", level=logging.INFO, format=LOG_FORMAT
)
logger = logging.getLogger()

root: Tk = Tk()
root.geometry("400x270")
root.title("Linear Equations Solver")
root.resizable(False, False)

Label(
    text="Solve two Linear Equations in two variables:",
    width=57, bd=3
).place(x=0, y=0)

Label(
    text="a₁x + b₁y + c₁ = 0    AND    a₂x + b₂y + c₂ = 0",
    width=57, bd=3
).place(x=0, y=20)

Label(
    text="Enter the coefficients and constants, which must be real numbers.",
    width=57, bd=3
).place(x=0, y=40)

Label(text="YOUR EQUATIONS:").place(x=10, y=65)
Label(text="x =").place(x=20, y=203)
Label(text="y =").place(x=210, y=203)

for i in range(2):
    Label(text="x   +").place(x=100, y=(85 + i*25))
    Label(text="y   +").place(x=230, y=(85 + i*25))
    Label(text="=   0").place(x=360, y=(85 + i*25))

reg = root.register(callback)

coeffs: list[Entry] = []
for i in range(6):
    coeffs.append(Entry(width=12, bd=2, cursor="xterm"))
    coeffs[i].config(validate="key", validatecommand=(reg, "%P"))
    if i < 3:
        coeffs[i].place(x=(20 + i*125), y=87)
    else:
        coeffs[i].place(x=(20 + (i-3)*125), y=112)

solutions: list[Entry] = [Entry(width=23, bd=2, state="readonly") for i in range(2)]
solutions[0].place(x=50, y=205)
solutions[1].place(x=240, y=205)

Button(
    text="Check Consistency", width=27, cursor="hand2",
    command=check_consistency
).place(x=5, y=135)

is_consistent = Entry(width=30, bd=2, state="readonly")
is_consistent.place(x=210, y=138)

Button(
    text="Solve the Equations", width=54, cursor="hand2", command=solution
).place(x=5, y=165)

Button(
    text="Plot solutions on Graph", width=54, cursor="hand2", command=display
).place(x=5, y=236)


if __name__ == "__main__":
    logger.info("Opened Linear Equations Solver")
    root.mainloop()
    logger.info("Closed Linear Equations Solver \n")