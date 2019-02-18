# MODELS

## "More or less" defined models

- √ Athlete
- √ Referee
- √ Location
- √ Country
- √ Discipline
  - Dorsals
- √ Team
- √ Session (general data)

- El que entrega los premios
- Voluntary

## To be defined models

Need to talk about some models:

- √ Session (event)
  - Custom discipline data (times, score...)
  - Run/Round (round, ronda)
  - Athletes/Teams on Session

- Genre (men, women, mixed)
- Category (junior, senior, combined, parallel, internship, worldship...) ??

## Questions

- Do we need "Categories" if we have Disciplines, Sessions and
disciplines_sessions?
- Do we need "Rounds" if we have disciplines_sessions
- We don't need "Dorsals" as an isolated table, we can put the dorsal number
in teams_athletes directly
- Need to talk about sessions in different disciplines where to store data
(goals, teams, athletes, times...) because every discipline has totally
different data.
