import random
from datetime import datetime
import string

class CodeOfTheDayGenerator:
    """Advanced and creative generator for a 'Code of the Day' with complex logic."""

    def __init__(self):
        self.categories = {
            "motivation": [
                "Keep pushing your limits!",
                "Success is the sum of small efforts repeated daily.",
                "Think twice, code once.",
                "Every great developer you know got there by solving problems they were unqualified to solve until they actually did it."
            ],
            "humor": [
                "Write code as if the person maintaining it is a violent psychopath who knows where you live.",
                "Code is like humor. When you have to explain it, it’s bad.",
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "A SQL query walks into a bar, goes up to two tables, and says 'Can I join you?'"
            ],
            "philosophy": [
                "Simplicity is the soul of efficiency.",
                "Great coders are not born; they are self-taught.",
                "First, solve the problem. Then, write the code.",
                "Programming is the art of algorithm design and the craft of debugging errant code."
            ]
        }

    def generate_random_category(self):
        """Randomly select a category."""
        return random.choice(list(self.categories.keys()))

    def generate_unique_code(self, category):
        """Generate a unique and creative code based on the category."""
        base_message = random.choice(self.categories[category])
        unique_hash = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"[{timestamp}] [{category.upper()}] {base_message} [ID-{unique_hash}]"

    def get_code_of_the_day(self):
        """Generate the full 'Code of the Day' with advanced logic."""
        category = self.generate_random_category()
        return self.generate_unique_code(category)

# Complex usage with advanced output logic
if __name__ == "__main__":
    generator = CodeOfTheDayGenerator()
    for _ in range(3):  # Generate multiple codes to showcase diversity
        print(generator.get_code_of_the_day())
