N = int(input())
elements = set(map(int, input().split()))

N_command = int(input())

while N_command:
    command = input().split(" ")
    command_name = command[0]
    
    if len(command) > 1:
        element = int(command[1])
    
    match command_name:
        case "remove":
            elements.remove(element)
        case "discard":
            elements.discard(element)
        case "pop":
            elements.pop()
    N_command -= 1

print(sum(elements))
