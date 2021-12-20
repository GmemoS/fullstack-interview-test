from datetime import datetime
from typing import Dict, Union

from flask_restful import Resource
from git_manager.repo import Repository
from git_manager.exceptions import NoBranch


class Branch(Resource):
    def __init__(self) -> None:
        self._repo_manager = Repository()

    def get(self, name: str) -> Dict[str, Union[str, datetime]]:
        """Return information for the given branch

        Args:
            name (str): Branch name

        Returns:
            Branch information
        """
        try:
            branch = self._repo_manager.get_branch(name)
        except NoBranch as ex:
            return {'error': str(ex)}, 404

        return branch
