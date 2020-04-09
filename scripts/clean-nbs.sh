#!/usr/bin/env bash
set -euo pipefail
git ls-files -- "*.ipynb" \
    | xargs -n1 jupyter nbconvert --to notebook \
                                  --ClearOutputPreprocessor.enabled=True \
                                  --inplace
