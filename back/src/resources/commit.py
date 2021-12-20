from datetime import datetime
from typing import Dict, Union

from flask_restful import Resource
from git_manager.repo import Repository
from git_manager.exceptions import NoCommit


class Commit(Resource):
    def __init__(self) -> None:
        self._repo_manager = Repository()

    def get(self, hexsha: str) -> Dict[str, Union[str, datetime]]:
        """Return information for the given commit

        Args:
            hexsha (str): Commit code

        Returns:
            Commit information
        """
        try:
            commit = self._repo_manager.get_commit(hexsha)
        except NoCommit as ex:
            return {'error': str(ex)}, 404

        return commit
