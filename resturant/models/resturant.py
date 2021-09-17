from datetime import datetime

class Restaurant:
    name = ''
    type = ''
    # 24h format
    startTime = 10
    endTime = 20

    def isOpen(self):
        hours = datetime.today().hour
        print(hours)
        if self.startTime < hours and self.endTime > hours:
            return True
        return False