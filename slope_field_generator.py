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

        self.function_string = "-cos(x)" # Default to the user's example

        # --- Main layout frames ---
        canvas_frame = tk.Frame(self.root)
        canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        controls_frame = tk.Frame(self.root)
        controls_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        # --- Matplotlib Figure and Canvas ---
        self.fig = plt.figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=canvas_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # --- Create and arrange control widgets ---
        # Frame for text entry boxes
        entry_frame = tk.Frame(controls_frame)
        entry_frame.pack(pady=5)
        
        # Dictionary to hold entry widgets
        self.entries = {}
        
        # Create labels and entry boxes for each setting
        for i, setting in enumerate(["X-Min", "X-Max", "Y-Min", "Y-Max", "Grid Density"]):
            label = tk.Label(entry_frame, text=f"{setting}:")
            label.grid(row=0, column=i*2, padx=(10, 2), pady=5)
            entry = tk.Entry(entry_frame, width=7)
            entry.grid(row=0, column=i*2 + 1, padx=(0, 10), pady=5)
            self.entries[setting] = entry

        # Set default values
        self.entries["X-Min"].insert(0, "-7")
        self.entries["X-Max"].insert(0, "7")
        self.entries["Y-Min"].insert(0, "-3")
        self.entries["Y-Max"].insert(0, "3")
        self.entries["Grid Density"].insert(0, "25")

        # Frame for buttons
        button_frame = tk.Frame(controls_frame)
        button_frame.pack(pady=5)

        self.change_button = tk.Button(button_frame, text="Change Function", command=self.prompt_for_function)
        self.change_button.pack(side=tk.LEFT, padx=10)
        
        self.redraw_button = tk.Button(button_frame, text="Update Plot Settings", command=self.plot_slope_field)
        self.redraw_button.pack(side=tk.LEFT, padx=10)

        self.plot_slope_field()

    def plot_slope_field(self):
        """Clears the old plot and draws a new one based on current settings."""
        try:
            # --- 1. Read plot settings from entry boxes ---
            plot_params = {}
            for key, widget in self.entries.items():
                # Use float for ranges, int for density
                converter = int if "Density" in key else float
                plot_params[key] = converter(widget.get())
            
            x_min, x_max = plot_params["X-Min"], plot_params["X-Max"]
            y_min, y_max = plot_params["Y-Min"], plot_params["Y-Max"]
            grid_density = plot_params["Grid Density"]
            
            if x_min >= x_max or y_min >= y_max:
                messagebox.showerror("Input Error", "Min values must be less than Max values.")
                return

            # --- 2. Safely parse the function string ---
            x_sym, y_sym = symbols('x y')
            transformations = (standard_transformations + (implicit_multiplication_application,))
            expr = parse_expr(self.function_string, local_dict={'x': x_sym, 'y': y_sym}, transformations=transformations)
            f = lambdify((x_sym, y_sym), expr, 'numpy')

            # --- 3. Clear the previous plot ---
            self.ax.clear()

            # --- 4. Create grid and calculate slopes ---
            x_pts = np.linspace(x_min, x_max, grid_density)
            y_pts = np.linspace(y_min, y_max, grid_density)
            X, Y = np.meshgrid(x_pts, y_pts)
            
            with np.errstate(divide='ignore', invalid='ignore'):
                slopes = f(X, Y) 
            
            slopes = np.full_like(X, slopes) if np.isscalar(slopes) else slopes
            slopes[~np.isfinite(slopes)] = np.nan
            
            dx = np.ones_like(slopes)
            dy = slopes
            magnitude = np.sqrt(dx**2 + dy**2)
            magnitude[magnitude == 0] = 1.0
            U = dx / magnitude
            V = dy / magnitude

            # --- 5. Draw the new plot on the axes ---
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
            self.canvas.draw()

        except ValueError:
            messagebox.showerror("Input Error", "Please ensure all plot settings are valid numbers.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not process the function or settings.\n\nError: {e}")

    def prompt_for_function(self):
        new_func = simpledialog.askstring("Input", "Enter new function f(x, y):",
                                          parent=self.root, initialvalue=self.function_string)
        if new_func:
            self.function_string = new_func
            self.plot_slope_field()

if __name__ == '__main__':
    root = tk.Tk()
    app = SlopeFieldApp(root)
    root.mainloop()