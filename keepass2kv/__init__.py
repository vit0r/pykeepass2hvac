from .keepass2kv import Keepass2Kv

if __name__ == "main":
    kv = Keepass2Kv()
    kv.kv_secrets = kv.export()
    kv.import_kv()
