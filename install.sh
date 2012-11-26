#!/bin/bash 

# get current dir
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ] ; do SOURCE="$(readlink "$SOURCE")"; done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"


# install tools config files
echo "Installing config files ..."
CONFIG_FILES=( 'astylerc' 'screenrc' 'tmux.conf' 'bashrc' 'profile')
ELEMENTS=${#CONFIG_FILES[@]}

for (( i=0;i<$ELEMENTS;i++)); do 
    if [ -e "${HOME}/.${CONFIG_FILES[${i}]}" ] ; then 
        echo "Warning: a ${CONFIG_FILES[${i}]} file already exists. Old file moved to backup folder."
        mkdir -p ${DIR}/backup
		mv ${HOME}/.${CONFIG_FILES[${i}]} ${DIR}/backup/${CONFIG_FILES[${i}]}.bak
    fi
    ln -s ${DIR}/config/${CONFIG_FILES[${i}]} ${HOME}/.${CONFIG_FILES[${i}]}
done

# tools (bin dir)
ln -s ${DIR}/bin/colorgcc.pl ${DIR}/bin/msp430-gcc

