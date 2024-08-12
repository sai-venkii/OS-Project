RED="\e[31m"
GREEN="\e[32m"
WHITE='\033[0;37m'
YELLOW='\033[0;33m'
ENDCOLOR="\e[0m"
PURPLE='\033[0;35m'      

printf "${RED}"
figlet -w 100 -c "SUID Escalation"
printf "${ENDCOLOR}"

#printf "${RED}LINUX Privilege Escalation USING SUID\n${ENDCOLOR}\n" 
printf "Checking SUID\n\n"

suid=$(find / -perm -4000 2>/dev/null | awk -F "/" '{print $NF}' | sort -u)

#echo $suid

for bin in $suid; do
	echo "---------------------------------------------------------------------------------------------------------------"
	echo -e "${PURPLE} $bin ${ENDCOLOR}"
	cmd=$(curl -s "https://gtfobins.github.io/gtfobins/$bin/#suid" | html2text | sed -n '/\*\*\*\*\* SUID \*\*\*\*\*/,$p' |	sed '1d' | sed -n '/^[[:space:]]*\*/,/^\*\*\*\*\*$/ {/^\*\*\*\*\*$/d; p}' | awk '/\*\*\*\*\*/ {exit} {print}')
	if [ -n "$cmd" ]; then
		echo -e "${GREEN}"
		curl -s "https://gtfobins.github.io/gtfobins/$bin/#suid" | html2text | sed -n '/\*\*\*\*\* SUID \*\*\*\*\*/,$p' |	sed '1d' | sed -n '/^[[:space:]]*\*/,/^\*\*\*\*\*$/ {/^\*\*\*\*\*$/d; p}' | awk '/\*\*\*\*\*/ {exit} {print}'
		echo -e "${ENDCOLOR}"
	else
		echo -e "${RED} NO EXPLOIT FOUND${ENDCOLOR}"
	fi
done
