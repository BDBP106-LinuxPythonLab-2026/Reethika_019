cat > pytext.txt << 'EOF'
Python is a high-level, interpreted programming language
that is widely used for web development, data science, automation,
artificial intelligence, and more.
It was created by Guido van Rossum in 1991 and
has grown into one of the most popular programming languages in the world.
Key Features of Python
Readable and simple syntax - Python code often looks like plain English,
making it beginner-friendly.
Interpreted language - You don’t need to compile Python;
you can run your code directly.
Cross-platform - Works on Windows, macOS, Linux, and many other systems.
Extensive libraries - Python has built-in modules and
third-party packages (via PyPI) for tasks like math,
data analysis, networking, and visualization.
Versatile use cases - From small scripts to large-scale applications.

EOF

echo " (i)line ontaining 'and"
sed -n '/and/p' pytext.txt

echo "(ii)Changing language into lang "
sed ' s/language/lang/g ' pytext.txt

echo "(iii)DEleting lines cintaining word is"
sed '/is/d' pytext.txt


echo "(iv)inserting line number at the bigining of the line"
sed "=" pytext.txt | sed 'N;s/\n/ /'

echo "(v)Remove 1st and Second line"
sed '1,2d' pytext.txt

echo "(vi) Every other line in the above file"
sed -n '1~2p' pytext.txt

echo "(vii)First instance"
sed -e '0,/python/s/Python/python/' -e '0,/lang/s/language/lang/' pytext.txt

