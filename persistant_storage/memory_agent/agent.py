from google.adk.tools.tool_context import ToolContext

def add_reminder(reminder:str , tool_context: ToolContext) -> dict:
 """Add a new reminder to the user's reminder list.
 Args:
  reminder: The reminder text to add 
  tool_context: Context for accessing
 """