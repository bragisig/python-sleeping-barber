from threading import Thread, Lock, BoundedSemaphore, Event
import time, random

mutex = Lock()

class BarberShop:
	waitingCustomers = []

	def __init__(self, barber, numberOfSeats):
		self.barber = barber
		
		self.numberOfSeats = numberOfSeats
		self.seatSemaphore = BoundedSemaphore(numberOfSeats)

		print 'BarberShop initilized with {0} seats'.format(numberOfSeats)

	def openShop(self):
			thread = Thread(target = self.barberGoToWork)
			thread.start()

	def barberGoToWork(self):
		while True:
			mutex.acquire()
			if len(self.waitingCustomers) > 0:
				mutex.release()
				self.serviceNextCustomer()
			else:
				mutex.release()
				barber.sleep()
			

	def enterBarberShop(self, customer):
		print '>> {0} entered the shop and is looking for a seat'.format(customer.name)
		self.seatSemaphore.acquire()
		#protect the list with a mutex
		mutex.acquire()
		self.waitingCustomers.append(c)	
		print '{0} sat down in the waiting room'.format(customer.name)
		mutex.release()
		
		#Wake up the barber if asleep
		barber.wakeUp()

	def serviceNextCustomer(self):
		mutex.acquire()

		if len(self.waitingCustomers) > 0:
			self.seatSemaphore.release()
			c = self.waitingCustomers.pop(0)
				
		mutex.release()

		self.barber.cutHair(c)

		print '{0} is done'.format(c.name)

class Customer:
	def __init__(self, name):
		self.name = name

class Barber:
	barberWorkingEvent = Event()

	def sleep(self):
		self.barberWorkingEvent.wait()

	def wakeUp(self):
		if not self.barberWorkingEvent.isSet():
			self.barberWorkingEvent.set()

	def cutHair(self, customer):
		#Set barber as busy
		print '{0} is having a haircut'.format(customer.name)
		self.barberWorkingEvent.clear()

		#Is cutting hair
		randomHairCuttingTime = random.randrange(3, 10+1)
		time.sleep(randomHairCuttingTime)
		

if __name__ == '__main__':
	customers = []
	customers.append(Customer('Bragi'))
	customers.append(Customer('Auja'))
	customers.append(Customer('Iris'))
	customers.append(Customer('Axel'))
	customers.append(Customer('Andrea'))
	customers.append(Customer('Agnar'))
	customers.append(Customer('Mamma'))
	customers.append(Customer('Solla'))
	customers.append(Customer('Olla'))
	customers.append(Customer('Berglind'))
	customers.append(Customer('Bergdis'))
	customers.append(Customer('Margret'))
	customers.append(Customer('Brynjar'))
	customers.append(Customer('Siggi'))
	customers.append(Customer('Tomas'))
	customers.append(Customer('Kristrun'))
	customers.append(Customer('Heidrun'))

	barber = Barber()

	barberShop = BarberShop(barber, numberOfSeats=3)
	barberShop.openShop()


	while len(customers) > 0:
		#Arriving customers
		#randomCustomerIndex = random.randrange(0, len(customers))
		#c = customers[randomCustomerIndex]

		c = customers.pop()	

		#New customer enters the barbershop
		barberShop.enterBarberShop(c)

		customerInterval = 1 #random.randrange(1,6)

		time.sleep(customerInterval)

	thread.join()

	print '\nAll done!'

		


