# Random-Mines-Generator 🤖
A simple discord application that will generate a random grid of emoji's replicating a game of mines
![image](https://user-images.githubusercontent.com/78031685/194453909-70489ad7-99b4-48ad-be3f-bfcdcb6fd769.png)

# Explanation 🧠
It's super simple and it just takes the SHA256 hash of the user's inputed gameid, converts that hash into a base10 number
```py
>> hash = str(int(hashlib.sha256(gameid.encode('utf-8')).hexdigest(), 16))[1:]
```
then it loops through the hash variable 2 characters at a time using that 2 digit number as the seed for the random selection in the list to determine which item is selected, then it removes that number from the list to prevent it from being picked twice or more
```py
for x in range(0, int(mines)*2, 2):
        print(x, x+2)
        if not x:
            n = int(hash[x : x+2])
        else:
            n = int(hash[x-2 : x])

        random.seed(n)
        n = random.choice(choices)
        choices.remove(n)


        t = [* msg[n // 5]]
        t[n % 5] = "✅"
        msg[n // 5] = ''.join(t)
```
