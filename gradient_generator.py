def _color(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


def _interpolate_color(color1, color2, ratio):
    r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
    g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
    b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
    return r, g, b


def _generate_gradient_string(input_string, colors):
    gradient_string = ""
    color_step = 1 / (len(input_string) - 1)
    for i, char in enumerate(input_string):
        color_index = int(i * color_step * (len(colors) - 1))
        if color_index == len(colors) - 1:
            gradient_string += _color(*colors[-1]) + char
        else:
            ratio = (i * color_step * (len(colors) - 1)) % 1
            color1 = colors[color_index]
            color2 = colors[color_index + 1]
            r, g, b = _interpolate_color(color1, color2, ratio)
            gradient_string += _color(r, g, b) + char
    gradient_string += "\033[0m"  # Reset color at the end
    return gradient_string


def make_gradient(text, *colors):
    return _generate_gradient_string(text, colors)

