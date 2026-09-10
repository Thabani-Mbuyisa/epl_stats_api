from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class EplAccumulatedPlayerStats(Base):
    __tablename__ = "acc_player_stats"

    player_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    season_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String)
    position: Mapped[str] = mapped_column(String)
    height: Mapped[int] = mapped_column(Integer)
    team_id: Mapped[int] = mapped_column(Integer)

    total_pass: Mapped[int] = mapped_column(Integer, default=0)
    accurate_pass: Mapped[int] = mapped_column(Integer, default=0)
    total_long_balls: Mapped[int] = mapped_column(Integer, default=0)
    accurate_long_balls: Mapped[int] = mapped_column(Integer, default=0)
    accurate_own_half_passes: Mapped[int] = mapped_column(Integer, default=0)
    total_own_half_passes: Mapped[int] = mapped_column(Integer, default=0)
    accurate_opposition_half_passes: Mapped[int] = mapped_column(Integer, default=0)
    total_opposition_half_passes: Mapped[int] = mapped_column(Integer, default=0)

    total_clearance: Mapped[int] = mapped_column(Integer, default=0)
    ball_recovery: Mapped[int] = mapped_column(Integer, default=0)
    saves: Mapped[int] = mapped_column(Integer, default=0)
    punches: Mapped[int] = mapped_column(Integer, default=0)
    total_keeper_sweeper: Mapped[int] = mapped_column(Integer, default=0)
    accurate_keeper_sweeper: Mapped[int] = mapped_column(Integer, default=0)

    minutes_played: Mapped[int] = mapped_column(Integer, default=0)
    touches: Mapped[int] = mapped_column(Integer, default=0)
    rating: Mapped[float] = mapped_column(Float, default=0)
    possession_lost_ctrl: Mapped[int] = mapped_column(Integer, default=0)

    total_shots: Mapped[int] = mapped_column(Integer, default=0)
    goal_assist: Mapped[int] = mapped_column(Integer, default=0)
    total_cross: Mapped[int] = mapped_column(Integer, default=0)
    accurate_cross: Mapped[int] = mapped_column(Integer, default=0)

    aerial_lost: Mapped[int] = mapped_column(Integer, default=0)
    duel_lost: Mapped[int] = mapped_column(Integer, default=0)
    duel_won: Mapped[int] = mapped_column(Integer, default=0)
    challenge_lost: Mapped[int] = mapped_column(Integer, default=0)
    total_contest: Mapped[int] = mapped_column(Integer, default=0)
    won_contest: Mapped[int] = mapped_column(Integer, default=0)

    total_tackle: Mapped[int] = mapped_column(Integer, default=0)
    was_fouled: Mapped[int] = mapped_column(Integer, default=0)
    fouls: Mapped[int] = mapped_column(Integer, default=0)
    key_pass: Mapped[int] = mapped_column(Integer, default=0)

    on_target_scoring_attempt: Mapped[int] = mapped_column(Integer, default=0)
    goals: Mapped[int] = mapped_column(Integer, default=0)
    outfielder_block: Mapped[int] = mapped_column(Integer, default=0)
    blocked_scoring_attempt: Mapped[int] = mapped_column(Integer, default=0)
    interception_won: Mapped[int] = mapped_column(Integer, default=0)

    big_chance_created: Mapped[int] = mapped_column(Integer, default=0)
    big_chance_missed: Mapped[int] = mapped_column(Integer, default=0)
    dispossessed: Mapped[int] = mapped_column(Integer, default=0)
    shot_off_target: Mapped[int] = mapped_column(Integer, default=0)
    unsuccessful_touch: Mapped[int] = mapped_column(Integer, default=0)
    total_offside: Mapped[int] = mapped_column(Integer, default=0)

    good_high_claim: Mapped[int] = mapped_column(Integer, default=0)
    saved_shots_from_inside_the_box: Mapped[int] = mapped_column(Integer, default=0)

    expected_assists: Mapped[float] = mapped_column(Float, default=0)

    total_ball_carries_distance: Mapped[float] = mapped_column(Float, default=0)
    ball_carries_count: Mapped[int] = mapped_column(Integer, default=0)
    total_progression: Mapped[float] = mapped_column(Float, default=0)
    progressive_ball_carries_count: Mapped[int] = mapped_column(Integer, default=0)

    keeper_save_value: Mapped[float] = mapped_column(Float, default=0)
    goals_prevented: Mapped[float] = mapped_column(Float, default=0)

    pass_value_normalized: Mapped[float] = mapped_column(Float, default=0)
    dribble_value_normalized: Mapped[float] = mapped_column(Float, default=0)
    defensive_value_normalized: Mapped[float] = mapped_column(Float, default=0)
    goalkeeper_value_normalized: Mapped[float] = mapped_column(Float, default=0)