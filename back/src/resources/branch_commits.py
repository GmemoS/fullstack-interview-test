from datetime import datetime
from typing import Dict, Union

from flask_restful import Resource
from git_manager.repo import Repository
from git_manager.exceptions import NoBranch


class BranchCommits(Resource):
    def __init__(self) -> None:
        self._repo_manager = Repository()


    def get(self, name: str) -> Dict[str, Union[str, datetime]]:
        """Return commits for the given branch

        Args:
            name (str): Branch name

        Returns:
            Branch commits
        """
        commits = []

        try:
            _commits = self._repo_manager.get_branch_commits(name)

            # Add count_file field to commit info
            for commit in _commits:
                commit['count_files'] = len(commit['files'])
                commits.append(commit)
        except NoBranch as ex:
            return {'error': str(ex)}, 404

        return commits
