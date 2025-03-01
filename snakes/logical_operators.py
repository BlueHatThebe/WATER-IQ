is_coding = True
is_not_coding = False


print("is_coding AND is_not_coding:", is_coding and is_not_coding)

print("is_coding OR is_not_coding:", is_coding or is_not_coding)

print("NOT is_coding:", not is_coding)
print("NOT is_not_coding:", not is_not_coding)

print("is_coding AND (NOT is_not_coding):", is_coding and (not is_not_coding))
print("(NOT is_coding) OR is_not_coding:", (not is_coding) or is_not_coding)