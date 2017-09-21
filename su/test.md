##  Guides to this game

### How to start the game?

Execute the freecell.py with the following command:

```
python freecell.py
```

Then the shell should show the game board and the  command menu:

```
=======Cells========  ====Foundations=====
---1----2----3----4--  --1----2----3----4--
 [   ][   ][   ][   ]  [   ][   ][   ][   ]
=================tableaus=================
---1----2----3----4----5----6----7----8---
   7c   Kc   7h   Ah   5c   9c   8s   7d
   5s   8h   6h  10d   4d   Qh   3c   5h
   Jc   2h   Qs   3d   Js   As   6s   Kh
   7s   6d   3h   4s   5d   Jh   3s  10s
   Qc   9h   8d   Ks   4h   6c   9s   2c
   Ac   9d   Kd   Ad  10c   2d   2s  10h
   Jd   Qd   4c   8c

=======================================================
Commands:
    TC x y    Move card from tableau x to cell y
    TF x y    Move card from tableau x to foundation y
    TT x y    Move card from tableau x to tableau y
    CF x y    Move card from cell x to foundation y
    CT x y    Move card from cell x to tableau y
    H         Display the commands
    Q         Quit
=======================================================

Please input the command:
```

### How to play?

**Display the command**

Enter the choice `h` or `H`, then the program will show the Command menu.

```
Please input the command: h

=======================================================
Commands:
    TC x y    Move card from tableau x to cell y
    TF x y    Move card from tableau x to foundation y
    TT x y    Move card from tableau x to tableau y
    CF x y    Move card from cell x to foundation y
    CT x y    Move card from cell x to tableau y
    H         Display the commands
    Q         Quit
=======================================================
```

At first, the game board show as below:

```
=======Cells========  ====Foundations=====
---1----2----3----4--  --1----2----3----4--
 [   ][   ][   ][   ]  [   ][   ][   ][   ]
=================tableaus=================
---1----2----3----4----5----6----7----8---
   7c   Kc   7h   Ah   5c   9c   8s   7d
   5s   8h   6h  10d   4d   Qh   3c   5h
   Jc   2h   Qs   3d   Js   As   6s   Kh
   7s   6d   3h   4s   5d   Jh   3s  10s
   Qc   9h   8d   Ks   4h   6c   9s   2c
   Ac   9d   Kd   Ad  10c   2d   2s  10h
   Jd   Qd   4c   8c
```

**Move card from cell to foundation**

Move card `Jd` from tableau 1 to cell 1:

```
Please input the command: tc 1 1                 
=======Cells========  ====Foundations=====       
---1----2----3----4--  --1----2----3----4--      
 [ Jd][   ][   ][   ]  [   ][   ][   ][   ]      
=================tableaus=================       
---1----2----3----4----5----6----7----8---       
   7c   Kc   7h   Ah   5c   9c   8s   7d         
   5s   8h   6h  10d   4d   Qh   3c   5h         
   Jc   2h   Qs   3d   Js   As   6s   Kh         
   7s   6d   3h   4s   5d   Jh   3s  10s         
   Qc   9h   8d   Ks   4h   6c   9s   2c         
   Ac   9d   Kd   Ad  10c   2d   2s  10h         
        Qd   4c   8c                             
```

**Move card from tableau to cell**

Move the card `Jd` from cell 1 to foundation 1, this movement is invalid, because there is no Ace card in foundation 1

```
Please input the command: cf 1 1
Invalid move: Source card is not an Ace
=======Cells========  ====Foundations=====
---1----2----3----4--  --1----2----3----4--
 [ Jd][   ][   ][   ]  [   ][   ][   ][   ]
=================tableaus=================
---1----2----3----4----5----6----7----8---
   7c   Kc   7h   Ah   5c   9c   8s   7d
   5s   8h   6h  10d   4d   Qh   3c   5h
   Jc   2h   Qs   3d   Js   As   6s   Kh
   7s   6d   3h   4s   5d   Jh   3s  10s
   Qc   9h   8d   Ks   4h   6c   9s   2c
   Ac   9d   Kd   Ad  10c   2d   2s  10h
        Qd   4c   8c
```

**Move card from tableau to foundation**

Move the card `Ac` from tableau  1 to foundation 1:

```
Please input the command: tf 1 1
=======Cells========  ====Foundations=====
---1----2----3----4--  --1----2----3----4--
 [ Jd][   ][   ][   ]  [ Ac][   ][   ][   ]
=================tableaus=================
---1----2----3----4----5----6----7----8---
   7c   Kc   7h   Ah   5c   9c   8s   7d
   5s   8h   6h  10d   4d   Qh   3c   5h
   Jc   2h   Qs   3d   Js   As   6s   Kh
   7s   6d   3h   4s   5d   Jh   3s  10s
   Qc   9h   8d   Ks   4h   6c   9s   2c
        9d   Kd   Ad  10c   2d   2s  10h
        Qd   4c   8c
```

Move card `4c` from tableau to foundation 1, this is a invalid move.

```
Please input the command: tf 4 1
Invalid command because of source card and destination card are not matching
=======Cells========  ====Foundations=====
---1----2----3----4--  --1----2----3----4--
 [ Jd][   ][   ][   ]  [ Ac][   ][   ][   ]
=================tableaus=================
---1----2----3----4----5----6----7----8---
   7c   Kc   7h   Ah   5c   9c   8s   7d
   5s   8h   6h  10d   4d   Qh   3c   5h
   Jc   2h   Qs   3d   Js   As   6s   Kh
   7s   6d   3h   4s   5d   Jh   3s  10s
   Qc   9h   8d   Ks   4h   6c   9s   2c
        9d   Kd   Ad  10c   2d   2s  10h
        Qd   4c   8c
Please input the command:
```

Move card `2d` from tableau to foundation 1, it's a invalid move

```
Invalid command because of source card and destination card are not matching
=======Cells========  ====Foundations=====
---1----2----3----4--  --1----2----3----4--
 [ Jd][   ][   ][   ]  [ Ac][   ][   ][   ]
=================tableaus=================
---1----2----3----4----5----6----7----8---
   7c   Kc   7h   Ah   5c   9c   8s   7d
   5s   8h   6h  10d   4d   Qh   3c   5h
   Jc   2h   Qs   3d   Js   As   6s   Kh
   7s   6d   3h   4s   5d   Jh   3s  10s
   Qc   9h   8d   Ks   4h   6c   9s   2c
        9d   Kd   Ad  10c   2d   2s  10h
        Qd   4c   8c
Please input the command:
```

**Move card from tableau to tableau**
Move card `Qd` from tableau 2 to tableau 1, it's a invalid move

```
Please input the command: tt 2 1
Invalid move: Wrong face
=======Cells========  ====Foundations=====
---1----2----3----4--  --1----2----3----4--
 [ Jd][   ][   ][   ]  [ Ac][   ][   ][   ]
=================tableaus=================
---1----2----3----4----5----6----7----8---
   7c   Kc   7h   Ah   5c   9c   8s   7d
   5s   8h   6h  10d   4d   Qh   3c   5h
   Jc   2h   Qs   3d   Js   As   6s   Kh
   7s   6d   3h   4s   5d   Jh   3s  10s
   Qc   9h   8d   Ks   4h   6c   9s   2c
        9d   Kd   Ad  10c   2d   2s  10h
        Qd   4c   8c
Please input the command:
```

**Move card from cell to tableau**

Move card from cell 1 to tableau 2, It's valid 

```
=======Cells========  ====Foundations=====
---1----2----3----4--  --1----2----3----4--
 [   ][   ][   ][   ]  [ Ac][   ][   ][   ]
=================tableaus=================
---1----2----3----4----5----6----7----8---
   7c   Kc   7h   Ah   5c   9c   8s   7d
   5s   8h   6h  10d   4d   Qh   3c   5h
   Jc   2h   Qs   3d   Js   As   6s   Kh
   7s   6d   3h   4s   5d   Jh   3s  10s
   Qc   9h   8d   Ks   4h   6c   9s   2c
   Jd   9d   Kd   Ad  10c   2d   2s  10h
        Qd   4c   8c
Please input the command:
```

**Quit **

Input `q` or `Q`, then the game will exit

```
=======Cells========  ====Foundations=====
---1----2----3----4--  --1----2----3----4--
 [   ][   ][   ][   ]  [ Ac][   ][   ][   ]
=================tableaus=================
---1----2----3----4----5----6----7----8---
   7c   Kc   7h   Ah   5c   9c   8s   7d
   5s   8h   6h  10d   4d   Qh   3c   5h
   Jc   2h   Qs   3d   Js   As   6s   Kh
   7s   6d   3h   4s   5d   Jh   3s  10s
   Qc   9h   8d   Ks   4h   6c   9s   2c
   Jd   9d   Kd   Ad  10c   2d   2s  10h
        Qd   4c   8c
Please input the command: q
```

