@echo off
setlocal enabledelayedexpansion



rem set M2_HOME=C:\apache-maven-3.5.3
rem set PATH=%M2_HOME%\bin


cd /d C:\Users\SURAMERICANA\PycharmProjects\chatbot\riskadmissionscalculateincomesv0Nuevo

call mvn kermit:trx

call mvn clean install

exit


