FROM openjdk:latest
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} gateway.jar
EXPOSE 9191
ENTRYPOINT ["java","-jar","/gateway.jar"]
