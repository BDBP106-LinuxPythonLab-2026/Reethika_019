echo "Enter numbers"
read num
 i=1
 until [ $i -gt 15 ]
 do
	 echo " $num x $i = $((num * i))"
	 i=$((i+1))
 done
