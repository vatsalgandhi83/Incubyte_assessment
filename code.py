from spacecraft import Spacecraft

print("Enter the initial values of x, y, z: ")
x = int(input())
y = int(input())
z = int(input())
dir = input("Enter the initial direction: ")
starting_position = (x, y, z)
initial_direction = dir

no_of_commands = int(input("Enter the number of commands: "))
commands = []
for i in range(no_of_commands):
    cmd = input("Enter command: ")
    commands.append(cmd)


chandrayaan_3 = Spacecraft(*starting_position, initial_direction)
chandrayaan_3.execute_commands(commands)

print("Final Position:", (chandrayaan_3.x, chandrayaan_3.y, chandrayaan_3.z))
print("Final Direction:", chandrayaan_3.direction)
