if __name__ == '__main__':
    N = int(input()) 
    List = []
    
    for _ in range(N):
        command = input()
        command = command.split(" ")

        match command[0]:
            case "insert":
                List.insert(int(command[1]), int(command[2]))
            case "print":
                print(List)
            case "remove":
                List.remove(int(command[1]))
            case "append":
                List.append(int(command[1]))
            case "sort":
                List.sort()
            case "pop":
                List.pop(len(List)-1)
            case "reverse":
                List.reverse()
