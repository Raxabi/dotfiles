# Edited by Raxabi

from os import path, system

# Import Custom Configuration
from funcs.screens import screens
from funcs.groups import groups
from funcs.keys import keys, mod, alt
from funcs.layouts import layouts
from funcs.widgets import widgets, widget_defaults, extension_defaults
from funcs.init_path import desktop_init

initial_config = [
    "setxkbmap es"
]

for i in initial_config:
    system(i)

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"