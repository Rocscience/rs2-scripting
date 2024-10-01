class ColorPicker():
    """
    RS2 can change color of an object by hex color codes or RGB. 
    """

    Black = 0x000000
    Brown = 0x002AA5
    Dark_Olive_Green = 0x404000
    Dark_Green = 0x005500
    Dark_Teal = 0x5E0000
    Dark_Blue = 0x8B0000
    Indigo = 0x82004B
    Dark_Grey = 0x282828

    Dark_Red = 0x00008B
    Orange = 0x2068FF
    Dark_Yellow = 0x008B8B
    Green = 0x009300
    Teal = 0x8E8E38
    Blue = 0xFF0000
    Blue_Grey = 0xC07B7B
    Grey_40 = 0x666666

    Red = 0x0000FF
    Light_Orange = 0x5BADFF
    Lime = 0x32CD32
    Sea_Green = 0x71B33C
    Aqua = 0xD4FF7F
    Light_Blue = 0xC09E7D
    Violet = 0x800080
    Grey_50 = 0x7F7F7F

    Pink = 0xCBC0FF
    Gold = 0x00D7FF
    Yellow = 0x00FFFF
    Bright_Green = 0x00FF00
    Turquoise = 0xD0E040
    Skyblue = 0xFFFFC0
    Plum = 0x480048
    Light_Grey = 0xC0C0C0

    Rose = 0xE1E4FF
    Tan = 0x8CB4D2
    Light_Yellow = 0xE0FFFF
    Pale_Green = 0x98FB98
    Pale_Turquoise = 0xEEEEAF
    Pale_Blue = 0x8B8368
    Lavender = 0xFAE6E6
    White = 0xFFFFFF

    def getRGBFromColor(color: int):
        """
        Returns the RGB representation of a color from its int value

        Parameters:
            color (int) : int representing the color

        Returns: 
            tuple containing red, green and blue values of the color. Each of red, green and blue are between 0 and 255 inclusive
                    
        """
        # Internally MSFT COLORREF stores the byte ordering of RGB Color as BGR: 0x00bbggrr
        blue = (color >> 16) & 0xFF
        green = (color >> 8) & 0xFF
        red = color & 0xFF

        return (red, green, blue)
    
    def getColorFromRGB(red: int, green: int, blue: int):
        """
        Returns the int representation of a color from its R, G, B values
        
        Parameters:
                red (int) : int representing red value of the color. Must be between 0 and 255 inclusive
                green (int) : int representing green value of the color. Must be between 0 and 255 inclusive
                blue (int) : int representing blue value of the color. Must be between 0 and 255 inclusive

            Returns: int representation of color formed combining rgb values
        """
        if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
                raise ValueError("Red, Green, and Blue values must be between 0 and 255, inclusive")
        
        # Internally MSFT COLORREF stores the byte ordering of RGB Color as BGR: 0x00bbggrr
        return (blue << 16) | (green << 8) | red
