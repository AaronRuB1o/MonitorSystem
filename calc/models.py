from django.db import models

# Create your models here.
class Monitoring(models.Model):
    Site = models.CharField(max_length=255)
    PC_tag = models.CharField(max_length=255, db_column='PC-Tag')
    MAC = models.CharField(max_length=255, primary_key=True)
    User = models.CharField(max_length=255)
    Local_IP = models.CharField(max_length=255)
    Patch_V2 = models.CharField(max_length=255)
    vpncfg_nc = models.CharField(max_length=255)
    x_scr = models.CharField(max_length=255)
    x_zm = models.CharField(max_length=255)
    ldap_ipa2 = models.CharField(max_length=255)
    ldaprs = models.CharField(max_length=255)
    chmd_ipa = models.CharField(max_length=255)
    incog = models.CharField(max_length=255)

    def __str__(self):
        return self.Site

    class Meta:
        db_table = 'Monitoring'