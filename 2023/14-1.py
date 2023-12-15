with open("input.txt") as f:
    lines = f.read().splitlines()

print(
    sum(
        row.count("O") * (len(lines) - i)
        for i, row in enumerate(
            map(
                "".join,
                zip(
                    *(
                        "#".join(
                            "".join(sorted(group, reverse=True))
                            for group in line.split("#")
                        )
                        for line in map("".join, zip(*lines))
                    )
                ),
            )
        )
    )
)
