from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'support.serializers')

from lms.djangoapps.support.serializers import *
