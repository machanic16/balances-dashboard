from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    parent_company = models.ForeignKey('self', on_delete=models.SET_NULL , null=True,blank=True)    

    def __str__(self) -> str:
        return self.name + '\n'

class Store(models.Model):

    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)

    company =  models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.company.name + '-' + self.name + '\n'
    
    def statuses(self):
        ''' Help: 
                0 : At least one rack is empty so is needed to visit the store
                1 : At least one rack needs to be filled but is no empty so is not an emergency
                2 : Some or all racks are good so don't need to be visited
                3 : All racks are full'''
        statuses = [rack.status for rack in self.rack_set.all()]
        if 'empty' in statuses:
            return 0
        elif 'needs_refil' in statuses :
            return 1
        elif len(set(statuses)) > 1 :
            return 2
        else :
            return 3

    

class Rack(models.Model):
    name = models.CharField(max_length=200,default='') 
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    status_choices = (
        ('full','Full'),
        ('empty','Empty'),
        ('good','Good'),
        ('needs_refill','Needs Refill')
    )
    status = models.CharField(max_length=30,choices=status_choices,default='empty')

    def __str__(self) -> str:
        return self.name + '-->'+ self.store.company.name +'-'+ self.store.name + '\n'



class Shelf(models.Model):
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    max_weight = models.FloatField()
    min_weight = models.FloatField()

    def __str__(self) -> str:
        return self.name + '\n'

