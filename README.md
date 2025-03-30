# RepoSyncer

**RepoSyncer** is a Python utility for automating the update process of multiple local Git repositories. It pulls the latest changes from the upstream master branch and updates your fork at the origin.

Background: It's was a personal project where often I had to do multiple repos cleanup at the same time. So I started a script that would take care of this. All my repos forks follow standard upstream (original) and origin (my fork) as remote names pattern.

## Features

- Batch update all your local repositories.
- Ensures the master branch is up-to-date with the upstream.
- Pushes changes to your fork.
- Handles unsaved changes interactively.
- User-defined workspace directory and remote names.

## Installation

1. Clone the RepoSyncer repository:
   ```bash
   git clone https://github.com/dailyops/RepoSyncer.git
   ```
2. Navigate to the RepoSyncer directory:
   ```bash
   cd RepoSyncer
   ```

## Usage

Run the script:
```bash
python3 reposyncer.py
```

You will be prompted for:
- Workspace directory (default is the script's location).
- Remote names for upstream and origin.

### Example

```
Enter the workspace directory (default: wherever you place the reposyncer.py): /Users/username
Enter the remote name for the original repo (upstream): upstream
Enter the remote name for your fork (origin): origin
```

## Troubleshooting

- Make sure Git is installed and available in your system's PATH.
- Ensure you have the necessary permissions to pull from upstream and push to origin.

## License

This project is licensed under the MIT License.
