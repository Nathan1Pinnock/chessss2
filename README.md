# chessss2

Terminal chess in Python. You play white, the computer plays black.

This is a study copy of [Dirk94/ChessAI](https://github.com/Dirk94/ChessAI), not my own engine. In 2023 I worked through it line by line while learning how game-tree search works, ahead of my A-level NEA chess project, and made small changes as I went. The engine design, move generation and evaluation are Dirk94's work and the credit belongs there. The original carries no licence, so this copy is here for reading and learning only.

The AI does a minimax search with alpha-beta pruning, two plies deep, and scores positions on material plus piece-square tables.

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
