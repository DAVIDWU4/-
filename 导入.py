import 函数
acc = ["dfasf","1242ffz","rgkurdh","dhsgejhs"]
函数.show_message(acc)

from 函数 import show_message
acc = ["dfasf","1242ffz","rgkurdh","dhsgejhs"]
answer= show_message(acc)
print(answer)

from printing_functions import show_message as fn
acc = ["dfasf","1242ffz","rgkurdh","dhsgejhs"]
fn(acc)

import printing_functions as mn
acc = ["dfasf","1242ffz","rgkurdh","dhsgejhs"]
mn.show_message(acc)

from printing_functions import *
acc = ["dfasf","1242ffz","rgkurdh","dhsgejhs"]
show_message(acc)