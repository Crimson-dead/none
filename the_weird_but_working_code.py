def that(smaller: str, bigger: str, boolean: bool):
    official = bigger
    for i in smaller:
        official = official.replace(i, "")
    if boolean:
        a = official
    else:
        a = official.__reversed__()
    print(a)
    return a


work = False


# THE CODE
try:
    to_say.something.but()
except:
    that("it", "will", not work)
