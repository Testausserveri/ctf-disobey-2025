# This one can figured out from the text and using known words.
cipher = {
    "u": "d",
    "g": "i",
    "w": "s",
    "x": "o",
    "c": "b",
    "f": "e",
    "n": "y",
    "y": "t",
    "t": "h",
    "f": "e",
    "z": "f",
    "p": "l",
    "h": "a",
    "v": "g",
    "i": "n",
    "l": "c",
    "o": "w",
    "s": "v",
    "d": "p",
    "b": "u",
    "a": "x",
}

ciphertext = "G hm ytf ogqhru xz Hphkthqhm. G lhi ybri vrffi hiu G hm ytf kgiv xz ytf zrxvw. Mn zhsxbrgyf zrffygmf hlygsgyn gw txddgiv hrxbiu jxnzbppn xr vhppxd ogyt h wpgvty xz wgppgifww. G pgkf yx dxiufr mn xrc hiu ufpgvtyzbppn fhy lhcchvf. G hm orgygiv ytfwf yfay txdgiv ytgw yfhltfw ytf ifo hiu lxrrbdyfu vfifrhygxiw xz ytf xpufi ohnw xz thsgiv zbi, pgkf orfwypgiv ogyt cfhrw.".lower()

flag_ciphertext = "Ytf zphv gw UGWXCFN[ytf_hrlhif_yfayw_wdfhk_ytf_yrbyt]"[12:].lower()

# print(''.join(cipher.get(c, c) for c in ciphertext)) # Used for figuring out different letters
flag = ''.join(cipher.get(c,c) for c in flag_ciphertext)
print(flag)
