person = {
  "name":"keertana",
  "age":45,
  "course":"cse"
}

asc = {k:v for k,v in sorted(person.items(), key=lambda item:item[0])}
print(asc)

