inventory = [
    {
        'listOwner': 'Melissa',
        'listItems': [
            {'location': 'Living Room', 'count': 1, 'items': [
                {'item':'couch'}
            ]},
            {'location': 'Living Room', 'count': 2, 'items': [
                {'item':'Left End Table'},
                {'item':'Right End Table'}
            ]}
        ]
    },
    {
        'listOwner': 'Mel'
    }
]
# print(inventory)
# print(inventory[0])
melissa = inventory[0]
mel = inventory[1]
# print("Melissa's list: ", melissa)
# print("List owner: ", melissa['listOwner'])

def printOwner(user):
    print(f"{user['listOwner']}'s list")

printOwner(inventory[0])

def printItems(user):
    #print(f"{user['listItems']}")
    for items in user['listItems']:
        for item in items['items']:
            print(f"- {item['item']}")

printItems(melissa)

def wrong():
    print("Sorry not a match")

def if_one(user, owner):
    if(user['listOwner'] == owner):
        printItems(user)
    else:
        print(wrong())


if_one(melissa, "Melissa")
if_one(mel, "Melissa")



