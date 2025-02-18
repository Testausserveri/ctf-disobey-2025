# Holy hash 1

## Difficulty rating, Category

medium, Crypto

## General description of challenge (NOT GIVEN TO PLAYERS)

This challenge is based on the definition of collision resistance of hash-functions. The challenges are python scripts running on a server where the player can connect to them and try to beat it. The source code `holy_hash1.py` is also given to the player.

Solving it is quite simple if you know the math behind it. The first challenge can be solved using $\varphi(n)$ which is the Euler Totient function. The second challenge is solved by calculating a discrete log which can be done using the Pohlig-Hellman algorithm. 

## Technical resources

It has a docker implementation so that the python file is ran whenever a player connects to the server. The implementation is done using `docker compose` and it maps the host port 5787 to the container port 5787. Spin it up using `docker compose up`. You can change the ports in `compose.yaml` but please leave the container port unchanged or you will have to change it also in the DockerFile.

This challenge also needs to give the players `holy_hash1.py`.

## Description of challenge (Given to players)

Hi, I’m father SHA. The leader of this church of the holy hash. Please treat yourself to a bit of hash browns and some sausage hash. In this church we worship the holy hash and we ascend to hash heaven by finding collision in it. The only ones who have succeeded in it are two very good friends Euler and Totient. Can you ascend?
Flag format: DISOBEY\[[A-Za-z0-9_]*\]
`nc <server addr> <port>`
<holy_hash1.py>

## Flag

DISOBEY\[a_V3ry_HO1y_hA5h_1Nd33d\]

## Solution

1. Read and understand the workings of holy_hash
2. Notice that everything is reversable except the 69^x mod 2^128
3. Go to open sources and find the euler totient functions property that $b^a\ \text{mod}\ n = b^c\ \text{mod}\ n \implies a = c\ \text{mod}\ \varphi(n)$
4. make a solve script and construct a collision using the previous property
5. Get flag
