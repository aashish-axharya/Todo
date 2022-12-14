from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError

class TestTodo(TransactionCase):
	def test_create(self):
	"Create a todo"
	Todo = self.env('todo.task')
	task = Todo.create({'name': 'Test Task'})
	self.assertEqual(task.is_done, False)
	
	#Toggle done test
	task.do_toogle_done()
	self.assertTrue(task.is_done)
	#Clear done test
	Todo.do_clear_done()
	self.assertFalse(task.active)

	def setUp(self,*args,**kwargs):
		result = super(TestTodo, self).setUp(*args,\**kwargs)
		user_demo = self.env.ref('base.user_demo')
		self.env = self.env(user=user_demo)
		return result

	def test_record_rule(self):
		"Test per user"
		Todo = self.env['todo.task']
		task = Todo.sudo().create({'name':'Admin Task'})
		with self.assertRaises(AccessError):
			Todo.browse([task.id]).name

