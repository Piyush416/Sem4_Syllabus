read -p "Enter a Number: " num

for ((i=0; i<=$num; i+=2));
do 
echo -ne "$i,"
done
