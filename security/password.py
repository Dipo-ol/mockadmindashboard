from pwdlib import PasswordHash


Password_hash = PasswordHash.recommended() #creates the password hasing object


def hash_password(password:str) -> str:
    return Password_hash.hash(password)

def verify_password(password:str,hashed_password:str) -> bool:
    return Password_hash.verify(password,hashed_password)