#!/bin/bash
VALUE="`snmpget -$1 -c $2 -OUvq $3 1.3.6.1.4.1.5454.1.30.1.6 2>/dev/null`"
#echo "Version: "$1
#echo "Community: "$2
#echo "IP: "$3
if [[ $VALUE = 0 ]]
then 
	echo 'SNMP Status OK|ifOperStatus=1'
else 
	echo 'SNMP Status OK|ifOperStatus=2' 
fi

