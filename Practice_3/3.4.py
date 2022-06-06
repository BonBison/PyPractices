a = [77, 'abc']
def from_string_to_list(string, a):
   a.extend(map(int, string.split()))

from_string_to_list("", a)
print(*a)