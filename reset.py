from db import DB

def reset_db():
    DB.exec('DROP TABLE race_results')

if __name__ == '__main__':
    reset_db()
    print('finisth reset DB.')
