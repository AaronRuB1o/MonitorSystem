from faker import Faker
from calc.models import Monitoring
import random

fake = Faker()

sites = ['Manila', 'Cebu', 'Davao', 'Clark']
patch_versions = [f"v{major}.{minor}" for major in range(1, 5) for minor in range(10)]

for _ in range(30):  # Generate 20 entries
    Monitoring.objects.create(
        Site=random.choice(sites),
        PC_tag=f"PC-{random.randint(100, 999)}",
        MAC=fake.unique.mac_address(),
        User=fake.user_name(),
        Local_IP=fake.ipv4(),
        Patch_V2=random.choice(patch_versions),
        vpncfg_nc=f"vpn-{random.randint(1,100)}",
        x_scr=f"x_scr_{random.randint(1,5)}",
        x_zm=f"x_zm_{random.randint(1,5)}",
        ldap_ipa2=f"ldap_ipa2_{random.randint(1,5)}",
        ldaprs=f"ldaprs_{random.randint(1,5)}",
        chmd_ipa=f"chmd_ipa_{random.randint(1,5)}",
        incog=random.choice(["True", "False"])
    )

print("20 dummy Monitoring records inserted.")