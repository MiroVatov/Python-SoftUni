from MODULES.Labs.Lab05 import create_sequence

while True:
    command = input().split()
    if 'Create' in command:
        num = int(command[-1])
        sequence = create_sequence.sequence_creation(num)
        sequence = (str(sequence).strip('[]').replace(', ', ' '))
        print(sequence)

    elif 'Locate' in command:
        num = int(command[-1])
        create_sequence.locate(num)
    elif command == 'Stop':
        break

