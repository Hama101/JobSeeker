"""
Base model for all models
"""

from db import engine


class BaseModel:
    """
    Base model for all models
    """

    def __init__(self):
        self.engine = engine

    def get_all(self):
        """
        Get all records from the table
        """
        with self.engine.connect() as connection:
            result = connection.execute(self.table.select())
            return result.fetchall()

    def get_by_id(self, id):
        """
        Get a record by id
        """
        with self.engine.connect() as connection:
            result = connection.execute(
                self.table.select().where(self.table.c.id == id)
            )
            return result.fetchone()

    def create(self, data):
        """
        Create a new record
        """
        with self.engine.connect() as connection:
            result = connection.execute(self.table.insert().values(**data))
            return result.inserted_primary_key

    def update(self, id, data):
        """
        Update a record
        """
        with self.engine.connect() as connection:
            result = connection.execute(
                self.table.update().where(self.table.c.id == id).values(**data)
            )
            return result.rowcount

    def delete(self, id):
        """
        Delete a record
        """
        with self.engine.connect() as connection:
            result = connection.execute(
                self.table.delete().where(self.table.c.id == id)
            )
            return result.rowcount