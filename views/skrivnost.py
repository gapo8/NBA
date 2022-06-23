import hashlib
# Initialize the empty message using SHA-256
message = hashlib.sha256()
 
# Update the message using byte strings
message.update('gasper1234'.encode("utf-8"))

 
# Print the message digest
print(message.hexdigest())

def nastaviSporocilo(sporocilo = None):
    return sporocilo
    
nastaviSporocilo('sporocilo = None')