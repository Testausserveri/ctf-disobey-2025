# Holy hash 2

## Difficulty rating, Category

hard, Crypto

## General description of challenge (NOT GIVEN TO PLAYERS)

This challenge is a continuation of Holy hash 1 and is based on the pre-image resistance of hash-funcitons. Like in Holy hash 1 it is a python file that is ran when the player connects to the server. The original source code is also given to the player.

This challenge should only be available if one has already completed Holy hash 1.

## Technical resources

It has a docker implementation so that the python file is ran whenever a player connects to the container. The implementation is done using `docker compose` and it maps the host port 5788 to the container port 5788. Spin it up using `docker compose up`. You can change the ports in `compose.yaml` but please leave the container port unchanges or you will have to change it also in the DockerFile.

This challenge needs to also serve the file `holy_hash2.py`

## Description of challenge (Given to players)

Hi!! Wow, you have now ascended from the mortal plane and now you are in hash heaven! Good job! Here everything is bliss and we are in paradise.
Although... There is still a peculiar talking safe in here which contains some secret which is yet unknown to all of us? I think I heard the Holy hash saying something about a flag.
I am not sure what that means but the last one who opened was named Hellman.
Do you want to take a crack at opening the safe?
Flag format: DISOBEY\[[A-Za-z0-9_]*\]
`nc <server addr> 5788`
<holy_hash2.py>

## Flag

DISOBEY\[pOhLi9_hELLmaNN_IS_SuCH_4_c0o1_AL9Or17hm\]

## Solution

1. Read and understand the workings of `holy_hash2.py`
2. Notice that everything is reversible trivially except $69**block^{IV}\ mod\ 2^{128}$
3. Using open sources find the discrete log problem in cryptography
4. Using open sources find pohlig-hellman algorithm for calculating discrete logs 
5. Find some implementation of the pohlig-hellman algorithm or way to calculate it another way.
6. Make a solve script to reverse the hash.
7. Get flag
