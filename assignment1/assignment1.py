# # Task1 : Hello
def hello():
    return ("Hello!")

# # Task2 : Greet with a Formatted String
name = "Neesha"
def greet(name: str) -> str:
    return f"Hello, {name}!"
print(greet(name))

# Task3 : Calculator

def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b             
            case "subtract":
                 return a - b 
            case "multiply":
                return a * b             
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b             
            case _: 
                return "Wrong"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return f"You can't multiply those values!"
    
print(calc(3, 5, "add"))

# Task4: DataTypeConversion

def data_type_conversion(input, dataType):
    # try/except for handling error instead of crashing 
    try:
        if dataType == "int":
            return int(input)
        elif dataType == "float":
            return float(input)
        elif dataType == "str":
            return str(input)
        else: 
            return f"You can't convert {input} into a {dataType}."
    except ValueError:
        return f"You can't convert {input} into a {dataType}."
    
print(data_type_conversion("Leo", "float"))

# Task5: Grading System, Using *args

def grade(*args):
    try:
        if len(args) == 0:
            return "Invalid data was provided."
        
        average = sum(args)/ len(args)

        if average >= 90:
            return "A"
        elif average>= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ValueError):
        return "Invalid data was provided."
    
grade("three", "blind", "mice")
    
# Task 6: Use a For Loop with a Range

def repeat(string, count):
    newStr = "" 
    # range + for loop
    for i in range(count): 
        newStr += string
    return newStr

print(repeat("Hello ", 5).strip())

# Task 7: Student Scores, Using **kwargs

def student_scores(option, **kwargs):
        if option == "best":
                return max(kwargs, key=kwargs.get)
        elif option == "mean":
                return sum(kwargs.values()) / len(kwargs)
              

print(student_scores("best", Maya=80, John=90, Julie=85))
print(student_scores("mean", Summer=10, Liya=30, Ruth=5))

# Task 8: Titleize, with String and List Operations

#sentence = "i like coffee And tea A lot."
#words = "i, like, coffee, and, tea, a, lot."
def titleize(sentence):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = sentence.split()
    new_word = []
    
    for i, word in enumerate(words):
        if i == 0:
            word = word.capitalize()
        elif i == len(words) - 1:
            word = word.capitalize()
        else:
            if word.lower() in little_words:
                word = word.lower()
            else: 
                word = word.capitalize()
        new_word.append(word)
    return " ".join(new_word)
        

titleize("war and peace")
titleize("a separate peace")
titleize("after on")

# Task 9: Hangman, with more String Operations
def hangman(secretWord, guessLetters):
    secretWordLower = secretWord.lower()
    guessLettersLower = guessLetters.lower()

    result = ""
    for letter in secretWordLower:
        #compare with guess letter
        if letter in guessLettersLower:
            # Preserve original case
            originalIndex = secretWordLower.index(letter)
            result += secretWord[originalIndex]
        else:
            result += "_"
    return result

secretWord = "alphabet"
guess = "ab"
print(hangman(secretWord, guess))



# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:
        # rule 1: containg vowels
        if word[0] in vowels:
            pig_word = word + "ay"
        else:
            #rule2 & 3
            consonant_cluster = ""
            i = 0
            while i < len(word):
            # check for special "qu" case
                if word[i:i+2] == "qu":
                    i += 2
                    break
                elif word[i] in vowels:
                    break
                else:
                    i += 1
            pig_word = word[i:] + word[:i] + "ay"
        
        result.append(pig_word)
    
    return " ".join(result)

print(pig_latin("square"))



