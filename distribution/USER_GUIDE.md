# User Guide - Slope Field Generator

## Introduction

The Slope Field Generator is a mathematical visualization tool that helps in understanding the behavior of first-order differential equations. It creates a graphical representation of the equation's solutions by plotting short line segments that indicate the slope at various points.

## Getting Started

1. **Starting the Application**
   - Locate and double-click `slope_field_generator.exe`
   - The application will open with a default slope field for `-cos(x)`

2. **Interface Overview**
   - Main Plot Area: Displays the slope field
   - Control Panel (bottom):
     - Input fields for plot ranges
     - Grid density control
     - Function change button
     - Dark mode toggle

3. **Basic Controls**
   - X-Min, X-Max: Set horizontal plot range
   - Y-Min, Y-Max: Set vertical plot range
   - Grid Density: Adjust number of plotted vectors
   - Change Function: Enter new differential equation
   - Update Plot Settings: Apply changes
   - Toggle Dark Mode: Switch between light/dark themes

## Advanced Usage

### Mathematical Functions

Available mathematical functions and operators:
- Basic: +, -, *, /, ^
- Trigonometric: sin, cos, tan, asin, acos, atan
- Exponential/Logarithmic: exp, log, ln
- Other: sqrt, abs

### Examples

1. Linear Equations
   - `y`
   - `x`
   - `x + y`

2. Nonlinear Equations
   - `-sin(x)`
   - `x*y`
   - `x^2 - y^2`

3. Exponential Growth/Decay
   - `exp(-x)`
   - `log(x)*y`

### Tips for Best Results

1. **Choosing Ranges**
   - Start with smaller ranges (-5 to 5)
   - Adjust based on function behavior
   - Keep aspect ratio reasonable

2. **Grid Density**
   - Higher values (60-100) for smooth plots
   - Lower values (20-40) for faster performance
   - Adjust based on screen size

3. **Visualization**
   - Use dark mode for presentations
   - Experiment with different ranges
   - Look for patterns in the field

## Technical Information

### Performance Considerations

- Grid density affects performance
- Recommended maximum grid density: 100
- Complex functions may take longer to plot

### Error Messages

1. "Input Error"
   - Check number format in range fields
   - Verify min values are less than max values

2. "Could not process function"
   - Verify function syntax
   - Check for missing parentheses
   - Ensure valid mathematical expression

### Security and Privacy

The application:
- Runs locally without internet connection
- Does not store or transmit data
- Creates no temporary files
- Requires no installation

## Support

For additional support or to report issues, please refer to the README.md file included with the distribution.

---

This guide is part of the Slope Field Generator distribution package.
Last updated: September 2025
