import json

# Our dictionary with the final data
final={}

# Read the file with our data
with open("dictionary_compact.json") as f:
    data = json.load(f)

# Parse each input and put it into final
for word in data:
    # get rid of unnecessary characters and split each definition into it's corresponding word.
    current = word.strip(',').strip('.').strip('-').lower().split()
    for thing in current:
        if thing in final:
            # If it has a current value, increment it.
            final[thing]+=1
        else:
            # Add it into the dictionary
            final[thing] = 1

# A sorted list containing {the word itself:the number of occurrences in other words} in ascending order.
final = [{k: v} for k, v in sorted(final.items(), key=lambda item: item[1])]

with open('wordfrequency.json', 'w+') as json_file:
    json.dump(final, json_file)

