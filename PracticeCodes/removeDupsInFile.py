class a:
    def removeDup(self):
        with open("removeDups.txt") as f:
            seen = set()
            for line in f:
                line_lower = line.lower()
                if line_lower in seen:
                    print(line)
                else:
                    seen.add(line_lower)

z = a()
z.removeDup()
