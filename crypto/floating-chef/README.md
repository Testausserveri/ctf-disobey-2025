# Floating chef

## Difficulty rating, Category

easy, Crypto

## General description of challenge (NOT GIVEN TO PLAYERS)

This challenge is an easy cyberchef challenge where the point is to learn how to use cyberchef effectively as an easy encoding, decoding tool that runs on the internet.

Solving the challenge needs the player to open cyberchef or some similar tool to decode the message which contains the flag. The message is a bunch of floats which may trip some people but with the name and the description of this challenge I hope to deter them from falling into an unintended red herring.

## Technical resources

It needs no resources and just gives the file `recipe.txt` to the players.

## Description of challenge (Given to players)

I am Cornolius the third, a son of Cornolius the second and we have the most prestigious restaurant in the world with three Michelin stars. My father left this secret recipe for me when he died but I am still confused about the contents of this recipe. Can you help me decode it as a fellow chef, a cyberchef?
<recipe.txt>

## Flag

DISOBEY\[Wi7h_Cyb3r_ch3F_MaY_W3_rulE_th3_WOrLD\]

## Solution

1. Investigate the `recipe.txt` file and find it contains a bunch of floats. 
2. Find the cyberchef tool using open sources
3. Give the text as input and start piling up a recipe
4. Use from Float, atBash, from Hex, from Base64 and rot13 with key 7
5. Get flag
