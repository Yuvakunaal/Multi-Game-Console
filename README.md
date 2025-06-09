# Multi-Game Console - Python Project 🎮

## Overview
This Python program implements a console-based multi-game platform featuring three classic games:
1. Rock, Paper & Scissors (Player vs Computer) 🪨 📄 ✂️
2. Snakes & Ladders (2 Players) 🐍 🎲
3. Tic-Tac-Toe (2 Players) ⭕ ❌

The application demonstrates strong programming fundamentals including:
- Modular design with a main game selector 🛠️
- User input validation ✅
- Game state management 📊
- Score tracking and statistics 📈
- Clean user interface with ASCII art 🖼️

## Code Structure

### Main Components
1. **game() function** - Core function that handles all game logic based on user selection
2. **Game Menu System** - Interactive menu for game selection and continuation
3. **Individual Game Implementations** - Three fully-featured games with rules display

## Game Details

### 1. Rock, Paper & Scissors
- **Features**:
  - Best-of-n rounds against computer
  - Input validation
  - Score tracking
  - Clear win/loss rules display
- **Technical Highlights**:
  - Random computer choice generation
  - Comprehensive win condition checking
  - Clean score display formatting

### 2. Snakes & Ladders
- **Features**:
  - Two-player implementation
  - Custom player names
  - Visual dice roll display (🎲)
  - Snake and ladder position tracking
  - Exact finish requirement (must land exactly on 100)
- **Technical Highlights**:
  - Position mapping for snakes/ladders
  - Turn-based gameplay with quit option
  - Score normalization for overshooting

### 3. Tic-Tac-Toe
- **Features**:
  - Alphabetical position reference (a-i)
  - Input validation and position checking
  - Real-time board display
  - Win/draw detection
  - Comprehensive statistics tracking
- **Technical Highlights**:
  - 2D array board representation
  - Position mapping system
  - Eight possible win condition checks
  - Move history tracking

## Technical Strengths

1. **Robust Input Handling**:
   - Type checking
   - Range validation
   - Position availability checking (Tic-Tac-Toe)
   - Case-insensitive inputs

2. **State Management**:
   - Score tracking across multiple rounds
   - Game statistics (wins/losses/draws)
   - Board state preservation

3. **User Experience**:
   - Clear rules display for each game
   - Visual separation of game elements
   - Helpful error messages
   - Option to continue or quit after each round

4. **Code Organization**:
   - Single entry point with game selection
   - Logical flow within each game
   - Consistent formatting
