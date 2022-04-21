import os

with os.scandir('./Formatted') as it:
    for entry in it:
        lines = []
        with open(entry.path, 'r') as fp:
            lines = fp.readlines()

        with open(entry.path, 'w') as fp:
            for number, line in enumerate(lines):

                if number not in [0, len(lines) - 1 ]:
                    fp.write(line)