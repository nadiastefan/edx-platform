from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'course_api.blocks.transformers.milestones')

from lms.djangoapps.course_api.blocks.transformers.milestones import *
