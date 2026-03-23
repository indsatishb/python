import datetime
import time
presentHour= datetime.datetime.now().hour
name=input("Enter Your Name : ")
if 5<= presentHour <=11:
    print("Good Morning ", name)
elif 12<= presentHour <=16:
    print("Good After Nood ", name)
else:
    print("Good Evening ", name)


print("Namste ! Welcome To Rule Based Chatbot")
print("You Can Ask Me Basic Question , Type bye to exit from the bot")
#chatbot memory Creation [Dictionary Of Responces]
responces = {
    "hello": "Hi, welcome! How can I help you?",
    "hi": "Hello! Kaise ho?",
    "hey": "Hey there! 😊",
    "how are you": "I am fine. Thank you!",
    "what is your name": "I am your chatbot friend 🤖",
    "who are you": "I am a smart AI chatbot",
    "bye": "Goodbye! Have a nice day 👋",
    "good morning": "Good morning! 🌞",
    "good night": "Good night! 🌙",
    "good evening": "Good evening! 😊",

    "thanks": "You are welcome!",
    "thank you": "Glad to help!",
    "ok": "Alright 👍",
    "fine": "Great!",
    "nice": "Glad you liked it 😊",

    "motivate me": "Keep going! You can do it 💪",
    "i am sad": "Don't worry, everything will be fine ❤️",
    "i am happy": "That's awesome 😄",
    "bored": "Try learning something new!",
    "tired": "Take some rest 😴",

    "what is python": "Python is a programming language.",
    "what is function": "Function ek block of code hota hai.",
    "what is list": "List ek collection hai jo change ho sakta hai.",
    "what is tuple": "Tuple immutable collection hota hai.",
    "what is dictionary": "Dictionary key-value pair store karta hai.",
    "what is set": "Set unique values store karta hai.",

    "what is loop": "Loop repeat karne ke liye use hota hai.",
    "for loop": "For loop iterable pe run karta hai.",
    "while loop": "While loop condition ke basis pe chalta hai.",
    "break": "Break loop ko stop karta hai.",
    "continue": "Continue next iteration pe le jata hai.",

    "what is variable": "Variable data store karne ke liye use hota hai.",
    "what is string": "String text data hota hai.",
    "what is int": "Integer whole number hota hai.",
    "what is float": "Float decimal number hota hai.",

    "what is class": "Class blueprint hota hai object ka.",
    "what is object": "Object class ka instance hota hai.",
    "oops": "OOPs ka matlab object oriented programming hai.",

    "what is html": "HTML webpage banane ke liye use hota hai.",
    "what is css": "CSS design ke liye use hota hai.",
    "what is javascript": "JavaScript web ko interactive banata hai.",

    "what is ai": "AI machines ko smart banata hai.",
    "what is machine learning": "ML data se learning karta hai.",
    "what is chatbot": "Chatbot user se baat karne wala program hai.",

    "time": "Sorry, mujhe current time nahi pata 😅",
    "date": "Mujhe date bhi nahi pata 😅",
    "your creator": "Mujhe ek developer ne banaya hai 👨‍💻",

    "tell joke": "Why do programmers hate bugs? Because they bug them 😄",
    "funny": "Haha 😄",
    "sing": "Sorry, main ga nahi sakta 🎤",

    "study tips": "Daily thoda-thoda padhai karo.",
    "exam fear": "Practice se fear khatam hota hai.",
    "coding tips": "Practice makes perfect 💻",
    "error": "Error se hi learning hoti hai.",
    "debug": "Debug patiently karo 🐞",

    "food": "Mujhe khana nahi lagta 😄",
    "travel": "Travel is fun! ✈️",
    "books": "Books knowledge deti hain 📚",
    "mobile": "Mobile useful hai but limit me use karo",

    "india": "India ek beautiful country hai 🇮🇳",
    "bihar": "Bihar ek historical state hai 😊",
    "patna": "Patna Bihar ki capital hai",

    "weather": "Mujhe weather info nahi pata 😅",
    "news": "Latest news ke liye internet check karo",

    "love": "Love is beautiful ❤️",
    "friend": "Friends life ko awesome banate hain 😊",

    "game": "Game khelna fun hai 🎮",
    "cricket": "Cricket India me popular hai 🏏",
    "football": "Football world famous hai ⚽",

    "money": "Money important hai 💰",
    "job": "Job ke liye skills develop karo",
    "government job": "Preparation consistent rakho",

    "sleep": "Proper sleep lena zaruri hai 😴",
    "health": "Health is wealth 💪",
    "exercise": "Daily exercise karo",

    "music": "Music mood fresh karta hai 🎵",
    "movie": "Movie dekhna fun hai 🎬",

    "internet": "Internet knowledge ka source hai 🌐",
    "google": "Google sabka dost hai 😄",

    "help": "Main yaha help ke liye hoon 😊",
    "support": "Always here to support you 💙",

    "goal": "Apne goal pe focus karo 🎯",
    "success": "Hard work se success milti hai",
    "failure": "Failure se hi success aata hai",

    "learn python": "Start with basics and practice daily",
    "project idea": "Expense tracker, chatbot bana sakte ho",
    "portfolio": "Projects se portfolio strong banta hai",

    "college": "College life important hoti hai",
    "school": "School basics strong karta hai",

    "future": "Future bright hai ✨",
    "dream": "Dream big 💭",

    "exit": "Bye! 👋"
}
#take user input

def getResponceOfBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in responces:
        if eachKey in userQuestion:
            return responces[eachKey]
    return "I am not able to tell that yet "

while True:
    takeInput=input(f"{name} Ask : ")
    reply=getResponceOfBot(takeInput)
    print(f"Bot : {reply}")

    if "bye" in takeInput:
        print("Thank You ! Good Bye")
        break