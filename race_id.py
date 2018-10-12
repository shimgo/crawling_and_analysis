from db import DB

class RaceId:
    def increment(self):
        if hasattr(self, '__race_id'):
            self.race_id += 1
            return self.race_id

        self.__race_id = self.fetchMax() + 1
        return self.__race_id

    def fetchMax(self):
        result = DB.exec(u"SELECT MAX(race_id) FROM race_results")
        for row in result:
            if not row[0]:
                return 1
            self.race_id = row[0]
        return self.race_id
