#!/bin/bash
touch nums.txt
echo "1 2 3 4 5 6 7" > nums.txt
read -ra numbers < nums.txt
echo " Original numbers:"
echo " ${numbers[@]}"

echo "Double numbers "
for n in  "${numbers[@]}"
do
	echo $((n*2))
done



