#!/bin/bash

# Retrieve username
username=$(<name.txt)

# Retrieve stats
data=$(curl https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=$username)

python3 src/main.py $data