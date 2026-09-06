# chessss2

Terminal chess in Python. You play white, the computer plays black.

The AI does a minimax search with alpha-beta pruning, two plies deep, and scores positions on material plus piece-square tables (the standard published ones). Move generation, check detection and checkmate/stalemate are all hand-written — no chess library.

## Run

    pip install numpy
    python main.py

Type moves as squares, e.g. `e2 e4`.

## Files

- `main.py` – game loop and input
- `ai.py` – evaluation and search
- `board.py` – board state, applying moves, check detection
- `pieces.py` – piece types and their move rules
- `move.py` – a move

Written in 2023 while learning how game-tree search works. in preparation for my NEA project.
