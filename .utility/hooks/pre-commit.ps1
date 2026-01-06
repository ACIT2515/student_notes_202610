#!/usr/bin/env pwsh
# hooks are run with project root as cwd
python .\.git\hooks\process_links.py ".\" ".\.sym_links.json"
