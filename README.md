This is an engine that plays the game Balatro. There are two models: one is using expected value and math to compute what the best play in any given situation is. The second model is trained on input data from the YouTube Balatro University, and the model emulates what he does in his videos (specifically, the Completionist++ runs)

It also contains the computer vision model that translates a screen from the game into the inputs of the Balatro engine API.

And finally, it contains the clicker that is able to translate the outputs of the Balatro engine API into actual game inputs.

Milestones:
Math Engine
- Be able to simulate a round of the small blind on red deck, ante 1. The engine should compute what is the best expected value play using probability. Simple because there are no jokers, no arcana cards, no celestial cards, no spectral cards. 
- Create an API of all the possible actions that the engine wants to take

CV Model + Clicker
- Be able to turn the game screens into inputs for the model to use
- Turn outputs from the function to the clicker
- Successfully enter the game, select the red deck, enter small blind, and finish the first round of Balatro and click exit to the shop. Then do nothing for now.


ML Engine