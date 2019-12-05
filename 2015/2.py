presents = []
with open('2.in') as f:
    for x in f.read().splitlines():
        presents.append([int(y) for y in x.split('x')])

paper_sqft = 0
ribbon_ft = 0
for p in presents:
    s = sorted(p)
    paper_sqft += 2*p[0]*p[1] + 2*p[1]*p[2] + 2*p[0]*p[2] + s[0]*s[1]
    ribbon_ft += p[0]*p[1]*p[2] + s[0]+s[0]+s[1]+s[1]
print(paper_sqft)
print(ribbon_ft)
