mass=1
speed=300000000
energy=$(bc << EOF
$mass*($speed*$speed)
EOF
)
echo "Energy=$energy"

