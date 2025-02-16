# Surely it can't be....

Creator: Antti Ellilä

It's not DNS, There's no way it's DNS, It was DNS  
Also JavaScript binary 😂

## Category

Reverse? Forensics?

## Description

This innocent, yet suspicious looking, binary was found on one of our production servers.  
We think it was used by our competitor to steal our secrets.  
Can you figure out what was stolen?

## Installation

Not needed, provide players with the two files (`innocent-binary`, `server-traffic.pcapng`) from `chal/`

The `infra/`, `server/` and `users/` are only necessary in generating the provided packet capture.

## Solution walkthrough

The binary is "compiled" javascript. Plaintext code appended to a nodejs executable.
If one runs the file it errors with a typo in self-destruction code causing a javascript error to be shown.

Reading the code one can figure out it's exfiltrating `/root/trade-secrets.jpg` via dns requests as base36.
The file is encrypted with an aes-256-cbc key derived from some AAAA request responses.

You need to create a script to parse the dns requests from the provided packet capture and decrypt the contents.

Example solution provided in `solution/`, `python parse.py > parsed.txt` and `node solution.js`.
The solution is in two parts because it was easier for me to do the parsing in python and decryption in javascript :D
