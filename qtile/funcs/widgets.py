# This file contain the configuration for widgets

from libqtile import widget
from Custom.CustomWidget import powerline_symbol

widget_defaults = dict(
    font='JetBrainsMono Nerd Font Mono',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

widgets = [
    widget.GroupBox(
        fontsize = 30,
        highlight_method = 'block',
        disable_drag = True,
    ),
    widget.WindowName(),
    widget.CurrentLayout(),
    powerline_symbol(fg_color="#afa9ff", bg_color=""),
    widget.TextBox(
        text = "Raxabi ",
        background = "#afa9ff"
    ),
    powerline_symbol(fg_color="#ffaffe", bg_color="#afa9ff"),
    widget.TextBox(
        text = "",
        background = "#ffaffe",
        foreground = "#000000",
        fontsize = 30,
    ),
    widget.Clock(
        format='%d %A %H:%M %p | %B del %Y ',
        background = "#ffaffe",
        foreground = "#000000"
    ),
    widget.Systray()
]