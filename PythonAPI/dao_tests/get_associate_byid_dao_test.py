import unittest


from daos.daos_impl.associate_dao_impl import AssociateDAOImpl

associate_dao = AssociateDAOImpl()


class AssociateTest(unittest.TestCase):
    def test_get_associate_by_id(self):
        assert associate_dao.get_associate_by_id(5)

