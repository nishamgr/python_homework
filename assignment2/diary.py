# -------Task:1 Diary-------
import traceback

try:

    diary_file = open("diary.txt", "a")
    user_input = input("What happened today? ")

    while True:

        diary_file.write(user_input + "\n")    
        if user_input == "done for now":
            break
        user_input = input("What else? ")
    diary_file.close()

except Exception as e:
    print("An exception ooccurred", type(e).__name__ )
    traceback.print_exc()



