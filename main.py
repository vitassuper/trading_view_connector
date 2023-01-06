from threading import Thread
from src.bot.telegram import run as run_telegram
from uvicorn import run as run_uvicorn
from uvicorn.config import LOGGING_CONFIG
from src.core.config import settings

def main():
    LOGGING_CONFIG["formatters"]["access"]["fmt"] = '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'

    run_uvicorn("src.server.server:app", host='0.0.0.0', port=80, log_level="info", reload=settings.DEBUG_MODE)
    t = Thread(target=run_telegram, daemon=True)
    t.start()

if __name__ == "__main__":
    main()
