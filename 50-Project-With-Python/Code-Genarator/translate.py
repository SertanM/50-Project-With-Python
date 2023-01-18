inp = input()
buSabah = {ord("A"): ord("Y"),ord("B"): ord("V"),ord("C"): ord("M"),ord("Ç"): ord("4"),ord("D"): ord("N"),ord("E"): ord("N"),
           ord("F"): ord("f"),ord("G"): ord("0"),ord("Ğ"): ord("Z"),ord("İ"): ord("W"),ord("I"): ord("v"),ord("J"): ord("e"),
           ord("K"): ord("I"),ord("L"): ord("P"),ord("M"): ord("l"),ord("N"): ord("K"),ord("O"): ord("T"),ord("Ö"): ord("w"),
           ord("P"): ord("3"),ord("Q"): ord("S"),ord("R"): ord("7"),ord("S"): ord("u"),ord("Ş"): ord("G"),ord("T"): ord("W"),
           ord("U"): ord("k"),ord("Ü"): ord("p"),ord("V"): ord("E"),ord("W"): ord("b"),ord("X"): ord("C"),ord("Y"): ord("Z"),
           ord("Z"): ord("b"),ord("a"): ord("Z"),ord("b"): ord("3"),ord("c"): ord("l"),ord("d"): ord("6"),ord("e"): ord("q"),
           ord("f"): ord("u"),ord("g"): ord("n"),ord("ğ"): ord("L"),ord("i"): ord("X"),ord("ı"): ord("U"),ord("j"): ord("F"),
           ord("k"): ord("7"),ord("l"): ord("2"),ord("m"): ord("v"),ord("n"): ord("j"),ord("o"): ord("b"),ord("ö"): ord("c"),
           ord("p"): ord("S"),ord("q"): ord("P"),ord("r"): ord("r"),ord("s"): ord("Ü"),ord("ş"): ord("n"),ord("t"): ord("G"),
           ord("u"): ord("e"),ord("ü"): ord("ç"),ord("v"): ord("/"),ord("w"): ord("{"),ord("x"): ord("v"),ord("y"): ord("j"),
           ord("z"): ord("?")}
print(inp.translate(buSabah))