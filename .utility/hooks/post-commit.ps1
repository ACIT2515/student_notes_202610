#!/usr/bin/env pwsh
# hooks are run with project root as cwd
python .\.git\hooks\restore_links.py ".\.sym_links.json"
git add .\.sym_links.json
