import maven
from printer import *


class Plugin:
    def __init__(self, path, project, author, version, package, main, maven, spigot_version):
        self.path = path
        self.project = project
        self.author = author
        self.version = version
        self.package = package
        self.main = main
        self.maven = maven
        self.spigot_version = spigot_version

    def open(self):
        # Open our new project in IntelliJ.
        delay_print("Opening project in IntelliJ...\n\n", 0.01)
        os.chdir(self.path)
        os.system("idea.bat " + self.project)

    def build(self):
        print_loading()
        self.create_main_folder()
        self.create_libraries()
        self.create_package()
        self.create_main_class()

    def create_plugin_yml(self):
        with open("plugin.yml", 'w') as yml:
            yml.write("name: " + self.project + "\n")
            yml.write("version: " + self.version + "\n")
            yml.write("author: " + self.author + "\n")
            yml.write("main: " + self.package + "." + self.main)
            yml.close()

    def create_resources(self):
        os.mkdir("resources")
        os.chdir("resources")
        self.create_plugin_yml()
        os.chdir("..")

    def create_main_folder(self):
        path = self.path
        if not path.endswith("/"):
            path = path + "/"
        full_path = path + self.project
        os.mkdir(full_path)
        os.chdir(full_path)
        delay_print("\n\nCreated project folder " + full_path + "\n\n", 0.01)
        self.create_resources()

    def create_libraries(self):
        response = str(self.maven).lower()
        if response == "y":
            maven.generate_maven_file(self.package, self.project, self.version, self.spigot_version)
        if response == "n":
            self.add_library(self.spigot_version)

    def create_package(self):
        package = self.package
        if not str(package).startswith("src."):
            package = "src." + package
        package = str(package).split(".")
        for i in range(len(package)):
            temp = package[i]
            os.mkdir(temp)
            os.chdir(temp)
        delay_print("Created packages " + str(package) + "\n\n", 0.01)

    def create_main_class(self):
        with open(self.main + ".java", 'w') as file:
            file.write("package " + self.package + ";\n\n")
            file.write("public class " + self.main + " extends JavaPlugin {\n\n")
            file.write("\tpublic void onEnable() {\n\n\t}\n")
            file.write("}")
            file.close()
        delay_print("Created main class " + self.main + ".java\n\n", 0.01)


def validate_api_version(api):
    values = str(api).split(".")
    length = len(values)

    # The version must be 2-3 characters. (Example: 1.8 or 1.8.8)
    if length < 2 or length > 3:
        return False

    # The first number should always be 1.
    if int(values[0]) is not 1:
        return False

    version = int(values[1])

    # We do not allow versions below 1.7
    if version < 7:
        print("The minimum version is 1.7")
        return False

    # We do not allow versions above 1.15
    if version > 15:
        print("The maximum version is 1.15")
        return False

    return True


def build():
    print_title()

    try:
        path = delay_input("\n\n\tSpecify the path of the file: \n\n\t", 0.03)
        project = delay_input("\n\n\tSpecify the project's name: \n\n\t", 0.03)
        author = delay_input("\n\n\tSpecify the author: \n\n\t", 0.03)
        version = delay_input("\n\n\tSpecify the version: \n\n\t", 0.03)
        package = delay_input("\n\n\tSpecify the default package: \n\n\t", 0.03)
        main_class = delay_input("\n\n\tSpecify the main class: \n\n\t", 0.03)

        # Ask the user for their desired dependency settings.
        maven = delay_input("\n\n\tAre you going to use maven? (Y/N): ", 0.03)
        spigot_version = "-1"

        # Keep asking for an API version if not correctly specified.
        while not validate_api_version(spigot_version):
            spigot_version = delay_input("\n\tWhat version of Spigot? (1.8, 1.8.8, 1.9, ...): ", 0.03)
        if not str(spigot_version).endswith("-R0.1-SNAPSHOT"):
            spigot_version = spigot_version + "-R0.1-SNAPSHOT"
        print("\n")

        # Create a Plugin object, and build it using our data.
        plugin = Plugin(path, project, author, version, package, main_class, maven, spigot_version)
        plugin.build()

        # Finally, open our plugin in IntelliJ IDEA.
        plugin.open()
    except KeyboardInterrupt:
        os.system("cls")
        raise SystemExit
