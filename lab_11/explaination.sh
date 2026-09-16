1.The shell treats STDOUT and STDERR  as two independent channels. Normally both appear mixed togeter on the terminal ,but each has its own file descripto number ,so they can be redirected independently.
1(ii) ls -l . newdir >listoffiles
Here > with no number defaults to 1 >(STDOUT Only).So the sucessfull listing of . goes into listoffiles, but the error about newdir stillprints to the terminal screen (since STDERR was not redirected)
Plain> only redirects Stdout BY DEFAULT.stderr IS UNTOUCHED AND STILL SHOWS ON SCREEN
2. -e File -> true if the file exists(regardless of directory or file)
-f file -> true if the file exist and is regular file(not a directoryy)
-s -> true if the file exist and has a size greater than zero (not empty)
3.-z means true if emoty
-n true if not empty 
4. indide [] ,\> , do string comaprisiom based on ASCII order(not numeric and redirection)
5.T=84,t=116 according to ASCII t>T(116>84)

