from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base


class SessionHockey(Base):

    """
    :Example:

    >>> SessionHockey(reference = REF001,
    >>>               session_id = 22,
    >>>               session = [(22, "Senior Men"),],
    >>>               localteam_id = 14,
    >>>               localteam = [(14, "USA"),],
    >>>               localteam_score_q1 = 2,
    >>>               localteam_score_q2 = 5,
    >>>               localteam_score_q3 = 7,
    >>>               localteam_score_q4 = 14,
    >>>               localteam_score_p1 = NULL,
    >>>               localteam_score_p2 = NULL,
    >>>               visitorteam_id = 15,
    >>>               visitorteam = [(15, "Uganda"),],
    >>>               visitorteam_score_q1 = 1,
    >>>               visitorteam_score_q2 = 1,
    >>>               visitorteam_score_q3 = 3,
    >>>               visitorteam_score_q4 = 7,
    >>>               visitorteam_score_p1 = NULL,
    >>>               visitorteam_score_p2 = NULL,
    >>>               ...
    >>> )
    """

    __tablename__ = 'session_hockey'
    id = Column(Integer, primary_key=True)
    reference = Column(String(150))

    # One to One: sessions
    #session_id = Column(Integer, ForeignKey("session.id"))
    #session = relationship("Session")

    # One to One: categories
    #localteam_id = Column(Integer, ForeignKey("localteam.id"))
    #localteam = relationship("Team")
    localteam_score_q1 = Column(Integer)
    localteam_score_q2 = Column(Integer)
    localteam_score_q3 = Column(Integer)
    localteam_score_q4 = Column(Integer)
    localteam_score_p1 = Column(Integer)
    localteam_score_p2 = Column(Integer)

    # One to One: locations
    #visitorteam_id = Column(Integer, ForeignKey("visitorteam.id"))
    #visitorteam = relationship("Team")
    visitorteam_score_q1 = Column(Integer)
    visitorteam_score_q2 = Column(Integer)
    visitorteam_score_q3 = Column(Integer)
    visitorteam_score_q4 = Column(Integer)
    visitorteam_score_p1 = Column(Integer)
    visitorteam_score_p2 = Column(Integer)

    """
    Note: We need to store much more data here
    """
