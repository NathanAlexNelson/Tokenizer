import re

def readInputFile(filePath): # Turns file into text or 'reads' the file

def simplifyCode(code): # We need to remove comments and spaces here

def tokenize(code):
    # Code then gets broken down here to tokenized definitions
    tokens = {
        'Keywords': set(['def', 'return', 'print']),
        'Identifiers': set(re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code)),
        'Operators': set(re.findall(r'[-+*/%=]', code)),
        'Delimiters': set(re.findall(r'[(),:]', code)),
        'Literals': set(re.findall(r'\b\d+\b', code))
    }
    return tokens

def printOutput(code): # Output for part 4 needs to be simplified code

def main(fileInput): # Call defs here to make code easy to understand

# Simple if statement to make sure the file matches input so things don't break
if __name__ == "__main__":
    fileInput = "fileInput.txt"  # Replace with the path to your input file
    main(fileInput)
