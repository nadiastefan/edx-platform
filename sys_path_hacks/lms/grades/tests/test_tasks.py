from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'grades.tests.test_tasks')

from lms.djangoapps.grades.tests.test_tasks import *
