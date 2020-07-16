def generate_maven_file(package, project, version, spigot_version):
    with open("pom.xml", 'w') as pom:
        pom.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        pom.write('<project xmlns="http://maven.apache.org/POM/4.0.0"\n')
        pom.write('\t\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n')
        pom.write(
            '\t\txsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">\n')
        pom.write('\t<modelVersion>4.0.0</modelVersion>\n\n')

        # Writing basic plugin settings.
        pom.write('\t<groupId>' + package + '</groupId>\n')
        pom.write('\t<artifactId>' + project + '</artifactId>\n')
        pom.write('\t<version>' + version + '</version>\n\n')

        # Writing spigot repository.
        pom.write('\t<repositories>\n')
        pom.write('\t\t<repository>\n')
        pom.write('\t\t\t<id>spigot-repo</id>\n')
        pom.write('\t\t\t<url>https://hub.spigotmc.org/nexus/content/repositories/snapshots/</url>\n')
        pom.write('\t\t</repository>\n')
        pom.write('\t</repositories>\n\n')

        # Writing spigot dependency.
        pom.write('\t<dependencies>\n')
        pom.write('\t\t<dependency>\n')
        pom.write('\t\t\t<groupId>org.spigotmc</groupId>\n')
        pom.write('\t\t\t<artifactId>spigot-api</artifactId>\n')
        pom.write('\t\t\t<version>' + spigot_version + '</version>\n')
        pom.write('\t\t\t<scope>provided</scope>\n')
        pom.write('\t\t</dependency>\n')
        pom.write('\t</dependencies>\n')
        pom.write('</project>')
        pom.close()