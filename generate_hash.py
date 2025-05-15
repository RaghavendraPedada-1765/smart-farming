import hashlib

def hash_password(password, algorithm='md5'):
    encoded_password = password.encode('utf-8')
    if algorithm == 'md5':
        return hashlib.md5(encoded_password).hexdigest()
    return None

password_to_hash = "password"
hashed_password = hash_password(password_to_hash)

with open("weak_hash.txt", "w") as f:
    f.write(f"user1:{hashed_password}\n")

print(f"MD5 hash of '\{password_to_hash\}' written to weak_hash.txt")