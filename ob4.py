class justCounter:
    __privateCounter = 0
    publicCounter = 0

    def count(self):
        self.__privateCounter += 1
        self.publicCounter += 1
        print(self.publicCounter)
        # return


counter = justCounter()
counter.count()
counter.count()

print(counter.publicCounter)
# print(counter.__privateCounter)
