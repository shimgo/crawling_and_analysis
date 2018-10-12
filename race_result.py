from db import DB
import textwrap

class RaceResult:
    def __init__(self, race_id = None, finish_order = None, box_num = None, horse_num = None, horse_name = None, horse_sex = None, horse_age = None, burden_weight = None, jockey = None, record = None, margin = None, last_passing_rank = None, second_passing_rank = None, before_goal_time = None, single_odds = None, popularity = None, horse_weight = None, horse_weight_delta = None, trainer = None, owner = None, prize = None):
        self.race_id             = race_id
        self.finish_order        = finish_order        # 着順
        self.box_num             = box_num             # 枠番
        self.horse_num           = horse_num           # 馬番
        self.horse_name          = horse_name          # 馬名
        self.horse_sex           = horse_sex           # 性齢
        self.horse_age           = horse_age
        self.burden_weight       = burden_weight       # 斤量
        self.jockey              = jockey              # 騎手
        self.record              = record              # タイム(秒)
        self.margin              = margin              # 着差
        self.last_passing_rank   = last_passing_rank   # 第4コーナー通過順位
        self.second_passing_rank = second_passing_rank # 第3コーナー通過順位
        self.before_goal_time    = before_goal_time    # 上り
        self.single_odds         = single_odds         # 単勝
        self.popularity          = popularity          # 人気
        self.horse_weight        = horse_weight        # 馬体重
        self.horse_weight_delta  = horse_weight_delta  # 馬体重変化
        self.trainer             = trainer             # 調教師
        self.owner               = owner               # 馬主
        self.prize               = prize               # 賞金(万円)

    @property
    def race_id(self):
        return self._race_id

    @race_id.setter
    def race_id(self, race_id):
        self._race_id = race_id

    @property
    def finish_order(self):
        return self._finish_order

    @finish_order.setter
    def finish_order(self, finish_order):
        self._finish_order = finish_order

    @property
    def box_num(self):
        return self._box_num

    @box_num.setter
    def box_num(self, box_num):
        self._box_num = box_num

    @property
    def horse_num(self):
        return self._horse_num

    @horse_num.setter
    def horse_num(self, horse_num):
        self._horse_num = horse_num

    @property
    def horse_name(self):
        return self._horse_name

    @horse_name.setter
    def horse_name(self, horse_name):
        self._horse_name = horse_name

    @property
    def horse_sex(self):
        return self._horse_sex

    @horse_sex.setter
    def horse_sex(self, horse_sex):
        self._horse_sex = horse_sex

    @property
    def horse_age(self):
        return self._horse_age

    @horse_age.setter
    def horse_age(self, horse_age):
        self._horse_age = horse_age

    @property
    def burden_weight(self):
        return self._burden_weight

    @burden_weight.setter
    def burden_weight(self, burden_weight):
        self._burden_weight = burden_weight

    @property
    def jockey(self):
        return self._jockey

    @jockey.setter
    def jockey(self, jockey):
        self._jockey = jockey

    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, record):
        self._record = record

    @property
    def margin(self):
        return self._margin

    @margin.setter
    def margin(self, margin):
        self._margin = margin

    @property
    def last_passing_rank(self):
        return self._last_passing_rank

    @last_passing_rank.setter
    def last_passing_rank(self, last_passing_rank):
        self._last_passing_rank = last_passing_rank

    @property
    def last_passing_rank(self):
        return self._last_passing_rank

    @last_passing_rank.setter
    def last_passing_rank(self, last_passing_rank):
        self._last_passing_rank = last_passing_rank

    @property
    def before_goal_time(self):
        return self._before_goal_time

    @before_goal_time.setter
    def before_goal_time(self, before_goal_time):
        self._before_goal_time = before_goal_time

    @property
    def single_odds(self):
        return self._single_odds

    @single_odds.setter
    def single_odds(self, single_odds):
        self._single_odds = single_odds

    @property
    def popularity(self):
        return self._popularity

    @popularity.setter
    def popularity(self, popularity):
        self._popularity = popularity

    @property
    def horse_weight(self):
        return self._horse_weight

    @horse_weight.setter
    def horse_weight(self, horse_weight):
        self._horse_weight = horse_weight

    @property
    def horse_weight_delta(self):
        return self._horse_weight_delta

    @horse_weight_delta.setter
    def horse_weight_delta(self, horse_weight_delta):
        self._horse_weight_delta = horse_weight_delta

    @property
    def trainer(self):
        return self._trainer

    @trainer.setter
    def trainer(self, trainer):
        self._trainer = trainer

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner

    @property
    def prize(self):
        return self._prize

    @prize.setter
    def prize(self, prize):
        self._prize = prize

    @classmethod
    def save_all(cls, race_results):
        INSERT_RACE_RESULTS = textwrap.dedent('''\
            INSERT INTO race_results VALUES(
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''')
        params = []
        for r in race_results:
            params.append((
                r.race_id,
                r.finish_order,
                r.box_num,
                r.horse_num,
                r.horse_name,
                r.horse_sex,
                r.horse_age,
                r.burden_weight,
                r.jockey,
                r.record,
                r.margin,
                r.last_passing_rank,
                r.second_passing_rank,
                r.before_goal_time,
                r.single_odds,
                r.popularity,
                r.horse_weight,
                r.horse_weight_delta,
                r.trainer,
                r.owner,
                r.prize
            ))
        DB.exec(str(INSERT_RACE_RESULTS), params)
