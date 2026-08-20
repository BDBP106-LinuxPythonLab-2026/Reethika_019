#!/bin/bash
#using -z
str=""
if [ -z "$str" ]
then
	echo "The string is empty"
else
	echo "THe string is not empty"
fi


#using -n

str=""
if [ -n "$str" ]
then
	echo "THe string is empty"
else
	echo "The string is not empty "
fi
