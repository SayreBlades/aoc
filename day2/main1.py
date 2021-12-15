def main1(input_fn):
    horiz = 0
    depth = 0
    with open(input_fn) as file:
        for line in list(file):
            command, val = line.split()[:2]
            val = int(val)
            if command == 'down':
                depth += val
                print(command, val, depth)
            elif command == 'up':
                depth -= val
                print(command, val, depth)
            elif command == 'forward':
                horiz += val
                print(command, val, horiz)
            else:
                raise Exception(f'found {command}')
    tot = horiz * depth
    print()
    print(f"found {tot}")


def main2(input_fn):
    horiz = 0
    depth = 0
    aim = 0
    with open(input_fn) as file:
        for line in list(file):
            command, val = line.split()[:2]
            val = int(val)
            if command == 'down':
                aim += val
            elif command == 'up':
                aim -= val
            elif command == 'forward':
                horiz += val
                depth += aim*val
            else:
                raise Exception(f'found {command}')
            print(f"{command} {val}: aim={aim} horiz={horiz} depth={depth}")
    tot = horiz * depth
    print()
    print(f"found {tot}")


if __name__ == '__main__':
    main2('input')
