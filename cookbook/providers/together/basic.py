from phi.agent import Agent, RunResponse  # noqa
from phi.model.together import Together

agent = Agent(
    model=Together(id="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo"),
    instructions=["Respond in a southern tone"],
    markdown=True
)

# Get the response in a variable
# run: RunResponse = agent.run("Explain simulation theory")
# print(run.content)

# Print the response on the terminal
agent.print_response("Explain simulation theory")