
# ANSI Escape Code Gradient Generator

This Python script provides a utility to generate gradient effects for text using ANSI escape codes. It allows you to create smooth color transitions across a given text string.

### Installation

You can simply copy the provided Python script (`gradient_generator.py`) into your project directory.

### Usage Example

```python
from gradient_generator import make_gradient

# Define the text and colors for the gradient
text = "Hello, Gradient!"
color1 = (255, 0, 0)  # Red
color2 = (0, 255, 0)  # Green

# Generate the gradient string
gradient_text = make_gradient(text, color1, color2)

# Print the gradient text
print(gradient_text)
```

### Output

The above code will print the text "Hello, Gradient!" with a smooth gradient effect transitioning from red to green colors.

### Note

- The `make_gradient` function takes a text string as its first argument, followed by a variable number of color tuples `(r, g, b)`.
- Each color tuple represents the RGB values of the desired color.
- The script utilizes ANSI escape codes to apply color to each character of the text, creating the gradient effect.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Majonezowy/ANSI-Gradient-Generator/blob/main/LICENSE) file for details.
```
MIT License

Copyright (c) 2024 Majonez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
