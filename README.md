# chessss2

Terminal chess in Python against a minimax AI. You play white, it plays black.

This is a study copy of [Dirk94/ChessAI](https://github.com/Dirk94/ChessAI), not my own engine. In 2023 I worked through it line by line while learning how game-tree search works, before my A-level NEA chess project, and made small changes as I went. The move generation, the search and the evaluation are Dirk94's, and the credit belongs there. The original has no licence, so this copy is for reading.

## Run it

    pip install numpy
    python main.py

It prints the board, asks for a move as two squares (e2 e4, or E2E4), and prints the board again after its reply.

## How it fits together

main.py is the loop: read a move, check it's in the list of white's moves, apply it, ask the AI for black's. ai.py holds the search and the evaluation: for every black move it runs alpha-beta two plies further, three plies in all, and scores a position as material (pawn 100, knight 320, bishop 330, rook 500, queen 900, king 20000) plus piece-square tables for everything but the king. board.py is an 8 by 8 list of pieces with cloning, applying a move, castling, promotion and a check test. pieces.py has the move rules for each piece, and move.py is four coordinates.

## Rough edges

- Moves are checked against the pseudo-legal list only, so you can leave your own king in check. The AI takes it and the game carries on without a white king.
- No en passant, promotion is always to a queen, and castling checks that the king hasn't moved but not the rook, and not whether the king passes through check.
- is_check doesn't look at attacks. It clones the board, plays every enemy move, and looks for the king afterwards.
- numpy is imported for five 8 by 8 tables that lists would do, and pieces.py imports ai without using it.
