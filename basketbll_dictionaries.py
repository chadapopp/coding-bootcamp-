class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

    def __repr__(self):
        return "Player: {}, Age: {}, Position: {}, Team: {}".format(
            self.name, self.age, self.position, self.team
        )



kevin = {"name" : "Kevin Durant", "age": 34, "position": "Small Forward", "team": "Brooklyn Nets"}
jason = {"name" : "Jason Tatum", "age": 24, "position": "Small Forward", "team": "Boston Celtics"}
kyrie = {"name" : "Kyrie Irving", "age": 32, "position": "Point Guard","team": "Brooklyn Nets"}
damian = {"name" : "Damian Lillard", "age": 33, "position": "Point Guard","team": "Portland Trailblasers"}
joel = {"name" : "Joel Embiid", "age": 32, "position": "Power Forward","team": "Philadelphia 76ers"}


player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)
player_damian = Player(damian)
player_joel = Player(joel)

print(player_kevin)
print(player_jason)
print(player_kyrie)
print(player_damian)
print(player_joel)


players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, 
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, 
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, 
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    }
]

new_team = []
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

print(new_team)
