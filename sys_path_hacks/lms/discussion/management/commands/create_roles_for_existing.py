from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'discussion.management.commands.create_roles_for_existing')

from lms.djangoapps.discussion.management.commands.create_roles_for_existing import *
