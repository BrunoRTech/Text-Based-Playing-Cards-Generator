def printCards(ranks, suits):
    print(f"Input ranks: {ranks}")
    print(f"Input suits: {suits}")

    try:
        ranks = [int(rank) for rank in ranks]
    except ValueError:
        ranks = [-1] * len(ranks)
        print("Invalid rank input. Using default value -1.")

    rank_symbols = {
        1: "A",
        11: "J",
        12: "Q",
        13: "K"
    }
    symbols1 = [rank_symbols.get(rank, str(rank) if 2 <= rank <= 10 else " ") for rank in ranks]
    print(f"Calculated rank symbols: {symbols1}")

    suit_symbols = {
        "club": "♣",
        "diamond": "♦",
        "heart": "♥",
        "spade": "♠"
    }
    symbols2 = [suit_symbols.get(suit, " ") for suit in suits]
    print(f"Calculated suit symbols: {symbols2}")

    top_rows = [f"║ {symbol:<2}      ║" if symbol == "10" else f"║ {symbol}       ║" for symbol in symbols1]
    bottom_rows = [f"║      {symbol:<2} ║" if symbol == "10" else f"║       {symbol} ║" for symbol in symbols1]

    print(" ".join(["╔═════════╗"] * len(ranks)))
    print(" ".join(top_rows))
    print(" ".join(["║         ║"] * len(ranks)))
    print(" ".join(["║         ║"] * len(ranks)))
    print(" ".join([f"║    {symbol}    ║" for symbol in symbols2]))
    print(" ".join(["║         ║"] * len(ranks)))
    print(" ".join(["║         ║"] * len(ranks)))
    print(" ".join(bottom_rows))
    print(" ".join(["╚═════════╝"] * len(ranks)))
