from sys import argv

try: name: str = argv[1]
except: name: str = input("Name: ")

final: list = []
for i in name.lower():
    final.append({"a": "ka", "b": "zu", "c": "mi", "d": "te", "e": "ku", "f": "lu", "g": "ji", "h": "ri", "i": "ki",
                  "j": "zu", "k": "me", "l": "ta", "m": "rin", "n": "to", "o": "mo", "p": "no", "q": "ke", "r": "shi",
                  "s": "ari", "t": "chi", "u": "do", "v": "ru", "w": "me", "x": "na", "y": "fu", "z": "zi", ...: ...}.get(i, "\u0001?\u0001"))
input(f"{"".join(final)}\n")
