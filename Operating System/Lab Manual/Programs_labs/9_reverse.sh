read -p "Enter a String: " string

reverse=" "

len=${#string}

for ((i=len-1; i>=0; i--))
do
    reverse="$reverse${string:i:1}"
done

if [ $string == $reverse ]
then
    echo "$string is palindrome"
else
    echo "$string is not palindrome"
fi
