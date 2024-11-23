@echo off
setlocal enabledelayedexpansion



rem set M2_HOME=C:\apache-maven-3.5.3
rem set PATH=%M2_HOME%\bin

cd riskadmissionscalculateincomesv0Nuevo

call mvn kermit:trx

rem call mvn clean install

exit


