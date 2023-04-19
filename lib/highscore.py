from lib import CONN, CURSOR

class HighScore:
    def __init__(self, name = None, highscore = None, user_id = None, id = None):
        self.name = name
        self.highscore = highscore
        self.id = id
        self.user_id = user_id

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS highscores (
                id INTEGER PRIMARY KEY,
                name TEXT,
                highscore INTEGER
            )
        """
        CURSOR.execute(sql)

    def save(self):
        if self.id:
            self._update()
        else:
            self._create()
    
    def _create(self):
        sql = """
            INSERT INTO highscores (name, highscore, user_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, [self.name, self.highscore, self.user_id])
        CONN.commit()
        self.id = CURSOR.execute('SELECT * FROM highscores ORDER BY id DESC').fetchone()[0]

    def _update(self):
        sql = """
            UPDATE highscores
            SET name = ?, highscore = ?, user_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, [self.name, self.highscore, self.user_id, self.id])
        CONN.commit()

    @classmethod
    def add_column(cls):
        sql = """
            ALTER TABLE highscores
            ADD user_id INTEGER
        """
        CURSOR.execute(sql)
        CONN.commit()

HighScore.create_table()
# HighScore.add_column()