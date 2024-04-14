# Factorial of given number

read -p "Enter a Number: " a

fact=1

for((i=2;i<=5;i++))
{
    fact=$((fact*i))
}

echo Factorial of ${a} is: ${fact}