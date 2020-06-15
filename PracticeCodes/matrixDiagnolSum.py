#Matrix

class a:
    def matrix(self):
            m = [[1,2,3],
                 [5,6,8],
                 [9,7,3]]
        
            rt=0
            ct=0

            for i in range (0,3):
                for j in range(0,3):
                    rt = rt + m[i][j]
                    ct=ct + m[j][i]
            print(rt,ct)
            
            dt1 = 0
            for i in range(0,3):
                dt1=dt1+m[i][i]
            print(dt1)

            
            dt2 = 0
            y=2
            for i in range(0,3):
                dt2=dt2+m[i][y]
                y=y-1
            print(dt2)

y = a()
y.matrix()
