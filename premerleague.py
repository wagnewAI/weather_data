teams = ["man utd", "arsenal", "man city", "liverpool", "aston villa", "tottenham", "newcastle", "brighton", "westham", "chelsea", "brentford", "wolves", "crystal palace", "fulham", "nottm forest", "bournemouth", "luton", "sheff utd", "everton", "burnely"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)
