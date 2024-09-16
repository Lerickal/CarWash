from django.db import models

class CarWash(models.Model):
    CarWashID = models.AutoField(primary_key=True)
    NM_Number = models.CharField(max_length=255, unique=True)
    CarWashName = models.CharField(max_length=255)
    RegisteredBusinessName = models.CharField(max_length=255)
    RegistrationNo = models.CharField(max_length=255)

    def __str__(self):
        return self.CarWashName

class Owner(models.Model):
    OwnerID = models.AutoField(primary_key=True)
    OwnerNameSurname = models.CharField(max_length=255)
    OwnerIDNumber = models.CharField(max_length=255)
    ContactNumber = models.CharField(max_length=50)
    EmailAddress = models.EmailField(max_length=255)
    CarWashID = models.ForeignKey(CarWash, on_delete=models.CASCADE)

    def __str__(self):
        return self.OwnerNameSurname

class Compliance(models.Model):
    ComplianceID = models.AutoField(primary_key=True)
    CIPC = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    BusinessBankAccount = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    SARS_PIN = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    Ownership = models.CharField(max_length=10, choices=[('Private', 'Private'), ('Franchise', 'Franchise')])
    CarWashID = models.ForeignKey(CarWash, on_delete=models.CASCADE)

    def __str__(self):
        return f"Compliance for CarWash ID: {self.CarWashID_id}"

class Location(models.Model):
    LocationID = models.AutoField(primary_key=True)
    PhysicalAddress = models.CharField(max_length=255)
    GPSCoordinates = models.CharField(max_length=50)
    CityTownship = models.CharField(max_length=100)
    Province = models.CharField(max_length=100)
    CarWashID = models.ForeignKey(CarWash, on_delete=models.CASCADE)

    def __str__(self):
        return f"Location of {self.CityTownship}, {self.Province}"

class Joining(models.Model):
    JoiningID = models.AutoField(primary_key=True)
    JoiningDate = models.DateField()
    CarWashID = models.ForeignKey(CarWash, on_delete=models.CASCADE)

    def __str__(self):
        return f"Joined on {self.JoiningDate}"



# Create your models here.
