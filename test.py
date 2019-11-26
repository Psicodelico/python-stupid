
def magic(listPrice, amount):
    result = []
    length = len(listPrice)
    def calc(listNum, listPrice, amount):
        n = 1
        curPrice = listPrice.pop()
        while(n*curPrice<amount & len(listPrice)>0):
            if(length == len(listNum)):
                tmp = 0
                for i in range(length):
                    tmp += listPrice[i]*listNum[i]
                    if(tmp == amount):
                        result.push(listNum)
                        return
            listNum.push(n)
            calc(listNum, listPrice, amount)
            n+=1
    calc([], listPrice, amount)
    return result

print(magic([78, 36, 25, 178, 65, 18], 7500))