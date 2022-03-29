from typing import  Union
from git.repo.base import Repo

def get_changes(repo: Repo, cmt: Union[str, None], before: str, after: str, author: Union[str, None]) -> list[str]:
    result = []
    commits = repo.iter_commits(cmt, before=before, after=after, author=author)
    for commit in commits:
        show = repo.git.show(commit)
        result.append(show) 
    return result
