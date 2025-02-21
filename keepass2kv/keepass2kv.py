from os import environ

import hvac
from pykeepass import PyKeePass


class Keepass2Kv:
    def __init__(self):
        self.kv_secrets = []

    def export(self):
        kp = PyKeePass(environ["KEEPASS_KDBX"], password=environ["KEEPASS_PASSWORD"])
        for entry in kp.entries:
            entry_data = {
                "username": ("" if entry.username is None else entry.username.strip()),
                "password": "" if entry.password is None else entry.password,
                "url": "" if entry.url is None else entry.url.strip(),
                "notes": "" if entry.notes is None else entry.notes.strip(),
                "group": entry.group.name,
                "path": entry.path,
                "tags": entry.tags,
            }
            path = (
                "/".join(entry.path).replace("\n", "").replace(" ", "-").strip().lower()
            )
            entry_data["path"] = path
            yield entry_data

    def import_kv(self):
        client = hvac.Client(
            url=environ["VAULT_URL"],
            token=environ["VAULT_TOKEN"],
        )
        if client.is_authenticated():
            client.secrets.kv.v2.create_or_update_secret(
                mount_point=environ["VAULT_MOUNT_POINT"],
                path=self.kv_secrets["path"],
                secret=self.kv_secrets,
            )
