
# Guess the Number Game

A simple Python console game where the computer picks a random number and you try to guess it.  
The game gives hints (higher or lower) and counts how many attempts you used.

## How to Run

1. Make sure you have Python (3.x) installed.  
2. Open a terminal (or command prompt).  
3. Navigate to the project folder:  
   ```
   cd guess_the_number
   ```  
4. Run the game:  
   ```
   python game.py
   ```  

## Game Flow

- The game picks a secret number between 1 and 100.  
- You are prompted to guess the number.  
- For each guess:  
  - If it's too low → you get a “Too low!” hint.  
  - If it's too high → you get a “Too high!” hint.  
  - If it's correct → you win and the game shows how many attempts you took.  
- If you enter non-integer input, you're asked again (input is validated).  

## Example Session

See `example_run.txt` for a sample play-through.

## License

This is a simple learning project — feel free to use and modify it freely.  
