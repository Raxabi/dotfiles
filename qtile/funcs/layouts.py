from libqtile import layout

layouts = [
    layout.Max(),
    layout.Columns(
        border_focus_stack = ['#a9a9a9', '#494949'],
        border_width = 2,
        margin = 5
    ),
]