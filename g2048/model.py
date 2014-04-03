from random import randint

class m2048:
    def m2048(self):
        pass
    
    def generate(self):
        flag=0
        while not flag:
            (a,va)=(randint(0,15),2 if randint(1,8)>1 else 4)
            if self.board[a] is None:
                flag=1
                self.board[a]=va

    def init(self):
        self.board=[None]*16
        self.generate()
        self.generate()


    def isWon(self):
       return any([x for x in self.board if x==2048])

    def checkCell(self,x,y):
        if self.board[x]==self.board[y]:
            if x/4==y/4 and x==y+1:
                return 1
            
            if x==y+4:
                return 1
        return 0

    def isFailed(self):
        for x in range(0,15):
            if not self.board[x]:
                return 0
            for y in range(0,15):
                if not self.board[y]:
                    return 0
                if self.checkCell(x,y):
                    return 0
        return 1

    @staticmethod
    def merge(row):
        flag=[1,1,1,1]
        nrow=[t for t in row if t]
        for i in range(0,len(nrow)-1):
            if i>=len(nrow)-1:
                break
            if flag[i] and nrow[i+1]==nrow[i]:
                nrow[i]*=2
                nrow[i+1]=None
                flag[i]=0
            nrow=[t for t in nrow if t] 
        while len(nrow)<4:
            nrow.append(None)
        return tuple(nrow)

    def move(self,vec):
        a=self.board
        if vec=="up":
            for x in range(0,4):
                row=m2048.merge((a[x],a[x+4],a[x+8],a[x+12]))
                a[x],a[x+4],a[x+8],a[x+12]=row     

        if vec=="down":
            first=0
            for x in range(12,16):
                row=m2048.merge((a[x],a[x-4],a[x-8],a[x-12])) 
                a[x],a[x-4],a[x-8],a[x-12]=row

        if vec=="left":
            first=0
            for x in range(0,13,4):
                row=m2048.merge((a[x],a[x+1],a[x+2],a[x+3]))
                a[x],a[x+1],a[x+2],a[x+3]=row

        if vec=="right":
            first=0
            for x in range(3,16,4):
                row=m2048.merge((a[x],a[x-1],a[x-2],a[x-3]))
                a[x],a[x-1],a[x-2],a[x-3]=row

if __name__=='__main__':
    game=m2048()
    game.init()
    print game.board


