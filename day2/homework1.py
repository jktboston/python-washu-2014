class School():
  def __init__(self, school):
    self.school = school
    self.db = {}

  def add(self, name, grade):
  	if grade in self.db:
  		self.db[grade].add(name)
  	else: self.db[grade] = {name}

  def sort(self):
		sorted_students={}
		for key in self.db.keys():
			sorted_students[key] = tuple(sorted(self.db[key]))
		return sorted_students
  
  def grade(self, check_grade):
  	if check_grade in self.db: 
  		return self.db[check_grade]
  	else: return None
