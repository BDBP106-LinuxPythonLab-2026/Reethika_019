#!/bin/bash
touch file1 file
chomd u+x file1 file2
chomd o-rx file1 file2

