from models.base_model import BaseModel

class Job(BaseModel):
    """
    Job model
    """

    def __init__(self):
        super().__init__()
        self.table = self.engine["jobs"]
        # create table if not exists
        self.table.create()

    def get_all(self):
        """
        Get all jobs
        """
        return super().get_all()

    def get_by_id(self, id):
        """
        Get a job by id
        """
        return super().get_by_id(id)

    def create(self, data):
        """
        Create a new job
        """
        return super().create(data)

    def update(self, id, data):
        """
        Update a job
        """
        return super().update(id, data)

    def delete(self, id):
        """
        Delete a job
        """
        return super().delete(id)