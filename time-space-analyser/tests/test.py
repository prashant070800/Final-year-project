import tsanalyser
tsanalyser.getTSAnlaysis(100)
ram = tsanalyser.getCurrentRSS(100)

print(ram)

tsanalyser.startKeepingTime()

time = tsanalyser.getTimeTaken(100)

print(time)
