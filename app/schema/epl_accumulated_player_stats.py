from pydantic import BaseModel, ConfigDict


class PlayerStats(BaseModel):
    id: int
    name: str
    position: str
    height: int
    team_id: int
    season_id: int

    total_pass: int
    accurate_pass: int
    total_long_balls: int
    accurate_long_balls: int
    accurate_own_half_passes: int
    total_own_half_passes: int
    accurate_opposition_half_passes: int
    total_opposition_half_passes: int

    total_clearance: int
    ball_recovery: int
    saves: int
    punches: int
    total_keeper_sweeper: int
    accurate_keeper_sweeper: int

    minutes_played: int
    touches: int
    rating: float
    possession_lost_ctrl: int

    total_shots: int
    goal_assist: int
    total_cross: int
    accurate_cross: int

    aerial_lost: int
    duel_lost: int
    duel_won: int
    challenge_lost: int
    total_contest: int
    won_contest: int

    total_tackle: int
    was_fouled: int
    fouls: int
    key_pass: int

    on_target_scoring_attempt: int
    goals: int
    outfielder_block: int
    blocked_scoring_attempt: int
    interception_won: int

    big_chance_created: int
    big_chance_missed: int
    dispossessed: int
    shot_off_target: int
    unsuccessful_touch: int
    total_offside: int

    good_high_claim: int
    saved_shots_from_inside_the_box: int

    expected_assists: float

    total_ball_carries_distance: float
    ball_carries_count: int
    total_progression: float
    progressive_ball_carries_count: int

    keeper_save_value: float
    goals_prevented: float

    pass_value_normalized: float
    dribble_value_normalized: float
    defensive_value_normalized: float
    goalkeeper_value_normalized: float

    model_config = ConfigDict(from_attributes=True)