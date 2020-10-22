def remove_palindroms(spells):
    local(a)
    a = 0
    for i in spells:
        if (i.lower()).split() == (i[::-1].lower()).split():
            spells.pop(a)
        a += 1