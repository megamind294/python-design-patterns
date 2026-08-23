from iterator.course import CourseModules


def test_course_modules_iterate_in_insertion_order_and_can_repeat():
    modules = CourseModules(['Databases', 'Security', 'AI'])

    assert list(modules) == ['Databases', 'Security', 'AI']
    assert list(modules) == ['Databases', 'Security', 'AI']
