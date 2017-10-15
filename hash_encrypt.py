import hashlib
import os


def main():
    os.system("cls")
    print("""\

                                           Verschlüsselungen - by Inkognito
                    
                                                    1 - SHA512
                                                    2 - SHA3_224
                                                    3 - SHA3_512
                                                    4 - SHA224
                                                    5 - MD5
                                                    6 - SHA512
                                                    7 - SHA1
                                                    8 - SHA384
                                                    9 - blake2s
                                                    10 - shake_128
                                                    11 - shake_256
                                                    12 - SHA256
                                                    13 - blake2b  """)

    dict = {1: (hashlib.sha512(), "SHA512"),
            2: (hashlib.sha3_224(), "SHA3_224"),
            3: (hashlib.sha3_512(), "SHA3_512"),
            4: (hashlib.sha224(), "SHA224"),
            5: (hashlib.md5(), "MD5"),
            6: (hashlib.sha512(), "SHA512"),
            7: (hashlib.sha1(), "SHA1"),
            8: (hashlib.sha384(), "SHA384"),
            9:(hashlib.blake2s(), "blake2s"),
            10:(hashlib.shake_128(), "shake_128"),
            11:(hashlib.shake_256(), "shake_256"),
            12:(hashlib.sha256(), "SHA256"),
            13:(hashlib.blake2b(), "blake2b")}
    eingabe = input("\n\nNummer: ")

    if eingabe == "help":
        print("\nGib die oben genannte Nummer ein, welche du als Verschlüsselung haben möchtest.")
        input()
        main()

    try:
        eingabe = int(eingabe)
    except ValueError:
        print("\nFalsche Eingabe. Schreib bei der Eingabe 'help' um herauszufinden, wie du das Tool benutzen kannst.")
        input()
        main()

    if not (0 < eingabe <= len(dict)):
        print("\nFalsche Eingabe. Schreib bei der Eingabe 'help' um herauszufinden, wie du das Tool benutzen kannst.")
        input()
        main()

    algo(dict[eingabe][0], dict[eingabe][1])
    algo(dict[eingabe][2], dict[eingabe][3])
    algo(dict[eingabe][3], dict[eingabe][4])
    algo(dict[eingabe][5], dict[eingabe][6])
    algo(dict[eingabe][7], dict[eingabe][8])
    algo(dict[eingabe][9], dict[eingabe][10])
    algo(dict[eingabe][11], dict[eingabe][12])
    algo(dict[eingabe][13], dict[eingabe][14])
    algo(dict[eingabe][15], dict[eingabe][16])
    algo(dict[eingabe][17], dict[eingabe][18])
    algo(dict[eingabe][19], dict[eingabe][20])
    algo(dict[eingabe][21], dict[eingabe][22])
    algo(dict[eingabe][23], dict[eingabe][24])

def algo(hash, string):
    os.system("cls")
    print(f"                                                     {string} Verschlüsselung ")
    a = bytes(input("\n\nEingabe: "), "utf-8")
    hash.update(a)
    print(f"\n{string} Hash:", hash.hexdigest())
    input()
    main()

main()