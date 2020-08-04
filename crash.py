# String
message = "I learn coding"
print(message)

name = "ada lovelace"
print(name.title())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello,{full_name.title()}!")

name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)

name = "ALBERT"
name1 = "Robert"
name2 = "vido"
print(name.lower())
print(name1.upper())
print(name2.title())


quote = 'Albert Eistein once said,"A person who never made a mistake never tried anything new. " '
print(quote)

4/2

3.0**2

# List

universe_age = 12_000_000
print(universe_age)

bicycles = ['trek', 'canondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[3].upper())

motorcylces = ['honda', 'yamaha', 'suzuki']
last_owned = motorcylces.pop(1)
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Manipulation of the Guest list# Invite some people to dinner.
guests = ['guido van rossum', 'jack turner', 'lynn hill']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Jack can't make it! Let's invite Gary instead.
del(guests[1])
guests.insert(1, 'gary snyder')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'frida kahlo')
guests.insert(2, 'reinhold messner')
guests.append('elizabeth peratrovich')

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")






