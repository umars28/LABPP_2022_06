#Program02
#input second
seconds = int(input('Input detik: '))

#convert seconds to hours:minutes:seconds format
hours = int(seconds / 3600)
minutes = int((seconds % 3600) / 60)
seconds = int((seconds % 3600 % 60))

#print output
print("%02d:%02d:%02d" % (hours, minutes, seconds))