# 🃏 Blackjack Game

A simple command-line Blackjack game implemented in Python.

## 🎮 Game Description

This is a classic Blackjack game where you play against the computer (dealer). The goal is to get as close to 21 as possible without going over, while having a higher score than the dealer.

## 🎯 Game Rules

- **Deck**: Unlimited size deck with no jokers
- **Card Values**: 
  - Number cards (2-10): Face value
  - Face cards (Jack, Queen, King): 10 points each
  - Ace: 11 points (automatically converts to 1 if total exceeds 21)
- **Blackjack**: 21 with exactly 2 cards (Ace + 10-value card)
- **Dealer Rules**: Must draw cards until reaching 17 or higher
- **Winning Conditions**:
  - Blackjack beats all other hands
  - Closest to 21 without going over wins
  - Going over 21 results in an automatic loss ("bust")

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jadarko55/blackjack.git
   cd blackjack
   ```

2. **Run the game**:
   ```bash
   python main.py
   ```

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies required (uses only built-in Python modules)

**Note**: This game was originally designed for Replit. If running locally, you may need to modify the `clear()` function import.

## 🎲 How to Play

1. Run the program
2. You'll be dealt 2 cards initially
3. The dealer gets 2 cards (only one is shown)
4. Choose whether to draw another card ('y') or stay ('n')
5. Try to get as close to 21 as possible without going over
6. The dealer will then play automatically
7. Winner is determined based on final scores

## 📁 Project Structure

```
blackjack/
├── main.py          # Main game logic
├── art.py           # ASCII art for the game logo
├── requirements.txt # Project dependencies
├── README.md        # This file
└── .gitignore       # Git ignore rules
```

## 🔧 Code Structure

- `deal_card()`: Returns a random card from the deck
- `calculate_score()`: Calculates hand total and handles Ace conversion
- `compare()`: Determines the winner based on final scores
- `play_game()`: Main game loop
- Game continues until player chooses to quit

## 🎨 Features

- Clean command-line interface
- Automatic Ace handling (11 → 1 conversion)
- Proper Blackjack detection
- Dealer AI following standard casino rules
- Option to play multiple rounds

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📝 License

This project is open source and available under the MIT License.

## 🎯 Future Enhancements

- [ ] Add betting system
- [ ] Implement split functionality
- [ ] Add double down option
- [ ] Create GUI version
- [ ] Add multiplayer support
- [ ] Statistics tracking

---

Enjoy playing Blackjack! 🎰
