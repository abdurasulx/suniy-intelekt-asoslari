import random 
def chatbot(savol): 
    javoblar = { 
        "salom": ["Salom! Qanday yordam bera olaman?","Salom, siz bilan muloqot qilish yoqimli!","Assalomu alaykum! Qalaysiz?","Salom! Bugun kayfiyatingiz yaxshimi?"], 
        "isming nima": ["Mening ismim AI-Chatbot.", "Men sun’iy intellektman, ismim yo‘q.", 
            "Ismim AI, men virtual yordamchim.", "Chatbot deb atash mumkin, ismim yo‘q."], 
        "qanday": ["Yaxshi, rahmat! Sizchi?", "Men yaxshi, sizning kayfiyatingiz qanday?", 
            "Ajoyib! Sizni eshitib xursandman.", "Yaxshi, bugun ko‘p ishlayapman.",],
        "nima qilayapsan": ["Men siz bilan suhbatlashayapman!", "Sizning savollaringizga javob beryapman."
," Yangi bilimlarni o‘rganishga tayyorman!", "Suhbatimizni davom ettirayapman."], 
        "xayr": ["Xayr! Yana uchrashguncha!", "Ko‘rishguncha, yaxshi kun tilayman!", 
            "Xayr, sog‘ bo‘ling!", "Yana gaplashamiz, salomat bo‘ling!"]  } 
    savol = savol.lower() 
    for kalit, javob in javoblar.items(): 
        if kalit in savol: 
            return random.choice(javob) 
    return "Kechirasiz, bu savolga javob bera olmayman."

# Chatbot bilan muloqot qilish
print("Chatbot bilan suhbatni boshlang ('chiqish' deb yozsangiz, u tugaydi).") 
while True: 
    user_input = input("Siz: ") 
    if user_input.lower() == "chiqish": 
        print("Chatbot: Xayr!") 
        break 
    javob = chatbot(user_input) 
    print("Chatbot:", javob)
