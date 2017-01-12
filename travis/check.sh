#!/bin/bash
git config --global user.email "profci@example.com"
git config --global user.name "profci"
git checkout -b travis-tmp
git pull -X theirs --no-edit "https://github.com/derari/profci-tasks.git" master
bundle exec rspec spec/_tdd_tasks/ --fail-fast --format j --out report.txt
cat report.txt | python travis/submit_issue.py
