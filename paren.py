#start 11:53 9/20/2018
class stack:
    def __init__(self,data=None):
        if data == None :
            self.items = []
        else :
            self.items = data
    def __str__(self):
        return 'stack-> ' + str(self.items)
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.isEmpty() :
            return self.items.pop()
        else:
            return None
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

while __name__ == '__main__':    
    string = input()
    tack = stack()
    good = True
    for i in string:
        if i in '{([':
            #print('l', end='')
            tack.push(i)
        elif i in ')]}':
            #print('r', end='')
            if dict(zip(')]}','([{'))[i] == tack.peek():
                tack.pop()
            else:
                good = False
                break
        #else:
            #print('_', end='')

    if tack.isEmpty() and good:
        print('it is perfecttt!')
    else:
        print('FFFFFFalse Ja')

#end 00:17 9/21/2018