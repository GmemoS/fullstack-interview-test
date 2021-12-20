from datetime import datetime
from typing import Dict, Iterable, Union

from flask_restful import request, Resource
from git_manager.repo import FileType, Repository
from git_manager.exceptions import NoBranch, NoCommit

CommitType = Dict[str, Union[str, datetime, FileType]]



class Commits(Resource):
    def __init__(self) -> None:
        self._repo_manager = Repository()


    def get(self) -> Union[CommitType, Iterable[CommitType]]:
        """Return commits information

        Returns:
            List of commits
        """
        commit_hexsha = request.args.get('id')
        branch_name = request.args.get('branch_name')

        if commit_hexsha:
            try:
                return self._repo_manager.get_commit(commit_hexsha)
            except NoCommit as ex:
                return {'error': str(ex)}, 404
        else:
            commits = []
            try:
                _commits = self._repo_manager.get_commits(branch_name)

                # Add count_file field to commit info
                for commit in _commits:
                    commit['count_files'] = len(commit['files'])
                    commits.append(commit)
            except NoBranch as ex:
                return {'message': str(ex)}, 404

            return commits
