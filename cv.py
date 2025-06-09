from PIL import Image
from models import GameState, Card, Deck
import pytesseract

def read_screen(image_path: str) -> GameState:
    # Load image
    image = Image.open(image_path)
    image = image.convert("L")
    crop_coords = {
        'score': ([569, 591, 716, 679], 64, '--psm 6 digits'),
        'current_score': ([315, 900, 832, 1007], 64, '--psm 6 digits'),
        'num_hands': ([455, 1531, 532, 1636], 64, '--psm 6 digits'),
        'num_discards': ([706, 1528, 779, 1632], 64, '--psm 6 digits'),
        'hand_size': ([1899, 1771, 1928, 1808], 64, '--psm 6 digits'),
    }

    game_state_dict = {}
    
    for key, (coords, threshold, config) in crop_coords.items():
        crop = image.crop(coords)
        crop = crop.point(lambda x: 255 if x > threshold else 0, mode='1')
        crop = crop.resize((crop.width * 4, crop.height * 4))
        crop.show()
        text = pytesseract.image_to_string(crop, config=config)
        game_state_dict[key] = text
        print(key, text)
    
    hand = read_cards(image)

    game_state = GameState(
        hand=hand,
        deck=Deck(),
        num_hands=game_state_dict['num_hands'],
        num_discards=game_state_dict['num_discards'],
        score=game_state_dict['score'],
        current_score=game_state_dict['current_score'],
        hand_size=game_state_dict['hand_size']
    )

    return game_state

def read_cards(image: Image.Image) -> Deck:
    # crop_coords = {
    #     'card_1': ([929, 1385, 988, 1472], 128),
    #     'card_2': ([1170, 1378, 1222, 1462], 128),
    #     'card_3': ([1403, 1364, 1445, 1455], 128),
    #     'card_4': ([1633, 1347, 1678, 1437], 128),
    #     'card_5': ([1873, 1343, 1908, 1434], 128),
    #     'card_6': ([2107, 1354, 2149, 1430], 128),
    #     'card_7': ([2347, 1357, 2372, 1444], 128),
    #     'card_8': ([2574, 1354, 2626, 1465], 128)
    # }

    # cards = []
    # for key, (coords, threshold) in crop_coords.items():
    #     crop = image.crop(coords)
    #     crop = crop.point(lambda x: 255 if x > threshold else 0, mode='1')
    #     crop = crop.resize((crop.width * 4, crop.height * 4))
    #     text = pytesseract.image_to_string(crop, config=config)
    #     cards.append(text)

    # hand = Deck([Card(card) for card in cards])  

    return Deck()

def main():
    game_state = read_screen("test_assets/test1.png")
    print(game_state)

if __name__ == "__main__":
    main()