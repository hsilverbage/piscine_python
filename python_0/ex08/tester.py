from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
	sleep(0.05)
# print()
# for elem in tqdm(range(333)):
# 	sleep(0.05)
# print()

# words = ["a", "b", "c", "d","a", "b", "c", "d","a", "b", "c", "d","a", "b", "c", "d"]

# for word in tqdm(words):
#     sleep(0.5)
