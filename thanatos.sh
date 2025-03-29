#!/bin/bash
sudo chmod +x art.sh
./art.sh
echo
echo
echo
echo
echo "==============================================================================================================================="
echo
echo "			                            WELCOME TO THANATOS"
echo
echo "=============================================================================================================================="

# Defining the choice function
choice() {
    read -p "Please, select: 
        1) Port scanning
        2) Domain Scanning
        3) Location
	4) Social account
 `	5) EXIT
(>>>>>>):" choice

    case $choice in
        1) 
            echo "Port scanning selected..."
            sleep 3
            python3 thanatos.py
            ;;
        2) 
            echo "Domain scanning selected..."
            read -p "Please, enter the domain name (For example: thnts.com): " domain
            ip_address=$(dig +short $domain)
        
            if [ -z "$ip_address" ]; then
                echo "Could not resolve IP for $domain"
            else
                echo "Domain $domain has IP address: $ip_address"
                # აქ ჩადე შენი სკანირების კოდი აიპზე
                echo "Starting scan on $ip_address..."
                # მაგალითად: nmap $ip_address
            fi
            whois $domain
            echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            nslookup $domain
            ;;
        3)
            while true; do
                read -p "Do you want to EXIT:(YES/NO)  " exit
                if [ "$exit" == "YES" ]; then
                    echo "Exiting..."
                    break
		elif [ "$exit" == "NO" ]; then
                     choice
		     continue
                else
		   echo "Looser, enter only YES or NO :))"
		   continue
                fi
            done
            ;;
	4)
            python3  location.py
            ;;
	5) 
 	    python3 social.py
      	    ;;
        *)
            echo "Invalid option selected."
            choice
            ;;
    esac
}

# Start by calling the choice function
choice
