

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Or(And):
    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        
        return False

class Not:
    def __init__(self, matcher) -> None:
        self._matcher = matcher
    def test(self, player):
        return not self._matcher.test(player)


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan(HasAtLeast):
    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class All:
    def test(self, player):
        return True

class QueryBuilder:
    def __init__(self, pino = All()) -> None:
        self.pino_olio = pino
    
    def playsIn(self, team):
        return QueryBuilder(And(self.pino_olio, PlaysIn(team)))
    
    def hasAtLeast(self, value, attribute):
        return QueryBuilder(And(self.pino_olio, HasAtLeast(value, attribute)))
    
    def hasFewerThan(self, value, attribute):
        return QueryBuilder(And(self.pino_olio, HasFewerThan(value, attribute)))
    
    def oneOf(self, query1, query2):
        return QueryBuilder(And(self.pino_olio, Or(query1, query2)))
    
    def build(self):
        return self.pino_olio