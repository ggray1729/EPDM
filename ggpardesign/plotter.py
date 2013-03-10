def plt(zd):
    #put this here because I'm lazy
    from pylab import *
    from matplotlib.ticker import MultipleLocator, FormatStrFormatter

    t = arange(0.0, 100.0, 0.1)
    #s = sin(0.1*pi*t)*exp(-t*0.01)

    ax = subplot(111)
    for x in range(len(zd)-1):
        plot(zd[0],zd[x+1], alpha=0.02, color='black', linewidth=3.0)

    minorticks_on()

    grid(which="both")

    xticks(fontsize='xx-large')
    yticks(fontsize='xx-large')

    xlabel("Galvanometer current(mA)", fontsize='x-large')
    ylabel("$R_{y}(\Omega)$", fontsize='x-large')

    show()

    return None

if __name__ == "__main__":
    filename = "mcgood2.csv"
    import csv
    f = open(filename)
    c = csv.reader(f)  
    d = []
    for line in c:
        d.append(map(lambda x: float(x), line))
    zd = zip(*d)
    zd2 = []
    zd2.append(map(lambda x: 1000*x, zd[0]))
    for x in zd[1:]:
        zd2.append(x)
    plt(zd2)
