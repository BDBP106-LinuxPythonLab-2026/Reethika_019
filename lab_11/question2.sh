touch empty.txt
echo "hello" > full.txt
mkdir mydir
if [ -e empty.txt ]
then
	echo "empty.txt exist"
fi

if [ -f mydir ]
then
	echo "mydir is a file "
else
	echo "mydir is not a regular file "
fi

if [ -s empty.xt ]
then
	echo "not empty "
else
	echo "empty.txt has no size zer"
fi

if [ -s full.txt ]
then
	echo "full.txt is non empty "
fi



