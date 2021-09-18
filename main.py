import git

repo = git.Repo()
commit_dev = repo.commit("df984b8fded74f477bbdb366d3b61b3daa741a1a")
commit_origin_dev = repo.commit("HEAD")
diff_index = commit_origin_dev.diff(commit_dev)

for diff_item in diff_index.iter_change_type('M'):
    print("A blob:\n{}".format(diff_item.a_blob.data_stream.read().decode('utf-8')))
    print("B blob:\n{}".format(diff_item.b_blob.data_stream.read().decode('utf-8')))