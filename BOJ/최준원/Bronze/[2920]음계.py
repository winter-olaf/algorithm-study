import sys
note = list(map(int,sys.stdin.readline().split()))
print({note == sorted(note) : 'ascending', note == sorted(note,reverse=True) : 'descending'}.get(True,'mixed'))