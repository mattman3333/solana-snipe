# Solana Token Sniper Application

#### Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file in the `config` directory with the following variables:
   - TWITTER_API_KEY
   - TWITTER_API_SECRET_KEY
   - TWITTER_ACCESS_TOKEN
   - TWITTER_ACCESS_TOKEN_SECRET
   - SOLANA_RPC_URL
   - PRIVATE_KEY

#### Usage
1. Start the application: `python src/main.py`.
2. Monitor specified Twitter accounts and execute buy orders automatically.

#### Troubleshooting
- Check logs in `logs/app.log`.
- Ensure all environment variables are correctly set.