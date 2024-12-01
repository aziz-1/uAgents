from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low


# Define the uagents agent
user_agent = Agent()
fund_agent_if_low(user_agent.wallet.address())

class TwitterAgentRequest(Model):
    query: str

class TwitterAgentResponse(Model):
    response: str


TWITTER_AGENT_ADDRESS="agent1qw7h8pqmt6tytxdqvcqla2udzgsmk222n8t6n5rt3kusmsadxzq5zm7eems"

@user_agent.on_event("startup")
async def fetch_tweets_handler(ctx: Context):
        ctx.logger.info(user_agent.address)
        await ctx.send(TWITTER_AGENT_ADDRESS, TwitterAgentRequest(query="Vaccine"))

@user_agent.on_message(model=TwitterAgentResponse)
async def handle_request(ctx: Context, sender: str, msg: TwitterAgentResponse):
    ctx.logger.info(msg.response)


# Run the agent
if __name__ == "__main__":
    user_agent.run()