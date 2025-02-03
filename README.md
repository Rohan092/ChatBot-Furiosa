# ChatBot Furiosa
Chatbot Overview: Furiosa Chat<br/>
Furiosa Chat is an AI-powered chatbot built using Flask and Cohere's language generation API. It serves as an interactive conversational agent that can understand and respond to user inputs with natural language.

# Features:
• Conversational AI: Utilizes Cohere's language model to generate human-like responses.<br/>
• Dynamic Interaction: Accepts user messages via a web interface and returns meaningful replies.<br/>
• Custom Termination: Recognizes keywords like "quit," "exit," or "bye" to gracefully end the conversation.<br/>
• Flexible Configurations: Allows tuning of response characteristics using parameters like max_tokens and temperature.<br/>

# Key Components

## 1. Flask Web Application:
Routes:<br/>
• /: Renders the main HTML page (FuriosaChat.html) for user interaction.<br/>
• /get: Handles AJAX requests from the front end, receiving user messages and returning the chatbot's responses.<br/>

## 2. Cohere API Integration:
• Utilizes the Cohere NLP model to generate responses based on user input.<br/>
• Configured with parameters like max_tokens (to control response length) and temperature (to influence creativity).<br/>

## 3. Conversation Management:
•Basic command handling: Recognizes commands like "quit", "exit", and "bye" to end the conversation gracefully.<br/>

# How It Works

• User Interaction: The user sends a message via the web interface.<br/>
• Backend Processing: The Flask route /get captures the message and forwards it to the chat_with_Furiosa function.<br/>
• Response Generation: chat_with_Furiosa sends the message to Cohere's API, retrieves a generated response, and returns it to the user.<br/>
• Ending the Chat: Specific keywords prompt the bot to respond with a goodbye message.<br/>

# Technical Stack:
• Backend: Flask (Python) for handling HTTP requests and routing.<br/>
• AI Engine: Cohere API for generating AI-driven responses.<br/>
• Frontend: HTML template (FurisoaChat.html) for user interaction.<br/>

# Repository Structure
• Data : https://github.com/Rohan092/ChatBot-Furiosa/blob/main/Furiosa%20Decode.zip<br/>
• Outputs :![Furiosa 1](https://github.com/user-attachments/assets/903fe1b8-31bd-41e5-995b-af6a1d280169)<br/>
![Furiosa 2](https://github.com/user-attachments/assets/bfd064f2-346f-4bae-b1ac-b1f494a7be56)<br/>
![Furiosa 3](https://github.com/user-attachments/assets/9d798853-e175-496a-b7fa-3c217a225105)<br/>


# Feedback & Collabration
Your feedback is always appreciated! If you’re interested in collaborating on similar projects or discussing new opportunities, feel free to reach out. I’m always open to connecting and sharing insights!
