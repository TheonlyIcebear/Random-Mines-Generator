# Random-Mines-Generator 🤖
A simple discord application that will generate a random grid of emoji's replicating a game of mines
![image](https://user-images.githubusercontent.com/78031685/194453909-70489ad7-99b4-48ad-be3f-bfcdcb6fd769.png)

# Explanation 🧠
It's super simple and it just takes the SHA256 hash of the user's inputed gameid, converts that hash into a base10 number
```py
>> hash = str(int(hashlib.sha256(gameid.encode('utf-8')).hexdigest(), 16))[1:]
```
then it loops through the hash variable 2 characters at a time using that 2 digit number and using `number % length_of_choiches` prevents the number from being larger than the list
```py
for x in range(0, int(mines)*2, 2):
        print(x, x+2)
        if not x:
            n = int(hash[x : x+2])
        else:
            n = int(hash[x-2 : x])

        n = choices[n % len(choices)]
        choices.remove(n)


        print(n, n // 5, n % 5)

        t = [* msg[n // 5]]
        t[n % 5] = "✅"
        msg[n // 5] = ''.join(t)
        print(msg)

    msg = '\n'.join(msg)

```

This method of generation also ensures you get a random random result that still will give the same result if the same arguements are provided
