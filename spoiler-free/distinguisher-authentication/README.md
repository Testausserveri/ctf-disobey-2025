# Distinguisher authentication

## Installation

`docker compose -f crypto/distinguisher-authentication/compose.yaml up -d`

## Description

Our company is trying a new authentication method to authenticate employees into our company services.
We believe this is foolproof as we are using AES-CTR which is known to be IND-CPA. 
Hint: For building scripts python + pwntools are very useful tools for communicating with the service.

Flag format: DISOBEY\[[A-Za-z0-9_]*\]

`nc <server addr> <port>`  
`nc localhost 5786`

