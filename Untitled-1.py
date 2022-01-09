if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    cor = []
    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                if i+j+k != n:
                    coordinates = [i,j,k]
                    i = coordinates[0]
                    j = coordinates[1]
                    k = coordinates[2]
                    cor.append(coordinates)
    print(cor)
