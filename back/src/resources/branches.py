from datetime import datetime
from typing import Dict, Iterable, Union

from flask_restful import request, Resource
from git_manager.repo import Repository
from git_manager.exceptions import NoBranch

BranchType = Dict[str, Union[str, datetime]]


class Branches(Resource):
    def __init__(self) -> None:
        self._repo_manager = Repository()

    def get(self) -> Union[BranchType, Iterable[BranchType]]:
        """Return branches information

        Returns:
            List of branches
        """
        branch_name = request.args.get('name')
        if branch_name:
            try:
                return self._repo_manager.get_branch(branch_name)
            except NoBranch as ex:
                return {'message': str(ex)}, 404
        else:
            return self._repo_manager.get_branches()
