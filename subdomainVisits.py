def subdomainVisits(cpdomains):
    cpsubdomains = {}
    for cpd in cpdomains:
        cpd_split = cpd.split()
        count = int(cpd_split[0])
        domain = cpd_split[1]
        while len(domain) > 0:
            if domain in cpsubdomains:
                cpsubdomains[domain] += count
            else:
                cpsubdomains[domain] = count
            if '.' in domain:
                dot_index = domain.index('.')
                domain = domain[dot_index+1:]
            else:
                domain = ""
    cpsubs = []
    for dom, c in cpsubdomains.items():
        cpsubs.append(str(c) + " " + dom)
    return cpsubs
