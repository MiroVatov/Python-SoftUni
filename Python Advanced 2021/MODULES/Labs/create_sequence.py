
def locate(num):
    sequence_nums = sequence_creation(num)
    if num in sequence_nums:
        print(f"The number - {num} is at index {sequence_nums.index(num)}")
    else:
        print(f"The number {num} is not in the sequence")


def sequence_creation(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 2] + sequence[i - 1])
    return sequence


