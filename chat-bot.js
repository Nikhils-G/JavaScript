// Simulate a basic chat system with dynamic and realistic conversation

class ChatBot {
  constructor() {
    this.history = [];
    this.responses = [
      "I'm here to help! What can I do for you?",
      "That's interesting, tell me more!",
      "I'm not sure about that. Could you elaborate?",
      "Great question! Here's my take on it...",
      "Hmm, I don't have an answer for that. Let me think...",
      "Got it! Let me look into it and get back to you.",
      "I think you're onto something! Let's explore that more."
    ];
  }

  generateResponse(input) {
    // Simple AI for dynamically generating responses based on input
    let response;
    if (input.toLowerCase().includes("hello") || input.toLowerCase().includes("hi")) {
      response = "Hello! How can I assist you today?";
    } else if (input.toLowerCase().includes("thank you") || input.toLowerCase().includes("thanks")) {
      response = "You're welcome! Let me know if you need anything else.";
    } else {
      response = this.responses[Math.floor(Math.random() * this.responses.length)];
    }

    return response;
  }

  addToHistory(input, response) {
    // Store the conversation history
    this.history.push({ user: input, bot: response });
  }

  getConversationHistory() {
    return this.history.map(convo => `User: ${convo.user} \nBot: ${convo.bot}`).join('\n\n');
  }
}

// HTML elements for chat UI interaction
const chatBot = new ChatBot();
const chatBox = document.getElementById('chatBox');
const inputField = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');
const historyButton = document.getElementById('historyButton');

// Send button click event
sendButton.addEventListener('click', () => {
  const userInput = inputField.value;
  if (userInput.trim()) {
    const botResponse = chatBot.generateResponse(userInput);
    chatBot.addToHistory(userInput, botResponse);
    
    // Display the user input and bot response in the chat box
    const newMessage = document.createElement('div');
    newMessage.classList.add('message');
    newMessage.innerHTML = `<strong>User:</strong> ${userInput}<br><strong>Bot:</strong> ${botResponse}`;
    chatBox.appendChild(newMessage);
    
    // Clear the input field
    inputField.value = '';
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the latest message
  }
});

// History button click event
historyButton.addEventListener('click', () => {
  const history = chatBot.getConversationHistory();
  alert(`Chat History:\n\n${history}`);
});
