# bio_calc_HW2
# Biological Computation – Exercise 2  
Solutions for **Question 1** (motif generation) and **Question 2** (motif counting).
---
## Contents
| File | Purpose |
|------|---------|
| `bio_calc_HW2_Q1.py` | Generates **all non-isomorphic, connected directed motifs** of size *n* and writes them to `motifs_n=<n>.txt`. |
| `bio_calc_HW2_Q2.py` | Counts how many times each size-*n* motif appears in a given graph and writes the results to `motifs_instances_n=<n>.txt`. |
| *input_graph.txt* | **Example** edge-list file used by Q2 *(You provide this).* |

---

## Requirements
* Python ≥ 3.8  
* [`networkx`](https://networkx.org/) ≥ 2.8

---

### How to run Q1
1. go to file `bio_calc_HW2_Q1.py`.
2. in line 58 set "n"
3. run the code it will creat a file named `motifs_n=<n>.txt` with the answer.

### How to run Q2
1. go to file `bio_calc_HW2_Q2.py`.
2. in line 97 set "n".
3. go to file `input_graph.txt` and past your graph.
4. run the code it will creat a file named `motifs_instances_n=<n>.txt` with the answer.
