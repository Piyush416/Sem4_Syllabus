# average of three Number

read -p "Enter first Number: " a
read -p "Enter second Number: " b
read -p "Enter third Number: " c

sum=$((a+b+c))
result=$((sum/3))

echo average of three Number is: ${result}