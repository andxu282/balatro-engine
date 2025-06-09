from models import GameState
from calculator import get_best_combo, get_score
from cv import read_screen

def main():
    game_state: GameState = read_screen("test_assets/test1.png")
    combo = get_best_combo(game_state, game_state.current_score)
    print("best combo", combo)
    print("score", get_score(combo))

if __name__ == "__main__":
    main()