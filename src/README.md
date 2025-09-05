# Slope Field Generator - Source Code

This directory contains the source code for the Slope Field Generator application.

## Requirements

- Python 3.8 or higher
- Dependencies listed in requirements.txt

## Setup

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```

## Running the Application

```bash
python slope_field_generator.py
```

## Development

The application is built using:
- Tkinter for the GUI
- Matplotlib for plotting
- NumPy for numerical computations
- SymPy for mathematical expression parsing

### Project Structure

- `slope_field_generator.py`: Main application file
- `slope-field-1.png`: Application icon

### Adding Features

1. The main application class is `SlopeFieldApp`
2. Plot updates are handled by `plot_slope_field()`
3. UI elements are initialized in `__init__()`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Building Executable

If you want to build the executable yourself:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Create the executable:
   ```bash
   pyinstaller --onefile --name slope_field_generator -w --add-data "slope-field-1.png;." slope_field_generator.py
   ```

The executable will be created in the `dist` directory.
