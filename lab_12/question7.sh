#!/bin/bash

check_dir(){
	local dir=$1
	if  [ ! -d "$dir" ]
	then
		mkdir "$dir"
		echo "Directory '$dir' did not exist "
	else
		echo "Directory '$dir' exist "
	fi
}
check_dir "Testdir"
