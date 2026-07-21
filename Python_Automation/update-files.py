# Assign `import_file` to the name of the file 

import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed to access restricted information. 

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# We use the `with` statement to open and store it in the file 

with open(import_file, "r") as file:
 
 # We use the `.read()` to read the imported file and store it in a variable named `ip_addresses`

    ip_addresses = file.read()
    
    # split for iteration
    
    ip_addresses = ip_addresses.split()

# We build iterative statement through ip_addresses list and Name loop variable `element`

for element in remove_list:

  #We use the conditional statement If, to remove ip addresses contain in `remove_list from ip_addresses list
  
    if element in ip_addresses:

        # then current element should be removed from `ip_addresses`

         ip_addresses.remove(element)

# Convert `ip_addresses` back to a string so that it can be written into the text file 

ip_addresses = "\n".join(ip_addresses) 

# Build `with` statement to rewrite the original file

with open(import_file, "w") as file:

  # Rewrite the file, replacing its contents with `ip_addresses`

  file.write(ip_addresses)

  # Build `with` statement to read in the updated file

with open(import_file, "r") as file:

    # Read in the updated file and store the contents in `text`

    text = file.read()

# Display the contents of `text`

print(text)