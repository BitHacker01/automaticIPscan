#!/bin/bash
       nmap  -p 3389 -iL $1 -Pn | grep -e report -e tcp > result.txt



<<COMMENT1
    usage:
	1.  ./randomIPport.sh domains.txt  
  	2.  cat result.txt

COMMENT1

