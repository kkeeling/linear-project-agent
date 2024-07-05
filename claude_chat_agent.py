from anthropic import Anthropic
from tools.read_txt_file import read_txt_file, read_txt_file_tool
from tools.read_binary_file import read_binary_file, read_binary_file_tool

class ClaudeChatAgent:
    def __init__(self, api_key):
        self.anthropic = Anthropic(api_key=api_key)
        self.conversation_history = []
        self.tools = [read_txt_file_tool, read_binary_file_tool]

    def chat_with_claude(self, message):
        try:
            response = self.anthropic.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1024,
                messages=self.conversation_history + [{"role": "user", "content": message}],
                tools=self.tools
            )
            return response
        except Exception as e:
            return f"Error communicating with Claude: {str(e)}"

    def process_tool_calls(self, tool_calls):
        results = []
        for call in tool_calls:
            if call.type == 'function':
                function_name = call.function.name
                arguments = call.function.arguments

                if function_name == 'read_txt_file':
                    file_path = arguments.get('file_path')
                    result = read_txt_file(file_path)
                elif function_name == 'read_binary_file':
                    file_path = arguments.get('file_path')
                    result = read_binary_file(file_path)
                else:
                    result = f"Unknown function: {function_name}"

                results.append({
                    "tool_call_id": call.id,
                    "output": str(result)
                })
        return results

    def chat(self, user_input):
        claude_response = self.chat_with_claude(user_input)

        if isinstance(claude_response, str):  # Error occurred
            return claude_response

        if claude_response.tool_calls:
            tool_results = self.process_tool_calls(claude_response.tool_calls)
            tool_response = self.chat_with_claude("Tool execution results")
            if isinstance(tool_response, str):  # Error occurred
                return tool_response
            self.update_conversation_history(user_input, claude_response.content, tool_results, tool_response.content)
            return tool_response.content
        else:
            self.update_conversation_history(user_input, claude_response.content)
            return claude_response.content

    def update_conversation_history(self, user_input, assistant_response, tool_results=None, tool_response=None):
        self.conversation_history.extend([
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": assistant_response}
        ])
        if tool_results:
            self.conversation_history.extend([
                {"role": "user", "tool_results": tool_results},
                {"role": "assistant", "content": tool_response}
            ])
        # Limit conversation history to last 10 messages to manage token usage
        self.conversation_history = self.conversation_history[-10:]