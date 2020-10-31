class Team:
    def __init__(self):
        self.teamname = 'none'
        self.teamwins = 0
        self.team_losses = 0

    def set_teamname(self, teamname):
        self.teamname = teamname

    def set_teamwins(self, teamwins):
        self.teamwins = teamwins

    def set_team_losses(self, team_losses):
        self.team_losses = team_losses

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        percent = self.teamwins / (self.teamwins + self.team_losses)
        return percent


if __name__ == "__main__":

    team = Team()

    teamname = input()
    teamwins = int(input())
    team_losses = int(input())

    team.set_teamname(teamname)
    team.set_teamwins(teamwins)
    team.set_team_losses(team_losses)

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.teamname, 'has a winning average!')
    else:
        print('Team', team.teamname, 'has a losing average.')