from langchain.agents import create_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    model="ollama:mistral",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
# agent.invoke(
#     {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
# )

if __name__ == "__main__":
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in blr"}]}
    )

    # print(response)

    final_message = response["messages"][-1].content
    print(final_message)
