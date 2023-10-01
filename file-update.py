# The variable import_file stores the url of the file I'm working with
import_file = "allow_list.txt"

# Now I open the file to read it
with open (import_file, "r") as file:

    # The string ip_addresses stores the content of the file converted to string
    ip_addresses = file.read()

# I convert the string into an array to easily manipulate it
# The variable ip_addresses is reassigned to the array
ip_addresses = ip_addresses.split()

# Now I open another file that contains the ip addresses to remove
with open("to_remove.txt", "r") as file:
    ip_addresses_to_remove = file.read()
ip_addresses_to_remove = ip_addresses_to_remove.split()

# Now I am ready to loop through the list of the addresses that must be removed 
# and remove the corresponding ip addresses in the allowed list
for i in ip_addresses_to_remove:
    if(i in ip_addresses):
        ip_addresses.remove(i)

# I reassign the variable ip_addresses to a sting
ip_addresses = " ".join(ip_addresses)

# Now I am ready to update the allowed ip addresses file
with open(import_file, "w") as file:
    file.write(ip_addresses)