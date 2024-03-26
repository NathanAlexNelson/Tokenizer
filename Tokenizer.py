import re


def readInputFile(filePath):
  with open(filePath, 'r') as file:
    return file.read()


def simplifyCode(code):
  # Remove comments and spaces
  code = re.sub(r'#.*?\n', '\n', code)
  code = re.sub(r'\s+', ' ', code)
  return code.strip()


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


def printOutput(code):
  # Output for part 4.
  print("Output1 - Code after removing excess space and comments:")
  print(code)


def printOutput2(code):
  # Sort of complicated looking but this is where the code gets printed in tabular form
  print("\nOutput2 - Tokenized code in tabular form:")
  print("Category\tTokens")
  for category, tokens in code.items():
    print(f"{category}\t{', '.join(tokens)}")


def main(fileInput):
  code = readInputFile(fileInput)
  processedCode = simplifyCode(code)
  printOutput(processedCode)
  tokenizedCode = tokenize(processedCode)
  printOutput2(tokenizedCode)


if __name__ == "__main__":
  fileInput = "fileInput.txt"  # Replace with the path to your input file
  main(fileInput)
