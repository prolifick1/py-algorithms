def rev(word):
    start = 0
    end = len(word) - 1
    if(not word):
        return ''
    while(start < end):
        temp = word[start]
        word[start] = word[end]
        word[end] = temp
        start+=1
        end-=1

    return word

def test_rev():
    assert(rev(['h', 'e', 'l', 'l', 'o'])) == ['o', 'l', 'l','e', 'h']
