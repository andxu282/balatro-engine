import matplotlib.pyplot as plt
from PIL import Image

def get_coords(img_path):
    all_coords = {
        # "score": [],
        # "current_score": [],
        # "num_hands": [],
        # "num_discards": [],
        # "hand_size": [],
        # "card_1": [],
        # "card_2": [],
        # "card_3": [],
        # "card_4": [],
        # "card_5": [],
        # "card_6": [],
        # "card_7": [],
        "card_8": [],
    }
    for key in all_coords:
        img = Image.open(img_path)
        plt.imshow(img)
        plt.title("Click corners for cropping")
        coords = plt.ginput(2)  # click top-left then bottom-right
        coords = [int(coord) for coord_tuple in coords for coord in coord_tuple]
        plt.close()
        all_coords[key] = coords
    return all_coords

print(get_coords("test_assets/test1.png"))