Abbreviation Scoring System
This Python program reads a list of names (e.g., tree names) from a file and generates 3-letter abbreviations. It assigns scores to each abbreviation based on custom per-letter scores and character position logic. The best abbreviation candidate for each name is selected and written to an output file.
🗂 Project Contents
text
📂 abbreviation-score/
├── values.txt        # Letter-to-score mappings
├── trees.txt         # Input list of names
├── output.txt        # Output abbreviations per name
└── main.py           
📌 How It Works
Inputs:
trees.txt: A list of string names, one per line (e.g., tree species).

values.txt: A list of letters with associated score values.

Example values.txt Format:

text
A 1
B 3
C 2
...
(Each line includes a letter and its score value separated by a space.)

🚀 Logic Overview
Read Name List:

Reads all names from trees.txt.

Split/Tokenize Name:

Removes non-alphabetic characters.

Splits names into uppercase word tokens.

Generate Abbreviations:

Constructs 3-letter abbreviations:

1st letter is the first character.

2nd and 3rd letters are selected from the rest.

Scores are computed based on:

Character position.

Letter score from values.txt.

Special handling for the letter "E" and word boundaries.

Track Best Abbreviation:

Stores only the lowest-scoring unique abbreviation per name.

Filters out abbreviations used for multiple names.

Save Results:

Writes the name and its abbreviation to output.txt.

📥 Input Files
trees.txt
text
Oak Tree
Maple
Douglas Fir
...
values.txt
text
A 1
B 3
C 2
D 4
E    0
...
(Handles empty middle column for special "E" treatment.)

📝 Output Format
Abbreviation results will be saved to output.txt in the following format:

text
MAPLE
MPL
DOUGLAS FIR
DFI
...
Each name is followed by its optimal abbreviation.

🛠 How to Run
Requirements
Python 3.x

Run the script:
Ensure the files trees.txt and values.txt are in the same directory.

🧠 Customization
Adjust scoring by modifying values.txt.

Modify how tokens are formed in split_name().

Tune abbreviation logic in generate_abbreviations().

🧪 Error Handling
If trees.txt or values.txt are missing, the program will print an error.

Handles malformed values.txt lines gracefully.

🙌 Acknowledgments
This program was designed to experiment with customized abbreviation generation using heuristic scoring logic.



