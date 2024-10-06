# Python-Polygons

This Python project provides classes and functions to perform geometric operations, calculations, and visualizations for various polygons, including triangles, quadrilaterals, parallelograms, rhombuses, rectangles, squares, and more. The program can compute areas, perimeters, angles, diagonals, and also check the validity of the input shapes.

## Features

- **Triangle Operations:**
  - Calculate area using Heron's formula.
  - Compute internal angles using cosine law.
  - Visualize the triangle using Turtle graphics.
  - Determine whether the triangle is valid.

- **Quadrilateral Operations:**
  - Compute angles and diagonals for general quadrilaterals.
  - Visualize the shape using Turtle graphics.

- **Parallelogram, Rhombus, and Rectangle Operations:**
  - Perform checks to verify the validity of the input polygon.
  - Compute diagonals, areas, and angles.
  - Visualize the polygons.

- **General Polygon Features:**
  - Definitions and properties for multiple polygons.
  - Access information from the web (Wikipedia).
  - Calculate perimeters, diagonals, angles, and more for specific polygons.

## Requirements

- Python 3.x
- Libraries:
  - `math`: For trigonometric and mathematical functions.
  - `numpy`: For certain trigonometric functions like `arccos`, `arcsin`.
  - `functools`: For efficient list reduction (`reduce` function).
  - `wikipedia`: To retrieve polygon definitions from Wikipedia.
  - `turtle`: For graphical visualization of the polygons.

## Installation

1. Clone the repository or download the project files.
2. Install the required libraries using pip:

```bash
pip install numpy wikipedia
```

## How to Use

1. **Create Polygon Objects:**
   - Initialize a polygon object by passing a list of sides to the `Polygons` class.
   
   Example for Triangle:
   ```python
   triangle = Triangle([side1, side2, side3])
   ```

   Example for Quadrilateral:
   ```python
   quadrilateral = Quadrilateral([(x1, y1), (x2, y2), (x3, y3), (x4, y4)])
   ```

2. **Call Functions on the Polygon:**
   - Calculate area:
     ```python
     triangle.area()
     ```
   - Get angles:
     ```python
     quadrilateral.angles()
     ```

3. **Visualize Polygons:**
   - To display a graphical representation of the polygon:
     ```python
     triangle.display()
     ```

4. **Check Validity:**
   - You can verify if the polygon provided is valid based on its geometric rules:
     ```python
     triangle.check_validity()
     ```

## Example Usage

```python
from polygon_geometry import Triangle, Quadrilateral, Parallelogram

# Example for Triangle
triangle = Triangle([3, 4, 5])
print(triangle.area())
print(triangle.angles())
triangle.display()

# Example for Parallelogram
parallelogram = Parallelogram([(0, 0), (2, 3), (6, 3), (4, 0)])
print(parallelogram.area())
parallelogram.display()
```

## Future Enhancements

- Optimization of the code to make it more compact and efficient.
- Adding functionality to handle additional polygons with more sides.
- Improving the validation logic for complex polygons.
