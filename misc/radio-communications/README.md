# Radio communications 

## Creator

Toni Tertsonen
toni@tertsonen.xyz, @tonero on Discord

## Description

We managed to capture communications between two devices. Can you decode the messages sent?

## Walkthrough

1. Analyze the capture in a SDR software, where it can be seen that the signal uses FSK modulation due to the 2 peaks (or go straight to step 2)
2. Open the file in a signal analysis tool which can demodulate FSK, such as Universal Radio Hacker
3. URH should autodetect the signal parameters
4. Remove excess garbage from the signal in the interpretation tab, every packet has some zeros in front of the actual message due to noise, these can be selected and removed afterwards by right-clicking the signal and clicking "Delete selection". Every packet has a preamble of 1111000011110000 (in bits, so it has to be figured out that bits before this are not actually part of the message)
5. Move on to the analysis tab
6. Press "Analyze Protocol", which will perform automatic analysis
7. Figure out the protocol format, which is:
- 6 bytes preamble/sync word
- 1 byte message number
- 1 byte message type
    - 0: ack
    - 1: new key
    - 2: message
- data, arbitrary length
- 1 byte CRC-ccitt checksum
8. Figure out that the data for the first message is actually a XOR key, which can be used to decrypt the third and fifth packet
9. Get the flag by decrypting the fifth packet, for example with CyberChef

## Protocol format

### Message ids
0 ack
Data contains id of acked packet.

1 transmit key
Data contains a XOR key, used to decrypt data of the following message packets.

2 message
Data contains message that is encrypted.

### Packets

```
Preamble        Message number  Message ID  Data                Checksum (crc-ccit, 1 byte)

XOR key

f0f0  82fc8a73  00              01          e4394ae74944fe9c66  40

ACK

f0f0  82fc8a73  01              00          0                   b0

Message, content: Hi!
f0f0  82fc8a73  02              02          ac506b              4a

ACK

f0f0  82fc8a73  03              00          2                   f7

Message, content: DISOBEY{D0N7_7r4N5M17_K3Y5_PU811C1Y_aasn438}

f0f0  82fc8a73  04              02          a07019a80b01a7e722d4777db87e36cad253a9087db80277a7a939b46c72d67807cfc539855839897d77c6e1 d2
```

## Flag

DISOBEY{D0N7_7r4N5M17_K3Y5_PU811C1Y_aasn438}

## Making of the challenge

First I created the protocol, drafting the packet format out to a text file. Then I generated the signals using URH's generator tab, which allows me to simply type in the desired data and modulation. Because I did not have a real SDR capable of transmitting back then, I exported the signals to Flipper Zero's format from URH. After that I played back the signals from the flipper and captured them using URH and a RTL-SDR. The complex16s file was made using URH's export feature.

## Reflections

AFAIK no one solved the challenge. (:D) It might have been that the XOR encryption was a bit much, since you had to guess that XOR encryption was being used, and the key was included in the first packet. There was supposed to be a hint about the packets containing encryption, but in the end that did not make it to the CTF due to hints not being used. However it was a great learning opportunity for someone just getting into radios and CTF challenge creation, and taught me not to underestimate the difficulty of my challenges in the future.

Also it seems like in the capture, in the first packet (and some other packets might have some errors too) the 18th byte seems to be irrelevant, so if this byte is used during the XOR decryption, the message does not decrypt fully after DISOBEY{D. However, this can be fairly easily figured out (because the decryption breaks when we get to the irrelevant bytes in the XOR operation) and the last byte removed from the XOR key in CyberChef. So maybe the challenge gained the aspect of a partly broken transmitter :D