friends = dict()
completeList = set()

# Read input
nStudents, nFriendships = input().split()
completeList.update(range(1, int(nStudents)+1))
for j in range (0, int(nFriendships)):
    friend1, friend2 = input().split()
    if friend1 not in friends:
        friends[friend1] = set()
    if friend2 not in friends:
        friends[friend2] = set()
    friends[friend1].add(int(friend2))
    friends[friend2].add(int(friend1))

# Create set of not-friends
for key, valueSet in friends.items():
    transition = set()
    transition.add(int(key))
    friends[key] = completeList.difference(transition).difference(valueSet)

# Check group formation
def canFormGroups(friends, initial, initialized1 = False, initialized2 = False):
    group1 = set()
    group2 = set()
    if not initialized1:
        group1.add(int(initial))
        initialized1 = True
    for notFriend in friends[initial]:
        group1.add(notFriend)
    for key, valueSet in friends.items():
        if key == initial:
            continue
        else:
            if int(key) not in group1:
                if not initialized2:
                    group2.add(int(key))
                else:
                    if valueSet.issuperset(group2):
                        return False
                    group2.add(int(key))
    return True

# Check for possible groups
for key, valueSet in friends.items():
    if not canFormGroups(friends, key, valueSet):
        print("No")
print("Yes")
