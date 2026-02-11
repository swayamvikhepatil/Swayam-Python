set1={1,2,3,5,6,2,2}
set2={1,3,2,4,5}
print(set1)
print(set2)
union_set=set1.union(set2)
print("Union set: ",union_set)
inter_set=set1.intersection(set2)
print("Intersection set: ",inter_set)
diff1_set=set1.difference(set2)
print("Difference of sets (set1-set2): ",diff1_set)
diff2_set=set2.difference(set1)
print("Difference of sets(set1-set2): ",diff2_set)
