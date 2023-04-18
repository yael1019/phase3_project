from lib import CONN, CURSOR

class HighScore:
    def __init__(self, name = None, highscore = None, id = None):
        self.name = name
        self.highscore = highscore
        self.id = id

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
            INSERT INTO highscores (name, highscore)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, [self.name, self.highscore])
        CONN.commit()
        self.id = CURSOR.execute('SELECT * FROM highscores ORDER BY id DESC').fetchone()[0]

    def _update(self):
        sql = """
            UPDATE highscores
            SET name = ?, highscore = ?,
            WHERE id = ?
        """
        CURSOR.execute(sql, [self.name, self.highscore, self.id])
        CONN.commit()

