
echo "The value of '$HOME"
echo $HOME
bc << EOF
scale=4
23934/4434
EOF
echo "Files in home path with letter D"
ls "$HOME" | grep '^D'
echo "Lines in /etc/passwd with username $(whoami):"
grep "$(whoami)" /etc/passwd

