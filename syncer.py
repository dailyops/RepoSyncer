# -- Mutliple Git Repositories Updater For Everyday Local Development -- #

import os
import subprocess

def run_command(command, cwd=None):
    result = subprocess.run(command, cwd=cwd, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode


def update_repo(repo_path, upstream_name, origin_name):
    print(f'\nUpdating repository: {repo_path}')

    # Check for unsaved changes
    status_out, _, _ = run_command('git status --porcelain', cwd=repo_path)
    if status_out:
        discard_changes = input(f'Uncommitted changes found in {repo_path}. Discard changes and continue? (y/n): ')
        if discard_changes.lower() == 'y':
            print('Discarding changes...')
            run_command('git reset --hard HEAD', cwd=repo_path)
            run_command('git clean -fd', cwd=repo_path)
        else:
            print(f'Skipping {repo_path} due to unsaved changes.')
            return

    # Ensure on master branch
    out, err, code = run_command('git checkout master -f', cwd=repo_path)
    if code != 0:
        print(f'Error: Failed to checkout master in {repo_path}. {err}')
        return

    # Pull the latest code from upstream master
    out, err, code = run_command(f'git fetch {upstream_name}', cwd=repo_path)
    if code != 0:
        print(f'Error: Failed to fetch from {upstream_name} in {repo_path}. {err}')
        return

    out, err, code = run_command(f'git reset --hard {upstream_name}/master', cwd=repo_path)
    if code != 0:
        print(f'Error: Failed to reset to {upstream_name}/master in {repo_path}. {err}')
        return

    # Push updates to the forked origin master
    out, err, code = run_command(f'git push {origin_name} master', cwd=repo_path)
    if code != 0:
        print(f'Error: Failed to push to {origin_name} in {repo_path}. {err}')
        return

    print(f'Updated {repo_path} to the latest master from {upstream_name}.')


def main():
    default_workspace_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_dir = input(f'Enter the workspace directory (default: {default_workspace_dir}): ').strip()
    if not workspace_dir:
        workspace_dir = default_workspace_dir

    if not os.path.isdir(workspace_dir):
        print(f'Workspace directory not found: {workspace_dir}')
        return

    # Get upstream and origin remote names from the user
    upstream_name = input("Enter the remote name for the original repo (upstream): ").strip()
    origin_name = input("Enter the remote name for your fork (origin): ").strip()

    for repo_name in os.listdir(workspace_dir):
        repo_path = os.path.join(workspace_dir, repo_name)
        if os.path.isdir(os.path.join(repo_path, '.git')):
            update_repo(repo_path, upstream_name, origin_name)


if __name__ == '__main__':
    main()