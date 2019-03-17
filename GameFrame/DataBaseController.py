import os
import sqlite3


class DataBaseController:
    def __init__(self, dbase_file_name):
        app_file_path = os.path.join(os.path.dirname(__file__), dbase_file_name)
        self.app_db = sqlite3.connect(app_file_path)
        self.app_cursor = self.app_db.cursor()

    def close(self):
        self.app_db.close()

    def add_score(self, name, score):
        print("Name: {}  Score: {}".format(name, score))
        self.app_cursor.execute(
            """
                INSERT OR IGNORE INTO Player(name)
                VALUES(:name)
            """,
            {'name': name}
        )

        self.app_cursor.execute(
            """
                INSERT INTO Score(player_id, score)
                VALUES(
                    (
                        SELECT id
                        FROM Player
                        WHERE name = :name
                    ),
                    :score
                )
            """,
            {'score': score, 'name': name}
        )

        self.app_db.commit()

    def get_top_5(self):
        self.app_cursor.execute(
            """
                SELECT Player.name, Score.score
                FROM Player, Score
                WHERE Score.player_id = Player.id
                ORDER BY Score.score DESC
                LIMIT 5
            """

        )
        return self.app_cursor.fetchall()
