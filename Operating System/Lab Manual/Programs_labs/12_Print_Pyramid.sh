read -p "Enter Pyramid height: " p

for ((row=1;row<=p;row++));
do
for ((s=row; s<=$(($p-1)); s++));
do
echo  -ne " "
done
for ((j=1; j<=row; j++));
do
echo -ne "$j"
done
echo
done


