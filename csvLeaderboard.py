import csv

'''
Demo on how to use reader and writer from csv module.
Uncomment and run one function call at a time to see how leaderboard.csv changes.
'''

def read():
    with open('leaderboard.csv', mode='r') as f:
        reader = csv.reader(f)
        for name, score in reader:
            print(name, score)

# overwrites the entire file
def write():
    with open('leaderboard.csv', mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(['Mike', 43])
        writer.writerow(['Ishaan', 24])
        writer.writerow(['Grace', 18])
        print('finished writing rows')

# creating 2D list of [name, score] leaderboard data to use when updating
def readLeaderboard():
    with open('leaderboard.csv', mode='r') as f:
        reader = csv.reader(f)
        leaderboard = [row for row in reader]
    return leaderboard

# updating score for specific name; if name not in leaderboard, add as new row
# write updated leaderboard data to file
def updateLeaderboard(leaderboard, name, score):
    with open('leaderboard.csv', mode='w') as f:
        writer = csv.writer(f)
        updated = False
        for row in leaderboard:
            if row[0] == name:
                row[1] = score
                updated = True
                break
        if not updated:
            leaderboard.append([name, score])
        for row in leaderboard:
            writer.writerow(row)

# update Mike's score to be 100
def leaderboardExample():
    leaderboard = readLeaderboard()
    print('before update', leaderboard)
    updateLeaderboard(leaderboard, 'Mike', 100)
    print('after update', leaderboard)
    
# read()
# write()
# leaderboardExample()
