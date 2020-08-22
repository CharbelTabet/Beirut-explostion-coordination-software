from . import models

class queries():
    positions = models.position.objects
    needs = models.need.objects
    damages = models.damage.objects

    def cards(self):
        return {
            'positionsCount': self.positions.all().count(),
            'positionsInNeed': self.needs.filter(status= True).count(),
            'servedPositions': 5,
            'damagesCount': self.damages.all().count(),
        }
    
    def charts(self):
        return {
            'positionsXAxis': 'TODO',
            'positionsYAxis': 'TODO',
            'damagesXAxis': 'TODO',
            'damagesYAxis': 'TODO',
        }

    def tables(self):
        return {
            'positions': self.positions.all(),
            'damages': self.damages.all(),
            'needs': self.needs.all()
        }
    