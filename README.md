How to Run the Project Locally

First make sure you have Python 3.9 or higher installed on your system.

Clone the repository and move into the project folder. Then create and activate a virtual environment. After activating the environment, install the required dependencies using the requirements.txt file.

Set your OpenAI API key as an environment variable on your system. This is required for intent detection using GPT-4o-mini. Make sure you restart VS Code or your terminal after setting the key.

Once everything is set up, you can run the project by executing the main Python file. The agent will start in the terminal and you can interact with it by typing messages. You can test greetings, pricing questions, and high intent messages to see the full lead capture flow.

Architecture Explanation

I chose LangGraph because the assignment focuses on building an agent with clear control over conversation flow and state. LangGraph allows defining explicit nodes and transitions, which makes the agent predictable and easier to debug compared to free flowing chains. This was especially important for handling multi turn lead capture without triggering actions prematurely.

The project is structured around a central state object that is passed through the graph on every user interaction. This state stores the user message, detected intent, current step in the conversation, retrieved knowledge context, and lead details such as name, email, and platform. Because the same state object is reused across turns, the agent is able to remember context across five or more messages without relying on external memory stores.

Intent detection is handled using GPT-4o-mini, while knowledge based responses use a local JSON file through a simple retrieval module. Tool execution for lead capture is strictly guarded by state checks, ensuring it only runs after all required information is collected. This design keeps the agent reliable, explainable, and aligned with real world production patterns.

WhatsApp Deployment Explanation

To deploy this agent on WhatsApp, I would use the WhatsApp Business Cloud API along with a webhook based backend service. The backend would be built using a lightweight framework like FastAPI.

Incoming WhatsApp messages would be sent to a webhook endpoint by Meta. The webhook handler would extract the user message and map the WhatsApp user ID to a stored conversation state. This state would then be passed to the LangGraph agent in the same way as local input.

The agent response would be returned by the graph and sent back to the user through the WhatsApp API as a reply message. State would be stored per user using an in memory store like Redis or a database, allowing conversations to persist across messages.

This setup allows the same agent logic to run unchanged, with only the input and output layers adapted for WhatsApp.