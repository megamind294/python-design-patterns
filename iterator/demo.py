from iterator.course import CourseModules


if __name__ == "__main__":
    for module in CourseModules(["Databases", "Security", "AI"]):
        print(module)
