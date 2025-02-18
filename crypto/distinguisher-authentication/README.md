# Distinguisher authentication

## Difficulty rating, Category

medium, Crypto

## General description of challenge (NOT GIVEN TO PLAYERS)

The point of this challenge is to essentially play with the IND-CPA definition for symmetric encryption schemes. The player has to “authenticate” themselves to get the flag and the authentication is done by solving a lot of challenges. These challenges boil down to distinguishing between the so-called real game and the ideal game which in this case is called the virus or real oracle. The player is playing the role of an adversary in the IND-CPA definition and the encryption scheme used here is designed to be deterministic which makes it not pass IND-CPA. This makes it easy to distinguish between the real and the ideal game and one can build a polynomial time adversary to distinguish the games.

The challenge is solved by making a script and communicating with the server. It is easy to distinguish between the oracle and the virus by asking the oracle two times the same question. As the virus oracle just returns a random same size string encrypted, the two same questions will return different answers. If this is the case, one can be very sure that it is a virus instead of the real oracle. This is then done the needed amount of times and then one gets the flag.

## Technical resources

It has a docker implementation and a player can run the python script by connecting to the server. One can spin up the server using `docker compose`. It maps the host port 5786 to container port 5786. You can change the host port in `compose.yaml` but please keep the container port the same.

## Description of challenge (Given to players)

Our company is trying a new authentication method to authenticate employees into our company services. We believe this is foolproof as we are using AES-CTR which is known to be IND-CPA. 
Hint: For building scripts python + pwntools are very useful tools for communicating with the service.
Flag format: DISOBEY\[[A-Za-z0-9_]*\]
`nc <server addr> <port>`
<service.py>

## Flag

DISOBEY\[1Nd_cP4_1s_SUCH_4_fUN_deF1N17IoN\]

## Solution

1. Download service.py and investigate its contents.
2. Notice that the cipher is fully deterministic and two same messages return the same value.
3. Figure out that one can distinguish between the virus and the real oracle by sending two of the same inputs to the function and seeing if they are the same or not.
4. build a script
5. Authenticate and get the flag 
