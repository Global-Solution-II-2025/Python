import oracledb
from app.config import settings
from contextlib import contextmanager

pool = None

def init_db():
    global pool
    # create_pool expects dsn, user, password
    try:
        pool = oracledb.create_pool(
            user=settings.ORACLE_USER,
            password=settings.ORACLE_PASSWORD,
            dsn=settings.ORACLE_DSN,
            min=1, max=5, increment=1
        )
        print("Oracle DB pool created.")
    except Exception as e:
        print("Warning: could not create Oracle pool:", e)
        pool = None

@contextmanager
def get_connection():
    """
    Use with: with get_connection() as conn:
    Returns a connection or raises.
    """
    global pool
    if pool:
        conn = pool.acquire()
        try:
            yield conn
        finally:
            try:
                pool.release(conn)
            except Exception:
                conn.close()
    else:
        # fallback: try direct connect (useful for tests or dev)
        conn = oracledb.connect(
            user=settings.ORACLE_USER,
            password=settings.ORACLE_PASSWORD,
            dsn=settings.ORACLE_DSN
        )
        try:
            yield conn
        finally:
            conn.close()
