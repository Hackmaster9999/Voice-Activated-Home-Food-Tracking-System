# Voice-Activated-Home-Food-Tracking-System #
In essence this voice assistant acts as an inventory system for your kitchen.
 
Dependencies needed for install: 
1. SpeechRecognition 
2. pyttsx3
3. pyaudio (On Windows you will need to use the pipwin module to install pyaudio)
4. tkinter (comes with python)

Installation Instructions:
1. Download and install the three above listed dependencies in your terminal.

How to use:
1. Run Inventory_Voice_Assistant. An inventory.csv list will generate. If an inventory is already generated, the system will add items to that inventory.
2. To run voice assistant commands, speak "hey kitchen".
3. You can add or remove items to your inventory when prompted by saying "add" or "remove" followed by the quantity and the item name. So for example, "Add 7 bread" would add 7 bread to inventory and "Remove 7 bread" would remove 7 bread from inventory.
4. To cancel at anytime speak "nevermind". To reopen you must use "hey kitchen"
5. To exit assistant, speak "exit kitchen". You may not utilize the "exit kitchen" command while adding or removing items. You must speak "nevermind" first and then "exit".
6. To clear inventory, say,"clear." You will then be prompted to clear inventory.