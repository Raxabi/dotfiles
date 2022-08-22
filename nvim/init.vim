set number
set relativenumber
set showcmd
set background=dark
syntax enable

" Indent
set shiftwidth=4

" Custom plugins
call plug#begin('~/.config/nvim/plugins')
	
" Custom Themes
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" Syntax Highlighting
Plug 'sheerun/vim-polyglot'

" Language Server AutoCompletion
Plug 'neoclide/coc.nvim', {'branch': 'release'}

call plug#end()

let g:airline_theme = "luna"
let g:airline_powerline_fonts = 1

highlight Pmenu ctermbg=DarkGrey ctermfg=White guibg=gray
highlight Comment ctermfg=green guibg=green
