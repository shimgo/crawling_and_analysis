from race_result import RaceResult
import textwrap
import re

class Parser:
    @classmethod
    def parse_race(cls, race_table, race_id):
        for table in race_table.find_all("table", class_="race_table_01 nk_tb_common"):
            race_results = []
            for tr in table.find_all("tr"):
                tds = tr.find_all("td")
                if len(tds) == 0:
                    continue
                cols = []
                for i, td in enumerate(tr.find_all("td")):
                    link = td.find("a")

                    content = None
                    if td.string and td.string != '\n':
                        content = td.string
                    elif link and link.string and link.string != '\n':
                        content = link.string
                    cols.append(content)
                result = RaceResult()
                result.race_id             = race_id
                result.finish_order        = cols[0]
                result.box_num             = cols[1]
                result.horse_num           = cols[2]
                result.horse_name          = cols[3]
                result.horse_sex           = cols[4][0]
                result.horse_age           = re.match(r".*([0-9]+)", cols[4]).group(1)
                result.burden_weight       = cols[5]
                result.jockey              = cols[6]
                record_match               = re.match(r"^([0-9]+):(.+)$", cols[7])
                result.record              = float(record_match.group(1)) * 60 + float(record_match.group(2))
                result.margin              = cols[8] or ""
                passing_rank_match         = re.match(r"^([0-9]+)-([0-9]+)$", cols[10])
                result.last_passing_rank   = passing_rank_match.group(2)
                result.second_passing_rank = passing_rank_match.group(1)
                result.before_goal_time    = cols[11]
                result.single_odds         = cols[12]
                result.popularity          = cols[13]
                horse_weight_match         = re.match(r"^([0-9]+)\(([+-]*[0-9]+)\)$", cols[14])
                result.horse_weight        = horse_weight_match.group(1)
                result.horse_weight_delta  = horse_weight_match.group(2)
                result.trainer             = cols[18]
                result.owner               = cols[19]
                result.prize               = str(cols[20] or '').replace(',', '')

                race_results.append(result)
        return race_results
