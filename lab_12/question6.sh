maximum(){
	local a=$1
	local b=$2
	if [ $a -ge $b ]
	then
		echo $a
	else
		echo $b
	fi
}
maximum_value=$(maximum 64 33 )
echo "Maximum values is $maximum_value"
	
