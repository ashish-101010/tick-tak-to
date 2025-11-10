import os
import time
import sys

# ANSI color codes for terminal styling
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BG_BLUE = '\033[44m'
    BG_GREEN = '\033[42m'
    BG_RED = '\033[41m'
    # Additional colors for glowing effects
    BRIGHT_RED = '\033[31m'
    BRIGHT_BLUE = '\033[34m'
    BRIGHT_YELLOW = '\033[33m'
    BRIGHT_WHITE = '\033[37m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color=Colors.WHITE, bold=False, end="\n"):
    """Print colored text"""
    style = Colors.BOLD if bold else ''
    print(f"{style}{color}{text}{Colors.END}", end=end)

def create_glowing_x():
    """Create a glowing X effect"""
    glow_layers = [
        f"{Colors.BRIGHT_RED}{Colors.BOLD}✦{Colors.END}",
        f"{Colors.RED}{Colors.BOLD}✧{Colors.END}",
        f"{Colors.BRIGHT_RED}{Colors.BOLD}X{Colors.END}",
        f"{Colors.RED}{Colors.BOLD}✧{Colors.END}",
        f"{Colors.BRIGHT_RED}{Colors.BOLD}✦{Colors.END}"
    ]
    return f"{Colors.BLINK}{glow_layers[2]}{Colors.END}"

def create_glowing_o():
    """Create a glowing O effect"""
    glow_layers = [
        f"{Colors.BRIGHT_BLUE}{Colors.BOLD}◈{Colors.END}",
        f"{Colors.BLUE}{Colors.BOLD}◇{Colors.END}",
        f"{Colors.BRIGHT_BLUE}{Colors.BOLD}O{Colors.END}",
        f"{Colors.BLUE}{Colors.BOLD}◇{Colors.END}",
        f"{Colors.BRIGHT_BLUE}{Colors.BOLD}◈{Colors.END}"
    ]
    return f"{Colors.BLINK}{glow_layers[2]}{Colors.END}"

def display_title():
    """Display the game title with styling"""
    clear_screen()
    print()
    print_colored("╔" + "═" * 37 + "╗", Colors.CYAN, True)
    print_colored("║" + " " * 11 + "TIC TAC TOE" + " " * 11 + "║", Colors.CYAN, True)
    print_colored("╚" + "═" * 37 + "╝", Colors.CYAN, True)
    print()

def display_board(board):
    """Display the game board with enhanced styling and glowing pieces"""
    def cell(i):
        if board[i] == 'X':
            return create_glowing_x()
        elif board[i] == 'O':
            return create_glowing_o()
        else:
            return f"{Colors.YELLOW}{i+1}{Colors.END}"
    
    print()
    print_colored("┌" + "─" * 5 + "┬" + "─" * 5 + "┬" + "─" * 5 + "┐", Colors.WHITE)
    print_colored(f"│  {cell(0)}  │  {cell(1)}  │  {cell(2)}  │", Colors.WHITE)
    print_colored("├" + "─" * 5 + "┼" + "─" * 5 + "┼" + "─" * 5 + "┤", Colors.WHITE)
    print_colored(f"│  {cell(3)}  │  {cell(4)}  │  {cell(5)}  │", Colors.WHITE)
    print_colored("├" + "─" * 5 + "┼" + "─" * 5 + "┼" + "─" * 5 + "┤", Colors.WHITE)
    print_colored(f"│  {cell(6)}  │  {cell(7)}  │  {cell(8)}  │", Colors.WHITE)
    print_colored("└" + "─" * 5 + "┴" + "─" * 5 + "┴" + "─" * 5 + "┘", Colors.WHITE)
    print()

def move_celebration(player):
    """Show a small celebration when a move is made"""
    sparkle_symbols = ["✨", "⭐", "💫", "🌟"]
    color = Colors.RED if player == 'X' else Colors.BLUE
    
    for i in range(2):
        sparkles = ""
        for _ in range(5):
            sparkles += f"{color}{sparkle_symbols[i % len(sparkle_symbols)]}{Colors.END} "
        print_colored(sparkles, Colors.WHITE)
        time.sleep(0.2)

def get_player_move(board, player):
    """Get player input with enhanced styling and validation"""
    while True:
        player_color = Colors.RED if player == 'X' else Colors.BLUE
        print_colored(f"Player {player_color}{player}{Colors.END}, it's your turn!", Colors.WHITE, True)
        print_colored("Choose a position (1-9): ", Colors.YELLOW, end="")
        
        move = input().strip()
        try:
            idx = int(move) - 1
        except ValueError:
            print_colored("❌ Please enter a valid number from 1 to 9.", Colors.RED)
            time.sleep(1)
            continue
        if idx < 0 or idx > 8:
            print_colored("❌ Number must be between 1 and 9.", Colors.RED)
            time.sleep(1)
            continue
        if board[idx] != ' ':
            print_colored("❌ That spot is already taken. Choose another one.", Colors.RED)
            time.sleep(1)
            continue
        
        # Show move celebration
        move_celebration(player)
        return idx

WIN_COMBINATIONS = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def check_winner(board):
    for a, b, c in WIN_COMBINATIONS:
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_board_full(board):
    return all(cell != ' ' for cell in board)
def firecrackers_animation():
    """Display spectacular firecrackers animation"""
    firecracker_symbols = ["💥", "✨", "🌟", "💫", "⭐", "🔥", "💢", "💨"]
    colors = [Colors.RED, Colors.YELLOW, Colors.MAGENTA, Colors.CYAN, Colors.GREEN, Colors.BLUE]
    
    print()
    # Multiple bursts of firecrackers
    for burst in range(5):
        clear_screen()
        print_colored("🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆", Colors.YELLOW, True)
        print()
        
        # Create explosion patterns
        for row in range(8):
            line = ""
            for col in range(30):
                if (row + col + burst) % 3 == 0:
                    symbol = firecracker_symbols[(row + col + burst) % len(firecracker_symbols)]
                    color = colors[(row + col + burst) % len(colors)]
                    line += f"{color}{symbol}{Colors.END} "
                else:
                    line += "  "
            print_colored(line, Colors.WHITE)
        
        print()
        print_colored("🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆", Colors.YELLOW, True)
        time.sleep(0.4)

def victory_celebration(winner):
    """Display victory celebration animation with firecrackers"""
    print()
    
    # Initial celebration
    for i in range(3):
        print_colored("🎉 " * 15, Colors.YELLOW)
        time.sleep(0.2)
        print_colored("🎊 " * 15, Colors.MAGENTA)
        time.sleep(0.2)
    
    # Firecrackers animation
    firecrackers_animation()
    
    # Final victory message with glow
    print_colored("🎉 " * 15, Colors.YELLOW)
    print()
    print_colored("╔" + "═" * 47 + "╗", Colors.GREEN, True)
    winner_text = f"🎉 PLAYER {create_glowing_x() if winner == 'X' else create_glowing_o()} WINS! 🎉"
    print_colored("║" + " " * 8 + winner_text + " " * 8 + "║", Colors.GREEN, True)
    print_colored("╚" + "═" * 47 + "╝", Colors.GREEN, True)
    print()
    
    # Final sparkle burst
    for i in range(3):
        print_colored("✨ " * 20, Colors.BRIGHT_WHITE)
        time.sleep(0.3)

def visual_sound_effects():
    """Simulate sound effects with visual cues"""
    sound_symbols = ["🔊", "🔉", "🔈", "📢", "🎵", "🎶"]
    for i in range(3):
        for symbol in sound_symbols:
            print_colored(f"{symbol} ", Colors.CYAN, end="")
            time.sleep(0.1)
        print()
        time.sleep(0.2)

def draw_animation():
    """Display draw animation with enhanced effects"""
    print()
    
    # Gentle sparkles for draw
    for i in range(3):
        print_colored("✨ " * 15, Colors.YELLOW)
        time.sleep(0.3)
        print_colored("💫 " * 15, Colors.CYAN)
        time.sleep(0.3)
    
    print_colored("╔" + "═" * 33 + "╗", Colors.YELLOW, True)
    print_colored("║" + " " * 8 + "🤝 IT'S A DRAW! 🤝" + " " * 8 + "║", Colors.YELLOW, True)
    print_colored("╚" + "═" * 33 + "╝", Colors.YELLOW, True)
    
    # Gentle sound effect simulation
    print()
    print_colored("Well played! Both players are equally skilled! 👏", Colors.CYAN, True)
    visual_sound_effects()
    print()

def play_game():
    """Main game loop with enhanced interface"""
    board = [' '] * 9
    current_player = 'X'
    
    display_title()
    print_colored("Welcome to Tic Tac Toe!", Colors.CYAN, True)
    print_colored("Players will take turns placing their marks.", Colors.WHITE)
    print_colored("First player to get 3 in a row wins!", Colors.WHITE)
    print()
    input("Press Enter to start the game...")

    while True:
        clear_screen()
        display_title()
        display_board(board)
        idx = get_player_move(board, current_player)
        board[idx] = current_player

        winner = check_winner(board)
        if winner:
            clear_screen()
            display_title()
            display_board(board)
            victory_celebration(winner)
            break

        if is_board_full(board):
            clear_screen()
            display_title()
            display_board(board)
            draw_animation()
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

def ask_play_again():
    """Ask if players want to play again"""
    print()
    print_colored("Would you like to play again?", Colors.CYAN, True)
    print_colored("Enter 'y' or 'yes' to play again, anything else to quit: ", Colors.YELLOW, end="")
    response = input().strip().lower()
    return response in ['y', 'yes']

def main():
    """Main program entry point"""
    while True:
        play_game()
        if not ask_play_again():
            clear_screen()
            print_colored("╔" + "═" * 37 + "╗", Colors.CYAN, True)
            print_colored("║" + " " * 8 + "Thanks for playing!" + " " * 8 + "║", Colors.CYAN, True)
            print_colored("║" + " " * 10 + "See you next time!" + " " * 10 + "║", Colors.CYAN, True)
            print_colored("╚" + "═" * 37 + "╝", Colors.CYAN, True)
            print()
            break
        clear_screen()

if __name__ == "__main__":
    main()
