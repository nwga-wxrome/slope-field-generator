import tkinter as tk
from tkinter import simpledialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import symbols, lambdify, sympify
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

class SlopeFieldApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Slope Field Generator")

        # --- Store the current function string ---
        self.function_string = "-x + y"

        # --- Create the Matplotlib Figure and Axes ---
        self.fig = plt.figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(111)

        # --- Create the Tkinter Canvas ---
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # --- Create a Frame for the button ---
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

        # --- Create the "Change Function" Button ---
        self.change_button = tk.Button(master=button_frame, text="Change Function", command=self.prompt_for_function)
        self.change_button.pack(pady=5)

        # --- Draw the initial plot ---
        self.plot_slope_field()

    def plot_slope_field(self):
        """Clears the old plot and draws a new one based on self.function_string."""
        try:
            # --- 1. Safely parse the function string ---
            x_sym, y_sym = symbols('x y')
            transformations = (standard_transformations + (implicit_multiplication_application,))
            expr = parse_expr(self.function_string, local_dict={'x': x_sym, 'y': y_sym}, transformations=transformations)
            
            # --- Lambdify handles constants (like -1) correctly ---
            f = lambdify((x_sym, y_sym), expr, 'numpy')

            # --- 2. Clear the previous plot ---
            self.ax.clear()

            # --- 3. Create grid and calculate slopes ---
            x_min, x_max, grid_density = -4, 4, 25
            y_min, y_max = -4, 4
            x_pts = np.linspace(x_min, x_max, grid_density)
            y_pts = np.linspace(y_min, y_max, grid_density)
            X, Y = np.meshgrid(x_pts, y_pts)
            
            # This line works even if f() returns a single number
            slopes = f(X, Y) 
            
            slopes = np.full_like(X, slopes) if np.isscalar(slopes) else slopes
            slopes[~np.isfinite(slopes)] = np.nan
            
            dx = np.ones_like(slopes)
            dy = slopes
            magnitude = np.sqrt(dx**2 + dy**2)
            magnitude[magnitude == 0] = 1.0
            U = dx / magnitude
            V = dy / magnitude

            # --- 4. Draw the new plot on the axes ---
            self.ax.quiver(X, Y, U, V, color='dodgerblue', alpha=0.8, angles='xy',
                           scale_units='xy', scale=grid_density/((x_max-x_min)*1.5), headwidth=0)
            
            self.ax.axhline(0, color='gray', linestyle='--', linewidth=1)
            self.ax.axvline(0, color='gray', linestyle='--', linewidth=1)
            
            self.ax.set_title(f"Slope Field for $dy/dx = {sympify(self.function_string)}$", fontsize=14)
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")
            self.ax.grid(True)
            self.ax.axis('scaled')
            self.ax.set_xlim(x_min, x_max)
            self.ax.set_ylim(y_min, y_max)

            # --- 5. Refresh the canvas to show the changes ---
            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Invalid Function", f"Could not process the function.\n\nError: {e}")

    def prompt_for_function(self):
        """Opens a dialog box to ask the user for a new function."""
        new_func = simpledialog.askstring("Input", "Enter new function f(x, y):",
                                          parent=self.root, initialvalue=self.function_string)
        
        if new_func:
            self.function_string = new_func
            self.plot_slope_field()

if __name__ == '__main__':
    root = tk.Tk()
    app = SlopeFieldApp(root)
    root.mainloop()