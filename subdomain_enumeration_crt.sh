if [ $# -gt 0 ]; then
	curl -s "https://crt.sh/?q=$1&output=json" | jq '.[] | .common_name' | sort | uniq >> "$1_domains.txt"
else
	echo "Insufficient Arguments"
fi
count=$(wc -l < "$1_domains.txt") 
echo "$count $1 subdomains retrieved"
