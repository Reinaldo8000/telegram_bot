# import psycopg2
# from psycopg2 import OperationalError

# def create_connection(db_name, db_user, db_password, db_host, db_port):
#     connection = None
#     try:
#         connection = psycopg2.connect(
#             database=db_name,
#             user=db_user,
#             password=db_password,
#             host=db_host,
#             port=db_port,
#         )
#         print("Connection to PostgreSQL DB successful")
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#     return connection


# db_connection = create_connection(
#     "lightningassist", "postgres", "reimg8000", "127.0.0.1", "5432"
#     )

from contextlib import contextmanager
from contextvars import ContextVar
from typing import Any, Generator, Optional
from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.session import Session


class WrappedSession(Session):
    pass


ENGINE_ARGUMENTS = {
    "connect_args": {"connect_timeout": 10, "options": "-c timezone=UTC"},
    "pool_pre_ping": True,
    "pool_size": 60,
}
SESSION_ARGUMENTS = {
    "class_": WrappedSession,
    "autocommit": False,
    "autoflush": False,
}


class Database:
    """Setup and contain our database connection.

    This is used to be able to setup the database in an uniform way while allowing easy
    testing and session management.
    Session management is done using ``scoped_session`` with a special scopefunc,
    because we cannot use threading.local(). Contextvar does the right thing with
    respect to asyncio and behaves similar to threading.local(). We only store a random
    string in the contextvar and let scoped session do the heavy lifting.
    This allows us to easily start a new session or get the existing
    one using the scoped_session mechanics.
    """

    def __init__(self, db_url: str) -> None:
        self.request_context: ContextVar[str] = ContextVar(
            "request_context", default=""
        )
        self.engine = create_engine(db_url, **ENGINE_ARGUMENTS)
        self.session_factory = sessionmaker(bind=self.engine, **SESSION_ARGUMENTS)

        self.scoped_session = scoped_session(self.session_factory, self._scopefunc)

    def _scopefunc(self) -> Optional[str]:
        scope_str = self.request_context.get()
        return scope_str

    @property
    def session(self) -> Session:
        return self.scoped_session()

    @contextmanager
    def database_scope(self, **kwargs: Any) -> Generator["Database", None, None]:
        """Create a new database session (scope).

        This creates a new database session to handle all the database connection from
        a single scope (request or workflow). This method should typically only been
        called in request middleware or at the start of workflows.

        Args:
            ``**kwargs``: Optional session kw args for this session
        """
        token = self.request_context.set(str(uuid4()))
        self.scoped_session(**kwargs)
        yield self
        self.scoped_session.remove()
        self.request_context.reset(token)


# class DBSessionMiddleware(BaseHTTPMiddleware):
#     def __init__(self, app: ASGIApp, database: Database):
#         super().__init__(app)
#         self.database = database

#     async def dispatch(
#         self, request: Request, call_next: RequestResponseEndpoint
#     ) -> Response:
#         with self.database.database_scope():
#             response = await call_next(request)
#         return response
