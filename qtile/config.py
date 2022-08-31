# Edited by Raxabi

from os import system
from libqtile import bar, layout, widget
from libqtile.config import Group, Key, Screen
from libqtile.lazy import lazy

mod = "mod4"
alt = "mod1"
terminal = "alacritty"

initial_config = [
    "setxkbmap es",
    "redshift -O 4200 -P",
    "feh --bg-scale /home/raxabi/.config/qtile/images/mountains.jpg",
    "picom &"
]

for i in initial_config:
    system(i)

# Shortcuts

keys = [

    # Switch between windows
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Up", lazy.layout.up()),
    Key([alt], "Tab", lazy.layout.next()),

    # Move windows between left/right columns or move up/down in current stack
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),

    # Grow windows
    Key([mod, "control"], "Left", lazy.layout.grow_left()),
    Key([mod, "control"], "Right", lazy.layout.grow_right()),
    Key([mod, "control"], "Down", lazy.layout.grow_down()),
    Key([mod, "control"], "Up", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),

    # Toggle between split and unsplit sides of stack
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(terminal)),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # Open programs #

    # Web
    Key([mod], "f", lazy.spawn("firefox")),
    
    # Google Chrome
    Key([mod, "shift"], "f", lazy.spawn("google-chrome-stable")),

    # Visual Studio Code
    Key([mod], "c", lazy.spawn("code")),

    # Music
    Key([mod], "s", lazy.spawn("spotify")),
    
    # Rofi Launcher
    Key([mod], "m", lazy.spawn("rofi -show run")),

    # Show running programs
    Key([mod, 'shift'], "m", lazy.spawn("rofi -show")),
]



groups = [Group(i) for i in 
    ["  ", "  ", "  ", "  ", "  ",]
]
# " ﬏ ",
for i, group in enumerate(groups):
    actual = str(i + 1)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], actual, lazy.group[group.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], actual, lazy.window.togroup(group.name, switch_group=True)),

        # Switch group on the right with arrow keys
        Key([mod, alt], "Right", lazy.screen.next_group()),
        
        # Switch group on the left with arrow keys
        Key([mod, alt], "Left", lazy.screen.prev_group())
    ])

layouts = [
    layout.Max(),
    layout.Columns(
        border_focus_stack=['#a9a9a9', '#494949'],
        border_width=2,
        margin = 5
    ),
    # layout.MonadTall(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='JetBrainsMono Nerd Font Mono',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize = 30,
                    highlight_method = 'block',
                    disable_drag = True,
                ),
                widget.WindowName(),
                widget.QuickExit(),
                widget.CurrentLayout(),
                widget.TextBox(
                    text = "",
                    fontsize = 70,
                    padding = -13,
                    foreground = "#007cc8"
                ),
                widget.TextBox(
                    text = "",
                    fontsize = "28",
                    background = "#007cc8"
                ),
                widget.Net(
                    format = "enp34s0: {down} ↓↑ {up}",
                    background = "#007cc8"
                ),
                widget.TextBox(
                    text = "",
                    background = "#007cc8",
                    foreground = "#00569f",
                    fontsize = 70,
                    padding = -13
                ),
                widget.TextBox(
                    text = "",
                    fontsize = 30,
                    background = "#00569f"
                ),
                widget.Volume(
                    background = "#00569f"
                ),
                widget.TextBox(
                    text = "",
                    background = "#00569f",
                    foreground = "#c24d33",
                    fontsize = 70,
                    padding = -13
                ),
                widget.TextBox(
                    text = "",
                    background = "#c24d33",
                    foreground = "#ffffff",
                    fontsize = 30,
                ),
                widget.Clock(
                    format='%d-%m-%Y %A | %H:%M %p',
                    background = "#c24d33",
                    foreground = "#ffffff"
                ),
                widget.TextBox(
                    text = "",
                    background = "#c24d33",
                    foreground = "#f0f36d",
                    fontsize = 70,
                    padding = -13
                ),
                widget.TextBox(
                    text = "",
                    fontsize = 29,
                    background = "#f0f36d",
                    foreground = "#000000"
                ),
                widget.Memory(
                    format = "RAM:{MemUsed: .0f}{mm}",
                    measure_mem = "G",
                    background = "#f0f36d",
                    foreground = "#000000"
                ),
                widget.TextBox(
                    text = "",
                    fontsize = 30,
                    background = "#f0f36d",
                    foreground = "#000000"
                ),
                widget.CPU(
                    background = "#f0f36d",
                    foreground = "#000000",
                    format = "CPU {load_percent}%",
                    margin = 10
                ),
                widget.TextBox(
                    text = "",
                    background = "#f0f36d",
                    foreground = "#222222",
                    fontsize = 70,
                    padding = -13
                ),
                widget.Systray()
            ],
            28,
            background="#222222",
        ),
    ),
]

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
