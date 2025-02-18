# Arcane texts

## Difficulty rating, Category

easy, Crypto

## General description of challenge (NOT GIVEN TO PLAYERS)

This is a challenge based on frequency analysis and the charasteristics of English. We give the player a ciphertext called `arcane_text.txt`. This has been encrypted by a monoalphabetic subtitution cipher which has no rule. The player is supposed to notice from the text some common words and try to figure some plaintext from the context.  

## Technical resources

This doesn't need any technical resources and just gives the file `arcane_text.txt` to player.

## Description of challenge (Given to players)

I recovered this arcane text from the ruins of a tower which was believed to be inhabited by wizards. It is written in a ancient language and even the best linguists can't break it. Can you recover anything it said?
Flag Format: DISOBEY\[[a-z_]*\]
<`arcane_text.txt`>

## Flag

DISOBEY\[the_arcane_texts_speak_the_truth\]

## Solution

1. Look at the `arcane_text.txt`.
2. Figure out patterns in the text and known words. For example DISOBEY is known because of the flag format.
3. repeat 2. until you can recover the flag 
