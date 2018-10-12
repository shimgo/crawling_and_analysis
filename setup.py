from db import DB
import textwrap

def setup_db():
    CREATE_RACE_RESULTS = textwrap.dedent('''\
        CREATE TABLE IF NOT EXISTS race_results(
            race_id INTEGER,
            finish_order INTEGER,
            box_num INTEGER,
            horse_num INTEGER,
            horse_name TEXT,
            horse_sex TEXT,
            horse_age INTEGER,
            burden_weight REAL,
            jockey TEXT,
            record REAL,
            margin TEXT,
            last_passing_rank INTEGER,
            second_passing_rank INTEGER,
            before_goal_time REAL,
            single_odds REAL,
            popularity INTEGER,
            horse_weight REAL,
            horse_weight_delta INTEGER,
            trainer TEXT,
            owner TEXT,
            prize INTEGER
        )
    ''')
    DB.exec(str(CREATE_RACE_RESULTS))

if __name__ == '__main__':
    setup_db()
    print('finish setup DB.')
