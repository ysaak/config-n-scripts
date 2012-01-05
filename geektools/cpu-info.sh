#!/bin/bash


CPU_SPEED=`top -l 2 | awk '/CPU usage/ && NR > 5 {print $3}'`
echo -e "\033[1mCPU\033[0m\n${CPU_SPEED}"

python /Users/ysaak/.geektools/set_progress.py "cpu_speed" $CPU_SPEED