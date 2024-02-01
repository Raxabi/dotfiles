local line = vim.fn["line"]

local function istop()
  local actual = line(".")
  local limit = line("0") + 1

  return (actual == limit) and true or false
end

local function isbot()
  local actual = line(".")
  local limit = line("$")

  return (actual == limit) and true or false
end

-- Depends on the direction passed as parameter
-- if 'up' is passed, when the keybind is actioned,
-- then vim will pass the line where cursor is placed will be a position up
-- if 'down' is passed the line where cursor is placed will be a position below
--
-- Only works if the cursor is not placed at the last line, when 'down' is passed
-- either when the cursor is in the first line, when 'up' is passed
function Swaplines(direction)
  if not istop() and direction == "up" then
    vim.cmd("m-2")
  elseif not isbot() and direction == "down" then
    vim.cmd("m+1")
  else
    print("Has alcanzado el limite del archivo")
  end
end

