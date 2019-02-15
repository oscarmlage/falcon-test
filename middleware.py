# -*- coding: utf-8 -*-

import sqlalchemy.orm.scoping as scoping
from sqlalchemy.exc import SQLAlchemyError


class DatabaseSessionManager(object):
    def __init__(self, db_session):
        self._session_factory = db_session
        self._scoped = isinstance(db_session, scoping.ScopedSession)

    def process_request(self, req, res, resource=None):
        """
        Handle post-processing of the response (after routing).
        """
        req.context['session'] = self._session_factory

    def process_response(self, req, res, resource=None):
        """
        Handle post-processing of the response (after routing).
        """
        session = req.context['session']

        try:
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise ValueError('A very specific bad thing happened: %s' % e)

        if self._scoped:
            # remove any database-loaded state from all current objects
            # so that the next access of any attribute, or any query execution
            # will retrieve new state
            session.remove()
        else:
            session.close()
