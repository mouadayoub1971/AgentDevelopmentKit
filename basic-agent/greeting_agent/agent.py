from google.adk.agents import Agent

root_agent = Agent(
 name="greeting_agent",
 model="gemini-2.0-flash",
 description="this is the greeting agent ",
 instruction="""
 your are a helpful ai agent that greets the user.
 Ask for the user's name then greet them by name .
 """
)