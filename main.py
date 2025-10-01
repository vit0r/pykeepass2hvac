from keepass2kv.keepass2kv import Keepass2Kv
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    kv = Keepass2Kv()
    kv.kv_secrets = kv.export()
    kv.import_kv()
