#!/bin/bash
for ((i=0;i<=50;i++))
do
	if [ $((i % 2)) -eq 0 ]
	then
		echo " The evn numbers are: $i"
	fi
done

for (( i=0; i<=50 ; i++))
do
	if [ $(( i % 2 )) -eq 1 ]
	then
		echo $i
	fi
done

for ((i=1;i<50;i+=2))
do
	echo $i
done

