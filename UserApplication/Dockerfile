FROM openjdk:latest
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} userapplication.jar
EXPOSE 8060
ENTRYPOINT ["java","-jar","/userapplication.jar"]