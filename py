#!/usr/bin/env sh

blue='tput setaf 4'
red='tput setaf 1'
gray='tput setaf 0'
green='tput setaf 2'
purple='tput setaf 5'
clear='tput sgr0'




if [ $(which python) = "/Users/keithsmith/.pyenv/shims/python" ]; then
    env_dir=$(pyenv prefix)
    echo "$($blue)Current python is: $($purple)$(pyenv version)"
    bp="${env_dir}/bin/bpython"
else
    env_dir=$(which python)
    echo "$($blue)Current python is: $($purple)$env_dir"
    bp="$(which python | xargs dirname)/bpython"
fi

if [ ! -e $bp ]; then
    echo "$($red)bpython not available, installing...$($gray)"
    pip install bpython
fi

echo "$($blue)Executing $($purple)$bp$($clear)"
$bp