spam=['apples', 'bananas', 'tofu', 'cats']
def commaList(somelist):
    result=''
    for i in range(0, len(somelist) -1):
        result = result + somelist[i] + ', '
    result= result + 'and '+ somelist[-1]
    print(result)
commaList(spam)
