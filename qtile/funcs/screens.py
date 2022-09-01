# This file contain the configuration for the status bar and the Desktop Wallpaper

from libqtile.config import Screen
from libqtile.bar import Bar

# Custom Widgets
from .widgets import widgets

screens = [
    Screen(
        wallpaper = "~/wallpapers/endyFixed_01.png",
        wallpaper_mode = "stretch",
        top=Bar(
            widgets,
            28,
            background="#222222"
        )
    )
]