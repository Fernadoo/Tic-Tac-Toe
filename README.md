# Tic-Tac-Toe

### Quick start

You can  try the ***pre-trained agent*** by running `python eval.py 10000`.



### Customized training and evaluating

First, ***train*** the Q learning agent, run `python train.py {num_iteration}`. For example:

```shell
>>> python train.py 150

Start learning...
100%|█████████████████████████| 150/150 [00:00<00:00, 109.45it/s]
Finish learning!
Q value saved, ready for play!
```

Then, ***play*** with the agent, run `python eval.py {num_iteration}`. You need to specify `{num_iteration}` to direct the program to the corresponding Q file. Note that for human players you must play a valid move. For example:

```shell
>>> python eval.py 150

Q value loaded from pickles/TPQ_0.9_0.9_0.2_150.pkl

x| |
- - -
 | |
- - -
 | |
TPQ move [0,0]!

Choose the row: 1
Choose the col: 1
x| |
- - -
 |o|
- - -
 | |
Fernando move [1,1]!
```



