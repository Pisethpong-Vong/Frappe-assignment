# Copyright (c) 2021, nomotoji and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Staff(Document):
	def before_save(self):
		self.fullname = f'{self.first_name}{self.last_name}'
