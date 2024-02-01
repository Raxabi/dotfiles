require("swapper")

local call = vim.call
local Plug = vim.fn["plug#"]

call("plug#begin")

Plug('catppuccin/nvim', { as = 'catppuccin' })
Plug('nvim-tree/nvim-web-devicons') -- optional
Plug('nvim-tree/nvim-tree.lua')
Plug('neoclide/coc.nvim', { branch = 'release' })
Plug('andweeb/presence.nvim')
Plug('vim-airline/vim-airline')
Plug('akinsho/toggleterm.nvim', { tag = '*' })
Plug('iamcco/markdown-preview.nvim', { ['do'] = function() vim.call("mkdp#util#install") end, ['for'] = {'markdown', 'vim-plug'} })

call("plug#end")

vim.cmd.colorscheme("catppuccin")
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true

-- Exit from terminal mode
vim.keymap.set('t', '<Esc>', "<C-\\><C-n><C-w>h", { silent = true })

vim.keymap.set("v", "<Tab>", ">gv")
vim.keymap.set("v", "<S-Tab>", "<gv")
vim.keymap.set("n", "<A-Up>", function() Swaplines("up") end)
vim.keymap.set("n", "<A-Down>", function() Swaplines("down") end)

-- select coc sugguestions
local opts = { silent = true, noremap = true, expr = true, replace_keycodes = false }
vim.keymap.set("i", "<cr>", [[coc#pum#visible() ? coc#pum#confirm() : "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"]], opts)
vim.keymap.set("i", "<C-Space>", "coc#refresh()", { silent = true, expr = true })

local function my_on_attach(buffer)
  local api = require "nvim-tree.api"

  -- default mappings
  api.config.mappings.default_on_attach(buffer)

  -- custom mappings
  vim.keymap.set("n", "<C-a>", api.tree.open)
  vim.keymap.set("n", "<C-ñ>", api.tree.close)
  vim.keymap.set("n", "<C-h>", api.tree.toggle_hidden_filter)
  vim.keymap.set("n", "<C-c><C-l>", api.tree.focus)
  vim.keymap.set("n", "<C-p>", api.tree.change_root_to_node)
end

-- ToggleTerm configuration
require("toggleterm").setup({
    size = 13,
    open_mapping = [[<C-l>]],
    direction = 'horizontal',
    close_on_exit = true
})

-- NvimTree configuration
require("nvim-tree").setup({
  on_attach = my_on_attach,
  sort = {
    sorter = "case_sensitive",
  },
  view = {
    width = 30,
  },
  renderer = {
    group_empty = true,
  },
  filters = {
    dotfiles = true,
  },
})
