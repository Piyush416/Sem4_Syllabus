if [ ${1} -gt ${2} ] && [ ${1} -gt ${3} ]
then
echo "${1} is Greater"
elif [ ${2} -gt ${1} ] && [ ${2} -gt ${3} ]
then
echo "${2} is Greater"
else
echo "${3} is Greater"
fi



# Input bash filename 15 20 12
# ${0} -> filename
# ${1} -> 15
# ${2} -> 20
# ${3} -> 12

# Output of this file is: 20

