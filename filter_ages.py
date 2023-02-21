import pandas as pd

# subsetting data
data = pd.read_csv("ages_stats_canada.csv").iloc[:, [0, 5]].head(
    22)  # first 22 entries are data, rest is bs


# convert populations to percentages
population_sizes = data.iloc[:, 1]


# these are all strings: '260,542' so need to convert to numbers
temp = population_sizes.values.tolist()
bucket_sizes = []

for t in temp:
    number = int(t.replace(',', ''))
    bucket_sizes.append(number)


size_of_population = bucket_sizes[0]


percentages = []

# skip first entry as its total population
for i in range(1, len(bucket_sizes)):
    percent = round(bucket_sizes[i]/size_of_population*100, 3)
    percentages.append(percent)



# find the min and max for each bucket, and add the buckets total percentage / max-min for each value between them inclusive
def add_to_list(min, max, percent, list):
    repetitions = max-min+1
    number_to_add = percent/repetitions

    for i in range(repetitions):
        list.append(number_to_add)

    return list


buckets_as_strings = data.iloc[:, 0].values.tolist()

population_percent = []

# add data to list
for i in range(1, len(buckets_as_strings)-1):
    string = buckets_as_strings[i]

    min = ''
    max = ''
    violated = False  # have we finished chars from min and are on to max

    for s in string:
        if not violated and str.isdigit(s):
            min += s
        
        elif not violated and not str.isdigit(s):
            violated = True
        
        elif violated and str.isdigit(s):
            max += s


    add_to_list(int(min), int(max), percentages[i], population_percent)
    # excluding 100 year olds and up since the data works without it


ages = []

for i in range(100):
    ages.append(i)



a = {'Age: ': ages, 'Percentage of Population': population_percent}
formatted_data=pd.DataFrame(data=a)

formatted_data.to_csv('ages.csv')
