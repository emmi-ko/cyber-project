from django.contrib.auth.hashers import BasePasswordHasher
# Create your models here.

class LegacyPasswordHasher(BasePasswordHasher):
    algorithm = 'legacy_hasher'

    def encode(self, password: str, salt: str):
        return password

    def verify(self, password: str, encoded: str):
        return password
