from datetime import datetime
from typing import Dict, Iterable, Union

from flask_restful import Resource
from git_manager.repo import Repository


class Branches(Resource):
    def __init__(self) -> None:
        self._repo_manager = Repository()

    def get(self) -> Iterable[Dict[str, Union[str, datetime]]]:
        """Return all branches in the repository

        Returns:
            List of branches
        """
        return self._repo_manager.get_branches()
