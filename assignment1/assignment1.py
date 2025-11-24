# # Task1 : Hello
print('Task 1 : Hello!')

# # Task2 : Greet with a Formatted String
name = "Neesha"
def greetFunc(name: str) -> str:
    return f"Hello, {name}!"
print(greetFunc(name))

# Task3 : Calculator

# def myCalc(a, b, operation="multiply"):
#     match operation:
#         case "add":
#             return a + b
#         case "subtract":
#             return a - b 
#         case "multiply":
#             return a * b
#         case "divide":
#             return a / b
#         case "modulo":
#             return a % b
#         case "int_divide":
#             return a // b
#         case "power":
#             return a ** b
#         case _: 
#             return "Wrong"
    
# print(myCalc(3, 5, "add"))

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

def checkGrades(*args):
    score = args[0]
    if score >= 90:
        print("A")
    elif score >= 80:
        print ("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print ("C")

checkGrades(90)

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
                best_student = max(kwargs, key=kwargs.get)
                return f"Best Student: {best_student}"
        elif option == "mean":
                mean_score = sum(kwargs.values()) / len(kwargs)
                return f"Mean Score: {mean_score}"
        else: 
             return "Chose 'best' or 'mean' ."

print(student_scores("best", Maya=80, John=90, Julie=85))
print(student_scores("mean", Summer=10, Liya=30, Ruth=5))

# Task 8: Titleize, with String and List Operations

#sentence = "i like coffee And tea A lot."
#words = "i, like, coffee, and, tea, a, lot."
def titleize(sentence):
    split_words = sentence.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    new_word = []
    for i, word in enumerate(split_words):
        if i == 0:
            word = word.capitalize()
        elif i == len(split_words) - 1:
            word = word.capitalize()
        else:
            if word.lower() in little_words:
                word = word.lower()
            else: 
                word = word.capitalize()
        new_word.append(word)
    return "Task 8 :" + " ".join(new_word)
        

print(titleize ("i like coffee And tea A lot."))

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
            # check for special case rule 3
            if word[:2] == "qu":
                pig_word = word[2:] + "quay"
            else:
                # Rule 2: move leading consonants to the end
                consonant_cluster = ""
                for letter in word:
                    if letter in vowels:
                        break
                    else:
                        consonant_cluster += letter
                pig_word = word[len(consonant_cluster):] + consonant_cluster + "ay"
        
        result.append(pig_word)
    
    return " ".join(result)

print(pig_latin("angel world quack"))



