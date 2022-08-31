if status is-interactive
    # Commands to run in interactive sessions can go here
end

# Deno CLI export to path
export DENO_INSTALL="/home/raxabi/.deno"
export PATH="$DENO_INSTALL/bin:$PATH"

# Flask environment variables
#export FLASK_APP=index
#export FLASK_ENV=development

# Android environment Packages
export ANDROID_SDK_ROOT=$HOME/Library/Android/Sdk
export PATH="$PATH:$ANDROID_SDK_ROOT/emulator"
export PATH="$PATH:$ANDROID_SDK_ROOT/platform-tools"

# Python Packages PIP
export PATH="/home/raxabi/.local/bin:$PATH"

# Custom Aliases
alias py='python'
alias ls='ls --color=auto'
alias ll='ls -l'
alias la='ls -a'
alias lla='ls -la'
alias lsdid='sudo blkid'
alias leer='redshift -O 4500 -P'
alias cleno='clear && neofetch'
alias xampp='sudo /opt/lampp/managerxamp.run'
alias copy='xclip -selection clipboard'
neofetch

# Themes config

#set -U AGNOSTER_PROMPT_SEGMENTS ("prompt_git" "${AGNOSTER_PROMPT_SEGMENTS[@]}")
