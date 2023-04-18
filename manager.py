from person import Person
class Manager(Person):
    
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000, job='manager')
    print(tom.lastName())
    tom.giveRaise(.20)
    print('%.2f' % tom.pay)
    