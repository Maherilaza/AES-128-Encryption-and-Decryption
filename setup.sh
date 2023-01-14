#!/bin/bash

# Vérifie si Python 3 est installé
if ! command -v python3 &> /dev/null
then
    echo "Python 3 n'est pas installé, installation en cours..."
    sudo apt-get update
    sudo apt-get install python3 -y
fi

if ! command -v pip3 &> /dev/null
then
    echo "pip n'est pas installé, installation en cours..."
    sudo apt-get install python3-pip -y
fi
pip3 install -r requirements.txt
