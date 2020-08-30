from . import models

class queries():
    def __init__(self):
        self.positions = models.position.objects
        self.needs = models.need.objects
        self.damages = models.damage.objects

    def allData(self):
        return {
            "cards": {
                'positionsCount': self.positions.all().count(),
                'positionsInNeed': self.needs.filter(status=True).count(),
                'servedPositions': 5,
                'damagesCount': self.damages.all().count(),
            },
            "tables": {
                'positions': self.positions.all(),
                'damages': self.damages.all(),
                'needs': self.needs.all()
            }
        }

    def userStats(self, userId):
        return {
            'positionsCount': self.positions.filter(user=userId).count(),
            'positionsInNeed': self.needs.filter(status=True).filter(user=userId).count(),
            'servedPositions': 5,
            'damagesCount': self.damages.filter(user=userId).count(),
        }
    
    def userData(self, userId):
        return {
            "cards": self.userStats(userId),
            "tables": {
                'positions': self.positions.filter(user=userId),
                'damages': self.damages.filter(user=userId),
                'needs': self.needs.filter(user=userId)
            }
        }
        