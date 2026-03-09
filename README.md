
# Advanced Telegram + Web Crypto Wallet (Starter Platform)

This is a more advanced architecture for a personal crypto wallet platform similar to Cwallet.

Features included:

• FastAPI backend
• PostgreSQL database models
• Wallet engine (ETH + ERC20 ready)
• Telegram bot integration
• Deposit watcher worker
• Dark dashboard UI
• Railway deployment ready
• Docker support
• Clean scalable architecture

⚠️ Educational / starter platform. Not production secure for large funds.

--------------------------------------------------

DEPLOY GUIDE (Railway)

1. Create Railway account
https://railway.app

2. Upload project to GitHub

3. Railway → New Project → Deploy from GitHub

4. Add environment variables:

BOT_TOKEN=telegram_token
ETH_RPC=https://rpc.ankr.com/eth
HOT_WALLET_KEY=your_private_key
DATABASE_URL=postgres_connection

5. Add Railway PostgreSQL plugin

6. Start command:

uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT

--------------------------------------------------

Telegram commands:

/start
/balance
/deposit
/withdraw
/tip

--------------------------------------------------
