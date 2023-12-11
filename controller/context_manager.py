from contextvars import ContextVar

import uuid
from fastapi import Depends, Request
from sqlalchemy.orm import Session

from data_adapter.db import get_db
from logger import logger

# we are using context variables to store request level context , as FASTAPI
# does not provide request context out of the box

# context_db_session stores db session created for every request
context_db_session: ContextVar[Session] = ContextVar('db_session', default=None)
# context_api_id stores unique id for every request
context_api_id: ContextVar[str] = ContextVar('api_id', default=None)
# context_log_meta stores log meta data for every request
context_log_meta: ContextVar[dict] = ContextVar('log_meta', default={})
# context_user_id stores user id coming from client for every request
context_user_id: ContextVar[str] = ContextVar('user_id', default=None)
# context_set_db_session_rollback stores flag to rollback db session or not
context_set_db_session_rollback: ContextVar[bool] = ContextVar('set_db_session_rollback', default=False)


async def build_request_context(request: Request,
                                db: Session = Depends(get_db)):
    # set the db-session in context-var so that we don't have to pass this dependency downstream
    context_db_session.set(db)
    context_api_id.set(str(uuid.uuid4()))
    context_user_id.set(request.headers.get('X-User-ID'))
    context_log_meta.set({'api_id': context_api_id.get(), 'request_id': request.headers.get('X-Request-ID'),
                          'user_id': context_user_id.get()})
    logger.info(extra=context_log_meta.get(), msg="REQUEST_INITIATED")


def get_db_session() -> Session:
    """common method to get db session from context variable"""
    return context_db_session.get()