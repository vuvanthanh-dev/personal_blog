from hashids import Hashids

hashids = Hashids(
    salt="cGVyc29uYWwgYmxvZyAxOTg5Cg==",
    min_length=15
)

def encode_id(id: int) -> str:
    return hashids.encode(id)

def decode_id(hash_id: str) -> int | None:
    ids = hashids.decode(hash_id)
    return ids[0] if ids else None
