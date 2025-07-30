secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("guess the secret number: "))
    if guess < secret_number:
        print ("too low")
    if guess > secret_number:
        print ("too high")

print ("you guessed it ! the secret number was ", secret_number)