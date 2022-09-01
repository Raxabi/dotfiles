from libqtile.config import Group, Key
from libqtile.lazy import lazy

from .keys import keys, mod, alt

groups = [Group(i) for i in
    ["  ", "  ", "  ", "  ", "  "]
]

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