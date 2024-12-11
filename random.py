import random
from datetime import datetime

# Code of the Day Generator
def generate_code_of_the_day():
    messages = [
        "Keep pushing your limits!",
        "Every line of code is a step closer to mastery.",
        "Debugging is twice as hard as writing the code in the first place.",
        "Success is the sum of small efforts repeated daily.",
        "Write code as if the person maintaining it is a violent psychopath who knows where you live.",
        "Simplicity is the soul of efficiency.",
        "Great coders are not born; they are self-taught.",
        "Think twice, code once.",
        "Code is like humor. When you have to explain it, it’s bad.",
        "Work smarter, not harder."
    ]
  
    today = datetime.now().strftime("%Y-%m-%d")
    message = random.choice(messages)

    code_of_the_day = f"[{today}] Code of the Day: {message}"
    return code_of_the_day

# Display the code of the day
if __name__ == "__main__":
    print(generate_code_of_the_day())
