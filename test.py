import random, hashlib
import datetime
for i in range(423):
    f = open(f'AllFiles/{i}.txt', 'w')
    f.write(str(random.randint(1000, 10000)))
    f.close()

# for i in range(5):
#     val = random.randint(0, 50)
#     f = open(f"cached_file/{val}.txt", "w")
#     file = open(f'AllFiles/{val}.txt', 'r')
#     f.write(file.read())
#     file.close()
#     f.close()

