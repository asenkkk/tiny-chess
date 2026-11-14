# Tiny Chess — strongest chess engine in 4 KB of Python

A pure-Python UCI chess engine in a single 4,096-byte file (`main.py`).

Run it: `python3 main.py`

Then talk UCI to it: `uci`, `isready`, `position startpos`, `go movetime 1000`.

Negamax + alpha-beta + iterative deepening, transposition table for move ordering, MVV-LVA ordering. Material + pawn-push + knight-centralisation evaluation. Supports castling, en passant, promotion (including underpromotion), FEN and `position startpos moves ...`.

MIT licensed.
