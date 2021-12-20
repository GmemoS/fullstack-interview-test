import os
from datetime import datetime
from typing import Dict, Iterable, Optional, Union

from git import Repo
from gitdb.exc import BadName

from .enums import ENV_REPO
from .exceptions import MissingEnv, NoBranch, NoCommit

FileType = Dict[str, Dict[str, int]]


class Repository:
    def __init__(self) -> None:
        if not os.getenv(ENV_REPO):
            raise MissingEnv(
                'No path to GIT repository defined',
                env=ENV_REPO,
            )
        self._repo = Repo(os.environ[ENV_REPO])

    def get_branch(self, name: str) -> Dict[str, Union[str, datetime]]:
        """Return branch info in the format below
        {
            'name': str,
            'commit': str,
            'datetime': datetime,
        }

        Args:
            name (str): Branch name

        Raises:
            NoBranch: Error when requested branch does not exist

        Returns:
            Branch information
        """
        try:
            branch = self._repo.heads[name]
        except IndexError:
            raise NoBranch(f'Branch {name} not found', branch=name)

        return {
            'name': branch.name,
            'commit': branch.commit.hexsha,
            'datetime': branch.commit.committed_datetime,
        }

    def get_branches(self) -> Iterable[Dict[str, Union[str, datetime]]]:
        """List all branches in the format below
        {
            'name': str,
            'commit': str,
            'datetime': datetime,
        }

        Yields:
            Available branches
        """
        for branch in self._repo.heads:
            yield {
                'name': branch.name,
                'commit': branch.commit.hexsha,
                'datetime': branch.commit.committed_datetime,
            }

    def get_commit(
        self, hexsha: str
    ) -> Dict[str, Union[str, datetime, FileType]]:
        """Return commit info in the format below

        Args:
            hexsha (str): Commit code

        Raises:
            NoCommit: Error when requested commit does not exist

        Returns:
            Commit information
        """
        try:
            commit = self._repo.commit(hexsha)
        except BadName:
            raise NoCommit(f'Commit {hexsha} not found', commit=hexsha)

        return {
            'hexsha': commit.hexsha,
            'message': commit.message,
            'author': commit.author.name,
            'email': commit.author.email,
            'files': commit.stats.files,
            'datetime': commit.committed_datetime,
        }

    def get_commits(
        self, branch_name: Optional[str] = None
    ) -> Iterable[Dict[str, Union[str, datetime, FileType]]]:
        """List all commits for the given branch in the format below
        {
            'hexsha': str,
            'message': str,
            'author': str,
            'email': str,
            'files': {
                str<file name>: {
                    'insertions': int,
                    'deletions': int,
                    'lines': int,
                },
                ...
            },
            'datetime': datetime,
        }

        Args:
            branch_name (str, optional): Branch name to be used for
                filtering commits. Defaults to None.

        Yields:
            Available commits
        """
        try:
            for commit in self._repo.iter_commits(branch_name):
                yield {
                    'hexsha': commit.hexsha,
                    'message': commit.message,
                    'author': commit.author.name,
                    'email': commit.author.email,
                    'files': commit.stats.files,
                    'datetime': commit.committed_datetime,
                }
        except Exception as ex:
            raise NoBranch(
                f'Branch {branch_name} not found', branch=branch_name
            )
