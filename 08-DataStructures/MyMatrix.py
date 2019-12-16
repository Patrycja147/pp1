class matrix():

    @staticmethod
    def create(x,y):
        matrix=[[0 for i in range(x)] for j in range(y)]
        return matrix
    
    @staticmethod
    def create_unit(x):
        z=matrix.create(x,x)
        a=0
        for i in z:
            i[a]=1
            a+=1
        return z
    
    @staticmethod    
    def fill_random(matrix,b,n):
        import random
        for i in matrix:
            for j in range(len(i)):
                i[j]=random.randint(b,n)


    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)

m=matrix.create(4,5)
matrix.fill_random(m,1,8)
matrix.print(m)
