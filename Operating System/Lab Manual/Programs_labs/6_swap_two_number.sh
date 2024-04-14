# Swap two number without using 3 variable

read -p "Enter First Number: " a
read -p "Enter Second Number: " b

echo Before Swapped
echo a is:${a} and b is:${b}

a=$((a+b))
b=$((a-b))
a=$((a-b))

echo After Swapped
echo a is:${a} and b is:${b}