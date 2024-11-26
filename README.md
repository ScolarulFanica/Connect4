<h1>🎮 Connect4 Game Implementation in Python 🎲</h1>

Welcome to Connect4, a Python-based reimagining of the classic 4-in-a-row strategy game!
Challenge your friends 👫, drop pieces 🟡🔴, and connect them to win 🏆.

✨ Features ✨

⚙️ Customizable Board Size: Set the board dimensions to match your playstyle (minimum: 4x4).
🎭 Player Choice: Play as ❌ or ⭕ and show your competitive spirit.
🎮 Game Mechanics:

Pieces automatically drop to the lowest available row in your chosen column.
Alternate turns to outsmart your opponent!

🧩 Modular Design:

- Encapsulated game entities ensure clean, scalable code.
- Repository-based structure simplifies data management for game pieces.
  
📂 Project Structure 📂

entities.py
🧱 Contains the Piece class, which represents each game piece with its position, player, and ID.

repo.py
📋 Implements the RepoPieces class, a repository for managing and storing game pieces.

gamebrain.py
🧠 Houses the GameBrain class, responsible for the core game logic, including:

- Placing pieces on the board.
- Determining valid rows for each move.

uiplayer.py
🎨 Offers a command-line interface for an interactive player experience:

- Customize the board size.
- Choose your game piece (❌ or ⭕).
- Make moves to compete for victory!

🚀 How to Play 🚀
Clone the repository and navigate to the project folder:

git clone <repository_url>
cd connect4
Run the game from the uiplayer.py module:

python3 uiplayer.py
Follow the instructions to:

🛠️ Set the board size.
🎭 Choose your piece (❌ or ⭕).
🎲 Take turns selecting a column and watch your pieces drop!
🛠️ Future Enhancements 🛠️
🔍 Add win detection for horizontal, vertical, or diagonal connections (coming soon!).
🎨 Introduce a graphical user interface (GUI) for a modernized look.
🤖 Implement AI for single-player mode and more challenging gameplay.

🎉 Enjoy the game and may the best strategist win! 🏆
