cl = [int(x) for x in open("test.txt", "r").read().split("\n")]

def nagivate_volts(ls, small, big,):
    def navigation_software(cur, lows, highs):
        if cur == max(ls):
            return lows * (highs+1)
        for adapter in ls:
            if adapter == cur + small:
                return navigation_software(adapter, lows+1, highs)
        for adapter in ls:
            if adapter == cur + big:
                return navigation_software(adapter, lows, highs+1)
    return navigation_software(0, 0, 0)

def pathways_volts(ls, small, big):
    paths = 0
    def pathway_software(cur):
        if cur == max(ls):
            return 1
        smalls = 0
        bigs = 0
        print(cur)
        if cur + small in ls:
            smalls = pathway_software(cur + small)
        else: smalls = 0
        if cur + big in ls:
            bigs = pathway_software(cur + big)
        else: bigs = 0
        return smalls + bigs
    return pathway_software(0)

#print(nagivate_volts(cl, 1, 3))
print(pathways_volts(cl, 1, 3))