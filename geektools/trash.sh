#!/bin/bash

SIZE=`du -sh ~/.Trash/ | awk '{print $1}'`

if [ $SIZE == "0B" ]
then
    echo "Empty"
else
    ITEMS=`ls -1 ~/.Trash/ | wc -l | sed 's/ //g'`
    
    if [ $ITEMS -eq 1 ]
    then
        echo "1 item"
    else
        echo "$ITEMS items"
    fi

    echo "$SIZE"
fi
