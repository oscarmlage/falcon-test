# References

* https://github.com/ziwon/falcon-rest-api
* https://github.com/codecraf8/rest-api-python-falcon
* https://app.quickdatabasediagrams.com/

```
athlete as a
-
id PK int
name string
surname string
country_id int FK >- c.id

country as c
-
id PK int
name  string

discipline as d
-
id int FK
name  string

dorsal as do
-
id int FK
number int


location
-
id int FK
name string
address string
gps string

referee
-
id int FK
name string

disciplines_sessions
-
discipline_id int FK >- discipline.id
session_id int FK - session.id
location_id int FK - location.id
referee_id int FK - referee.id

session
-
id int FK
date date
time time


team as t
-
id PK int
name string
country_id int FK >- c.id
discipline_id int FK >- discipline.id

teams_athletes
-
athlete_id int FK - a.id
team_id int FK >- team.id
dorsal_id int FK >- dorsal.id
```