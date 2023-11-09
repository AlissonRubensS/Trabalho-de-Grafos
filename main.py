def LoadGraph(path):
    file = open(path, "r")
    lines = file.readlines();
    file.close()

    for line in lines:
        l = line.split()
        if(len(l) == 3):
            v = int(l[0])
            e = int(l[1])
            adj_list = [ [] for i in range(v)]
        else:
            if(l[2] == 'D'):
                adj_list[int(l[0])].append(int(l[1])) 
            else:
                adj_list[int(l[0])].append(int(l[1]))
                adj_list[int(l[1])].append(int(l[0]))

    return adj_list

def PrintGraph(adj_list):
    for i in range(len(adj_list)):
        print("V",i,":", adj_list[i])

PrintGraph(LoadGraph("grafo.txt"))