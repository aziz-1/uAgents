from uagents import Agent, Context
import random
from datetime import datetime, timedelta

agent = Agent()


MY_WALLET_ADDRESS = "fetch1___"

def generate_synthetic_data(num_articles=10):
    """Generate synthetic news data with titles, dates, and URLs."""
    sample_titles = [
        "Global health conference announces new vaccine",
        "Pandemic prevention strategies discussed at summit",
        "WHO launches campaign to tackle misinformation",
        "New guidelines for infection control released",
        "Global equity in vaccine distribution highlighted",
        "Breakthrough research in pandemic response unveiled",
        "International health forum addresses emerging threats",
        "New health advisory for seasonal infections issued",
        "Advances in healthcare technology shared at conference",
        "Emergency response plans for infectious diseases updated",
    ]

    synthetic_data = []
    base_url = "https://synthetic-news.org/item/"
    today = datetime.now()

    for i in range(num_articles):
        title = random.choice(sample_titles)
        date = today - timedelta(days=random.randint(0, 30))  # Random date within the last 30 days
        link = f"{base_url}{i+1}"
        synthetic_data.append({
            "date": date.strftime("%d %B %Y"),
            "title": title,
            "link": link
        })

    return synthetic_data

@agent.on_interval(period=3600)
async def log_synthetic_updates(ctx: Context):
    """Fetch synthetic news updates and log them."""
    updates = generate_synthetic_data(num_articles=10)
    for update in updates:
        alert = f"{update['date']} - {update['title']} - Read more: {update['link']}"
        ctx.logger.info(alert)
        if MY_WALLET_ADDRESS != "fetch1___":
            await ctx.send_wallet_message(MY_WALLET_ADDRESS, alert)

if __name__ == "__main__":
    agent.run()
