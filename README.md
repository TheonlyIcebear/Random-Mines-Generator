# Random-Mines-Generator 🤖
A simple discord application that will generate a random grid of emoji's replicating a game of mines
![image](https://user-images.githubusercontent.com/78031685/194453909-70489ad7-99b4-48ad-be3f-bfcdcb6fd769.png)

# Explanation 🧠
It's super simple and it just takes the SHA256 hash of the user's inputed gameid, converts that hash into a base10 number
```py
>> hash = str(int(hashlib.sha256(gameid.encode('utf-8')).hexdigest(), 16))[1:]
```
then it loops through the hash variable 2 characters at a time using that 2 digit number as the seed for the random selection in the list to determine which item is selected, then it removes that number from the list to prevent it from being picked twice or more
