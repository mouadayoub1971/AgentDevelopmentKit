from google.adk.agents import Agent
from datetime import datetime
from google.adk.tools import google_search

def current_time() -> dict :
 """
 Get the current time in the format YYYY-MM-DD HH-MM-SS
 """

 return {
  "current_time" : datetime.now().strftime("%Y-%m-%d %H-%M-%S")
 }


root_agent = Agent(
 name="greeting_agent",
 model="gemini-2.0-flash",
 description="this is the greeting agent ",
 instruction="""
 your are a helpful assistant  that use the following tools 
 """ ,
)