with open('Delta_SkyMiles') as delta:
    delta_members = delta.read()
    delta.closed

with open('AAA') as aaa:
    AAA_members = aaa.read()
    aaa.closed

with open('library.txt') as library:
    library_members = library.read()
    library.closed

with open('Museum_of_Bash_History') as bash_history:
    bash_history_members = bash_history.read()
    bash_history.closed

delta_members_list = delta_members.splitlines()
AAA_members_list = AAA_members.splitlines()
library_members_list = library_members.splitlines()
bash_history_members_list = bash_history_members.splitlines()

intersect = [name for name in delta_members_list
             if name in AAA_members_list
             if name in library_members_list
             if name in bash_history_members_list]

print(intersect)
