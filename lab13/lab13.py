class Delivery_personnel: 
	def __init__(self, years_of_services, company, is_drone, zip_codes_covered, name = None):
		
		self.years_of_services 	= years_of_services
		self.company			= company
		self.is_drone 			= is_drone
		self.zip_codes_covered	= zip_codes_covered
		
	
	#Getters
	def get_years_of_services (self): 
		return (self.years_of_services)
	def get_company(self): 
		return (self.company)
	def get_zip_codes_covered(self): 
		return (self.zip_codes_covered)

	#Setters
	def set_years_of_services (self, y): 
		self.years_of_services = y
	def set_company (self, c): 
		self.company = c 
	def set_zip_codes_covered (self,z): 
		self.zip_codes_covered = z

	#Recursive deliver method
	def deliver_rec(self,zip_list): 

		zip_list = [i for i in zip_list if i not in self.zip_codes_covered]
		if(int(len(zip_list)) == 1):
			print ("deliver to house", (zip_list[0]))
		else: 
			first_half = zip_list[:len(zip_list)//2]
			second_half = zip_list [len(zip_list)//2:]
			return (self.deliver_rec(first_half))
			return (self.deliver_rec(second_half))
def main(): 

	first_person	= Delivery_personnel(name = 'Hieu', years_of_services = 2, company = 'FedEx', is_drone = True, zip_codes_covered = ['03820','20016','100000','23476','29304'])
	z_list 			= ['03820','20016','54280','100000']
	
	return (first_person.deliver_rec(z_list))

if __name__ == '__main__':
	main()

