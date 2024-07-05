from anthropic import Anthropic
from tools.read_txt_file import read_txt_file, read_txt_file_tool
from tools.read_binary_file import read_binary_file, read_binary_file_tool

class ClaudeChatAgent:
    def __init__(self, api_key):
        self.anthropic = Anthropic(api_key=api_key)
        self.conversation_history = []
        self.tools = [read_txt_file_tool, read_binary_file_tool]
        self.system_prompt = self.read_system_prompt()

    def read_system_prompt(self):
        try:
            with open("system_prompt.md", "r") as file:
                return file.read().strip()
        except FileNotFoundError:
            print("Warning: system_prompt.md file not found. Using default system prompt.")
            return "You are a helpful AI assistant."

    def chat_with_claude(self, message):
        try:
            response = self.anthropic.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1024,
                system=self.system_prompt,
                messages=[
                    *self.conversation_history,
                    {"role": "user", "content": message}
                ],
                tools=self.tools
            )
            return response
        except Exception as e:
            return f"Error communicating with Claude: {str(e)}"

    def process_tool_calls(self, tool_calls):
        results = []
        for call in tool_calls:
            if call.type == 'tool_use':
                tool_name = call.name
                tool_input = call.input

                if tool_name == 'read_txt_file':
                    file_path = tool_input.get('file_path')
                    result = read_txt_file(file_path)
                elif tool_name == 'read_binary_file':
                    file_path = tool_input.get('file_path')
                    result = read_binary_file(file_path)
                else:
                    result = f"Unknown tool: {tool_name}"

                results.append({
                    "type": "tool_result",
                    "tool_use_id": call.id,
                    "content": str(result)
                })
        return results

    def chat(self, user_input):
        claude_response = self.chat_with_claude(user_input)

        if isinstance(claude_response, str):  # Error occurred
            return claude_response

        if claude_response.content:
            for content_block in claude_response.content:
                if content_block.type == 'tool_use':
                    tool_results = self.process_tool_calls([content_block])
                    tool_response = self.chat_with_claude({"role": "user", "content": tool_results})
                    if isinstance(tool_response, str):  # Error occurred
                        return tool_response
                    self.update_conversation_history(user_input, claude_response.content, tool_results, tool_response.content)
                    return tool_response.content
            
            # If no tool use, just return the content
            self.update_conversation_history(user_input, claude_response.content)
            return claude_response.content
        else:
            return "No response from Claude."

    def update_conversation_history(self, user_input, assistant_response, tool_results=None, tool_response=None):
        self.conversation_history.extend([
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": assistant_response}
        ])
        if tool_results:
            self.conversation_history.extend([
                {"role": "user", "content": tool_results},
                {"role": "assistant", "content": tool_response}
            ])
        # Limit conversation history to last 10 messages to manage token usage
        self.conversation_history = self.conversation_history[-10:]