from pydantic import BaseModel

class CricketMatch(BaseModel):
    batting_team: int
    bowling_team: int
    wides: int
    noballs: int
    byes: int
    legbyes: int
    penalty: int
    balls_left: int
    cumulative_runs: int
    run_rate: float
    target_runs: int
    req_runs: int
    req_rr: float