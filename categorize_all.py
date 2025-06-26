import os
import re
from collections import defaultdict

# Patterns for categories
CATEGORIES = {
    'Graph Algorithms': [r'\bgraph\b', r'\bUnionFind\b', r'\bDijkstra\b', r'\bkruskal\b', r'bfs', r'dfs', r'\bdeque\b'],
    'Dynamic Programming': [r'\bdp\b', r'\bmemo\b', r'\brecurrence\b'],
    'Search / Backtracking': [r'dfs', r'backtrack', r'recursion'],
    'Bit Operations': [r'<<', r'>>', r'\bbit\b', r'&', r'\|'],
    'Math / Number Theory': [r'gcd', r'lcm', r'pow\(', r'mod'],
    'Data Structures': [r'heapq', r'bisect', r'DefaultDict', r'Counter', r'SegmentTree', r'Fenwick'],
    'Binary Search': [r'bisect', r'binary_search'],
    'Greedy / Sorting': [r'sorted\(', r'sort\(', r'heapq'],
}

results = defaultdict(list)

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.py'):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as fh:
                    text = fh.read()
            except Exception:
                continue
            added = False
            for cat, pats in CATEGORIES.items():
                for pat in pats:
                    if re.search(pat, text):
                        results[cat].append(path)
                        added = True
                        break
                if added:
                    break
            if not added:
                results['Implementation / Misc'].append(path)

with open('FULL_SOURCE_CATEGORIZATION.md', 'w', encoding='utf-8') as out:
    out.write('# Full Source Categorization\n\n')
    for cat in sorted(results.keys()):
        out.write(f'## {cat}\n')
        for p in sorted(results[cat]):
            out.write(f'- `{p}`\n')
        out.write('\n')
