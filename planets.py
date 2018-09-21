def weight_on_planets():
    i = input("What do you weigh on earth? ")
    weight = float(i)
    mars_w = weight * 0.38
    jupiter_w = weight * 2.34
    print "\nOn Mars you would weigh", mars_w, "pounds.\nOn Jupiter you would weigh", jupiter_w, "pounds."


if __name__ == '__main__':
    weight_on_planets()
