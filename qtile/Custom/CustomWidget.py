from libqtile import widget
from libqtile.widget import base

def powerline_symbol(fg_color: str, bg_color: str) -> str:
    """
        Separator Between Widgets.

        Set a usefull and beautiful separator to widgets!

        ### bg_color is optional, because a widget can be at the end of the widget bar
        #### * bg_color refer to background color
    """
    return widget.TextBox(
        text = "",
        foreground = fg_color,
        background = bg_color,
        fontsize = 26,
        padding = -0.02
    )

class SuperWidget:
    """
        #### Create a Qtile Widget through SuperWidget constructor
    """    
    def __init__(self, WidgetIcon: str, WidgetType: widget):
        self.WidgetIcon = WidgetIcon
        self.WidgetType = WidgetType