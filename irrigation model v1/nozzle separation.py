import numpy

# will return the length of the coord
def chord(xcoord, spray_radius, nozzle_separation):
  return 2 * (numpy.sqrt(spray_radius**2 - (xcoord - nozzle_separation)**2))

def water_range(nozzle_separation, spray_radius):
  xi = 0.0
  xf = nozzle_separation
  spray_radius = spray_radius
  water = []
  for x in numpy.arange(xi, xf, 0.01):
    left_chord = chord(x, spray_radius, 0)
    right_chord = chord(x, spray_radius, nozzle_separation)
    if left_chord + right_chord >= 0:
      water.append(left_chord + right_chord)
  # print(water)
  maxmin = max(water) - min(water)
  return [maxmin, max(water), min(water)]

def optimize(max_nozzle_separation, spray_radius):
  xi = 25
  xf = max_nozzle_separation
  ranges = []
  nozzle_separation_value = []
  maximum = []
  minimum = []
  for x in numpy.arange(xi, xf, 0.1):
    # print(x)
    nozzle_separation_value.append(x)
    ranges.append(water_range(x, spray_radius)[0])
    maximum.append(water_range(x, spray_radius)[1])
    minimum.append(water_range(x, spray_radius)[2])
  print(min(ranges))
  print(ranges.index(min(ranges)))
  print(nozzle_separation_value[ranges.index(min(ranges))])
  print(maximum[ranges.index(min(ranges))])
  print(minimum[ranges.index(min(ranges))])
  # return nozzle_separation_value[ranges.index(min(ranges))]

# def optimize(min_nozzle_separation, max_nozzle_separation, )

def main():
  optimize(50, 25)
  return 0

main()
