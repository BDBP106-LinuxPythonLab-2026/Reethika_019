#!/bin/bash

var1=Jayashree
var2=Nagesh
if [ $var1 > $var2 ]
then
	echo " $var1 is greater than $var2"
else
	echo " $var1 is lesser than $var2"
fi


#another method using "/"

var1=Jayashree
var2=Nagesh
if [ $var1 \> $var2 ]
then
	echo " $var1 is greater than $var2 "
else
	echo " $var1  lesser than $var2"
fi
