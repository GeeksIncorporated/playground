words = set("""hello
be
db
at
how
bed
are
bat
hand
beyond
and
bath
you""".split("\n"))

res = []


def breaking_words(text):

    if len(text) == 0:
        print res

    for i in xrange(len(text) + 1):
        if text[:i] in words:
            res.append(text[:i])
            breaking_words(text[i:])
            res.pop()
        continue

breaking_words("bedbathandbeyond")
