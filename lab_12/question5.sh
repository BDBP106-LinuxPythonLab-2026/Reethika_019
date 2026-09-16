#!/bin/bash
divide(){
	local a=$1
	local b=$2
	local quotient
	local remainder
	if [ $b -eq 0 ]
	then
		echo " Error :Divison by zero "
	fi
	quotient=$(echo "scale=2;$a/$b" | bc)
	remainder=$((a % b))
	echo "Quotient $quotient , Remainder $remainder "
}
result=$(divide 17 5)
echo "$result "
